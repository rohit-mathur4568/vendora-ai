import os
import hmac
import hashlib
from datetime import datetime

import razorpay
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from agents.commerce_agent import CommerceAgent


load_dotenv()

app = FastAPI(title="Vendora AI")

app.mount("/static", StaticFiles(directory="static"), name="static")

agent = CommerceAgent()

RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")

razorpay_client = razorpay.Client(
    auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET)
)

orders = {}
audit_logs = []


class ChatRequest(BaseModel):
    message: str


class PaymentRequest(BaseModel):
    amount: int


class VerifyPaymentRequest(BaseModel):
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/api/chat")
def chat(request: ChatRequest):

    result = agent.process_request(request.message)

    audit_logs.append({
        "timestamp": datetime.now().isoformat(),
        "event": "agent_request",
        "message": request.message,
        "success": result.get("success")
    })

    return result


@app.get("/api/cart")
def get_cart():

    return {
        "items": agent.cart.get_items(),
        "total": agent.cart.get_total()
    }


@app.post("/api/cart/add")
def add_to_cart(product: dict):

    result = agent.add_product(product)

    audit_logs.append({
        "timestamp": datetime.now().isoformat(),
        "event": "cart_add",
        "product": product.get("product_name")
    })

    return result


@app.post("/api/payment/create-order")
def create_payment_order(request: PaymentRequest):

    amount_paise = int(request.amount * 100)

    order = razorpay_client.order.create({
        "amount": amount_paise,
        "currency": "INR",
        "receipt": f"vendora_{len(orders) + 1}",
        "notes": {
            "product": "Vendora AI Commerce"
        }
    })

    orders[order["id"]] = {
        "amount": request.amount,
        "created_at": datetime.now().isoformat()
    }

    audit_logs.append({
        "timestamp": datetime.now().isoformat(),
        "event": "payment_order_created",
        "order_id": order["id"],
        "amount": request.amount
    })

    return {
        "order_id": order["id"],
        "amount": amount_paise,
        "currency": "INR",
        "key_id": RAZORPAY_KEY_ID
    }


@app.post("/api/payment/verify")
def verify_payment(request: VerifyPaymentRequest):

    if request.razorpay_order_id not in orders:
        return {
            "success": False,
            "message": "Unknown order."
        }

    body = (
        request.razorpay_order_id
        + "|"
        + request.razorpay_payment_id
    )

    generated_signature = hmac.new(
        RAZORPAY_KEY_SECRET.encode(),
        body.encode(),
        hashlib.sha256
    ).hexdigest()

    valid = hmac.compare_digest(
        generated_signature,
        request.razorpay_signature
    )

    if not valid:

        audit_logs.append({
            "timestamp": datetime.now().isoformat(),
            "event": "payment_verification_failed",
            "order_id": request.razorpay_order_id
        })

        return {
            "success": False,
            "message": "Payment verification failed."
        }

    order_data = orders[request.razorpay_order_id]

    audit_logs.append({
        "timestamp": datetime.now().isoformat(),
        "event": "payment_verified",
        "order_id": request.razorpay_order_id,
        "payment_id": request.razorpay_payment_id,
        "amount": order_data["amount"]
    })

    return {
        "success": True,
        "message": "Payment verified successfully!",
        "payment_id": request.razorpay_payment_id,
        "order_id": request.razorpay_order_id,
        "amount": order_data["amount"]
    }


@app.get("/api/audit")
def get_audit():

    return {
        "logs": audit_logs
    }