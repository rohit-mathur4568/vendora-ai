🚀 Vendora AI – Autonomous Commerce & Revenue Growth Agent

Turning customer intent into recommendation, revenue growth, and payment — in one intelligent commerce flow.

Vendora AI is an agentic commerce prototype designed to help merchants convert natural-language customer intent into a complete shopping journey.

Instead of forcing customers to browse products manually, Vendora understands what the customer wants, recommends a suitable product, suggests relevant upsells and cross-sells, builds the cart, and completes the transaction through Razorpay Test Mode.

🎯 Problem

Traditional e-commerce journeys often separate:

Customer intent
Product discovery
Recommendations
Upselling
Cart creation
Payment

This creates friction and can lead to lost conversions.

For example:

"I want a Goa trip under ₹18,000 for 3 days."

A traditional system may require the customer to search, filter, compare and manually select products.

Vendora AI turns this into a conversational commerce journey.

💡 Solution

Vendora AI follows this workflow:

Customer Intent
      ↓
Intent Understanding
      ↓
Product Recommendation
      ↓
Upsell / Cross-sell
      ↓
Customer Approval
      ↓
Cart Creation
      ↓
Razorpay Checkout
      ↓
Server-side Payment Verification
      ↓
Audit Trail

The goal is to make the merchant's catalog conversational and transactable.

🧠 Key Features
1. Conversational Shopping

Customers can describe their requirements naturally.

Example:

I want a Goa trip under 18k for 3 days

Vendora extracts:

Destination
Budget
Duration
Category
2. Smart Product Recommendation

The recommendation agent matches customer requirements with the available merchant catalog.

Example:

Goa Explorer Package

₹14,999
⭐ 4.5 Rating

3. Revenue Growth Agent

Vendora identifies relevant revenue opportunities.

Upsell

Premium Hotel Upgrade

₹1,999

Cross-sell

Airport Transfer

₹799

This can help merchants increase:

Average Order Value
Revenue per customer
Cross-sell opportunities
4. Customer-Controlled Actions

The agent does not silently purchase additional products.

The customer explicitly chooses:

Add Upgrade
Add Recommendation
Continue Without Add-ons

This keeps revenue-growth actions bounded and customer-controlled.

5. Razorpay Payment Integration

Vendora creates a Razorpay order and opens Razorpay Checkout.

Vendora
   ↓
Create Razorpay Order
   ↓
Razorpay Checkout
   ↓
Payment
   ↓
Server-side Signature Verification
   ↓
Payment Success

The project uses Razorpay Test Mode, so no real money is involved.

6. Payment Failure Handling

If payment fails, the customer is informed while the cart remains safe.

Example:

⚠️ Payment Failed

Don't worry — your cart is still safe.

7. Audit Trail

Important commerce events can be recorded:

Agent Request
Cart Add
Payment Order Created
Payment Verification
Payment Verification Failure

This provides visibility into the commerce workflow.

🏗️ Architecture
                         ┌─────────────────┐
                         │    Customer     │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │  Web Interface  │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Commerce Agent  │
                         └────────┬────────┘
                                  │
                 ┌────────────────┼────────────────┐
                 ▼                ▼                ▼
        ┌────────────────┐ ┌───────────────┐ ┌──────────────────┐
        │  Intent Agent  │ │ Recommendation│ │ Upsell /         │
        │                │ │    Agent      │ │ Cross-sell Agent │
        └────────────────┘ └───────┬───────┘ └──────────────────┘
                                   │
                                   ▼
                           ┌───────────────┐
                           │Merchant       │
                           │Catalog        │
                           └───────┬───────┘
                                   │
                                   ▼
                           ┌───────────────┐
                           │ Cart Service  │
                           └───────┬───────┘
                                   │
                                   ▼
                           ┌───────────────┐
                           │ FastAPI       │
                           │ Backend       │
                           └───────┬───────┘
                                   │
                                   ▼
                           ┌───────────────┐
                           │   Razorpay    │
                           │  Test Mode    │
                           └───────┬───────┘
                                   │
                                   ▼
                           ┌───────────────┐
                           │   Checkout    │
                           └───────┬───────┘
                                   │
                                   ▼
                     ┌──────────────────────────┐
                     │ Server-side Verification │
                     └────────────┬─────────────┘
                                  │
                                  ▼
                           ┌───────────────┐
                           │  Audit Trail  │
                           └───────────────┘
🔄 Complete Demo Flow
Step 1 — Customer Intent

Customer enters:

I want a Goa trip under 18k for 3 days

Step 2 — Agent Understanding

Vendora identifies:

Destination: Goa
Budget: ₹18,000
Duration: 3 days
Category: Travel
Step 3 — Recommendation

Goa Explorer Package

₹14,999
⭐ 4.5

