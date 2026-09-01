from agents.intent_agent import IntentAgent
from agents.recommendation_agent import RecommendationAgent
from agents.upsell_agent import UpsellAgent
from services.cart_service import CartService
from services.approval_service import ApprovalService


class CommerceAgent:

    def __init__(self):
        self.intent_agent = IntentAgent()
        self.recommendation_agent = RecommendationAgent()
        self.upsell_agent = UpsellAgent()
        self.cart = CartService()
        self.approval = ApprovalService()

    def process_request(self, message):

        # 1. Understand customer intent
        intent = self.intent_agent.extract_intent(message)

        print("\n========== CUSTOMER INTENT ==========")
        print(intent)

        # 2. Find best product
        product = self.recommendation_agent.recommend(intent)

        if not product:
            print("\nSorry, I could not find a suitable product.")
            return False

        print("\n========== RECOMMENDATION ==========")
        print(
            f"{product['product_name']} - ₹{product['price']}"
        )

        # 3. Add main product to cart
        self.cart.add_item(product)

        # 4. Find upsell/cross-sell
        suggestions = self.upsell_agent.get_suggestions(product)

        # 5. Ask customer for approval
        choice = self.approval.ask_customer(suggestions)

        # 6. Process customer choice
        if choice == "1" and suggestions["upsell"]:

            self.cart.add_item(
                suggestions["upsell"]
            )

            print("\n✅ Upsell added to cart.")

        elif choice == "2" and suggestions["cross_sell"]:

            self.cart.add_item(
                suggestions["cross_sell"]
            )

            print("\n✅ Cross-sell added to cart.")

        elif choice == "3":

            print("\n✅ Continuing without add-ons.")

        else:

            print("\nInvalid choice. Continuing with main product only.")

        # 7. Show final cart
        print("\n========== FINAL CART ==========")

        self.cart.show_cart()

        return True


if __name__ == "__main__":

    agent = CommerceAgent()

    message = input(
        "\nWhat are you looking for?\n> "
    )

    agent.process_request(message)