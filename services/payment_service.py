import os
import razorpay
from dotenv import load_dotenv

load_dotenv()


class PaymentService:

    def __init__(self):
        self.key_id = os.getenv("RAZORPAY_KEY_ID")
        self.key_secret = os.getenv("RAZORPAY_KEY_SECRET")

        if not self.key_id or not self.key_secret:
            raise ValueError(
                "Razorpay API keys are missing from .env"
            )

        self.client = razorpay.Client(
            auth=(self.key_id, self.key_secret)
        )

    def create_order(self, amount_rupees):

        amount_paise = int(amount_rupees * 100)

        order_data = {
            "amount": amount_paise,
            "currency": "INR",
            "receipt": "vendora_test_001"
        }

        order = self.client.order.create(
            data=order_data
        )

        return order


if __name__ == "__main__":

    payment = PaymentService()

    print("\nCreating Razorpay Test Order...")

    order = payment.create_order(16998)

    print("\n✅ Razorpay Order Created!")
    print(f"Order ID: {order['id']}")
    print(f"Amount: ₹{order['amount'] / 100}")
    print(f"Currency: {order['currency']}")
    print(f"Status: {order['status']}")