Step 4 — Revenue Growth

Vendora suggests:

Premium Hotel Upgrade — ₹1,999

Airport Transfer — ₹799

Step 5 — Customer Approval

Customer decides which recommendations to add.

Step 6 — Cart
Goa Explorer Package       ₹14,999
Premium Hotel Upgrade       ₹1,999
-----------------------------------
Total                      ₹16,998
Step 7 — Payment

Customer clicks:

Proceed to Razorpay

Razorpay Test Mode Checkout opens.

Step 8 — Verification

The backend verifies the Razorpay payment signature before confirming the transaction.

💰 Revenue Growth Example
Without Upsell

Base Product = ₹14,999

With Relevant Upsell
Base Product       ₹14,999
Hotel Upgrade       ₹1,999
---------------------------
Total              ₹16,998

Potential additional order value = ₹1,999

This demonstrates how agentic recommendations can directly contribute to merchant revenue.

🛡️ Safety & Trust

Vendora follows a bounded commerce approach:

Customer approval before adding optional products
Payment actions require explicit checkout
Razorpay payment signature is verified server-side
Payment failures are handled gracefully
Important commerce events can be audited
No real money is processed in the demo
🧪 Demo Data

The current prototype uses a synthetic/demo merchant catalog.

Example products:

Goa Explorer Package
Manali Adventure Package
Jaipur Heritage Package
Hotel Upgrades
Airport Transfer
Adventure Activity Pass
Local Tour Pass

In a production environment, the catalog could connect to:

Product database
Inventory system
Pricing system
CRM
Promotions
Order management system
🛠️ Tech Stack
Backend
Python
FastAPI
Pydantic
Commerce Logic
Agent-based architecture
Intent extraction
Recommendation engine
Upsell / Cross-sell engine
Cart service
Payment
Razorpay Test Mode
Razorpay Checkout
Server-side HMAC SHA256 verification
Data
CSV-based demo catalog
Pandas
Frontend
HTML
CSS
JavaScript
Deployment
GitHub
Render
📁 Project Structure
VendoraAI/
│
├── agents/
│   ├── commerce_agent.py
│   ├── intent_agent.py
│   ├── recommendation_agent.py
│   └── upsell_agent.py
│
├── services/
│   ├── catalog_service.py
│   ├── cart_service.py
│   ├── payment_service.py
│   └── approval_service.py
│
├── data/
│   └── products.csv
│
├── static/
│   └── index.html
│
├── models/
├── utils/
│
├── api.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
🚀 Running Locally
1. Clone Repository
git clone https://github.com/rohit-mathur4568/vendora-ai.git
cd vendora-ai
2. Create Virtual Environment
python -m venv venv
3. Activate Environment

Windows:

venv\Scripts\activate
4. Install Dependencies
pip install -r requirements.txt
5. Configure Razorpay Test Mode

Create .env:

RAZORPAY_KEY_ID=your_test_key_id
RAZORPAY_KEY_SECRET=your_test_key_secret

Never commit .env or Razorpay secrets to GitHub.

6. Start Server
uvicorn api:app --reload

Open:

http://127.0.0.1:8000
🌐 Live Demo

Vendora AI

https://vendora-ai-i4y2.onrender.com

The demo uses Razorpay Test Mode and synthetic catalog data.

🔮 Future Scope
AI Improvements
LLM-based intent reasoning
Context-aware multi-turn conversations
Personalized recommendations
Customer preference memory
Natural-language product search
Merchant Intelligence
Real-time inventory
Dynamic pricing
Campaign generation
Customer segmentation
Revenue analytics
Agentic Commerce
AI-readable product catalogs
AI buyer integration
Conversational checkout
Automated offer optimization
Multi-merchant commerce agents
Production Infrastructure
Database-backed carts
Persistent audit logs
Razorpay webhooks
Authentication
Merchant dashboard
Real-time inventory synchronization
🏆 Buildathon Vision

Vendora AI explores a simple idea:

What if a customer could describe what they want, and an AI agent could take them from intent to transaction?

The long-term vision is to reduce the distance between:

Intent → Discovery → Decision → Transaction

and turn it into one intelligent, explainable commerce experience.

🎯 Razorpay AI Buildathon 2026
Track

AI Growth & Agentic Commerce

Core Idea
Customer Intent
       ↓
AI Recommendation
       ↓
Revenue Growth
       ↓
Customer Approval
       ↓
Transaction

Vendora AI demonstrates how an intelligent commerce agent can connect customer intent with merchant revenue and payment in a single workflow.

📌 Important Note

This project is a prototype built for demonstration purposes.

Catalog data is synthetic/demo data.
Payments use Razorpay Test Mode.
No real customer money is processed.
Production deployment would require persistent storage, authentication, webhooks, real merchant data integrations, and additional security controls.