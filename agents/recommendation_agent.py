from services.catalog_service import CatalogService
from agents.intent_agent import IntentAgent


class RecommendationAgent:

    def __init__(self):
        self.catalog = CatalogService()

    def recommend(self, intent):

        # No customer information = no recommendation
        if (
            not intent["destination"]
            and not intent["budget"]
            and not intent["duration_days"]
        ):
            return None

        products = self.catalog.get_all_products().copy()

        # Only travel packages
        products = products[
            products["category"].str.lower() == "travel"
        ]

        # Destination filter
        if intent["destination"]:
            destination = intent["destination"].lower()

            products = products[
                products["tags"]
                .str.lower()
                .str.contains(destination, na=False)
            ]

        # Duration filter
        if intent["duration_days"]:
            duration = intent["duration_days"]

            products = products[
                products["description"]
                .str.lower()
                .str.contains(
                    f"{duration} days",
                    na=False
                )
            ]

        # Budget filter
        if intent["budget"]:
            products = products[
                products["price"] <= intent["budget"]
            ]

        # No matching product
        if products.empty:
            return None

        # Highest rated matching product
        products = products.sort_values(
            by="rating",
            ascending=False
        )

        return products.iloc[0].to_dict()


if __name__ == "__main__":

    intent_agent = IntentAgent()
    recommendation_agent = RecommendationAgent()

    message = input("\nEnter customer request: ")

    intent = intent_agent.extract_intent(message)

    print("\nDetected Intent:")
    print(intent)

    recommendation = recommendation_agent.recommend(intent)

    print("\nRecommended Product:")

    if recommendation:
        print(
            f"""
Product: {recommendation['product_name']}
Price: ₹{recommendation['price']}
Rating: ⭐ {recommendation['rating']}
Description: {recommendation['description']}
"""
        )
    else:
        print("Sorry, no matching product found.")