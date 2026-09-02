from agents.intent_agent import IntentAgent
from agents.recommendation_agent import RecommendationAgent
from agents.upsell_agent import UpsellAgent
from services.cart_service import CartService


class CommerceAgent:

    def __init__(self):
        self.intent_agent = IntentAgent()
        self.recommendation_agent = RecommendationAgent()
        self.upsell_agent = UpsellAgent()
        self.cart = CartService()

    def process_request(self, message):

        intent = self.intent_agent.extract_intent(message)

        product = self.recommendation_agent.recommend(intent)

        if not product:
            return {
                "success": False,
                "message": "I couldn't find a suitable product."
            }

        suggestions = self.upsell_agent.get_suggestions(product)

        self.cart.clear_cart()

        self.cart.add_item(product)

        return {
            "success": True,
            "intent": intent,
            "product": product,
            "suggestions": suggestions,
            "cart_items": self.cart.get_items(),
            "total": self.cart.get_total()
        }

    def add_product(self, product):

        self.cart.add_item(product)

        return {
            "cart_items": self.cart.get_items(),
            "total": self.cart.get_total()
        }