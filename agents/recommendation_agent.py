from agents.intent_agent import IntentAgent
from services.catalog_service import CatalogService


class RecommendationAgent:

    def __init__(self):
        self.catalog = CatalogService()
        self.intent_agent = IntentAgent()

    def recommend(self, intent):

        products = self.catalog.get_all_products()

        # Only travel packages
        products = [
            p for p in products
            if str(p.get("category", "")).lower() == "travel"
        ]

        destination = intent.get("destination")
        budget = intent.get("budget")
        duration = intent.get("duration_days")

        # Destination filter
        if destination:
            destination = destination.lower()

            products = [
                p for p in products
                if destination in str(p.get("tags", "")).lower()
                or destination in str(p.get("product_name", "")).lower()
                or destination in str(p.get("description", "")).lower()
            ]

        # Budget filter
        if budget:
            products = [
                p for p in products
                if float(p.get("price", 0)) <= float(budget)
            ]

        # Duration filter
        if duration:

            duration_text = f"{duration}-day"

            filtered = [
                p for p in products
                if duration_text in str(p.get("tags", "")).lower()
            ]

            # Don't fail completely if duration is not in tags
            if filtered:
                products = filtered

        if not products:
            return None

        # Highest rated product
        products.sort(
            key=lambda p: float(p.get("rating", 0)),
            reverse=True
        )

        return products[0]


if __name__ == "__main__":

    agent = RecommendationAgent()

    intent = {
        "destination": "goa",
        "budget": 18000,
        "duration_days": 3,
        "category": "travel"
    }

    result = agent.recommend(intent)

    print("\nRecommended Product:")
    print(result) 