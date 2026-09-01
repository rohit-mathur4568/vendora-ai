from services.catalog_service import CatalogService


class UpsellAgent:

    def __init__(self):
        self.catalog = CatalogService()

    def get_suggestions(self, product):

        suggestions = {
            "upsell": None,
            "cross_sell": None
        }

        # -------------------------
        # Upsell Product
        # -------------------------
        upsell_id = product.get("upsell_product")

        if upsell_id:
            suggestions["upsell"] = self.catalog.get_product(
                upsell_id
            )

        # -------------------------
        # Cross-sell Product
        # -------------------------
        cross_sell_id = product.get("cross_sell_product")

        if cross_sell_id:
            suggestions["cross_sell"] = self.catalog.get_product(
                cross_sell_id
            )

        return suggestions


if __name__ == "__main__":

    catalog = CatalogService()
    agent = UpsellAgent()

    product = catalog.get_product("P001")

    suggestions = agent.get_suggestions(product)

    print("\nSelected Product:")
    print(
        f"{product['product_name']} - ₹{product['price']}"
    )

    print("\nUpsell Suggestion:")

    if suggestions["upsell"]:
        item = suggestions["upsell"]

        print(
            f"{item['product_name']} - ₹{item['price']}"
        )
    else:
        print("No upsell available.")

    print("\nCross-sell Suggestion:")

    if suggestions["cross_sell"]:
        item = suggestions["cross_sell"]

        print(
            f"{item['product_name']} - ₹{item['price']}"
        )
    else:
        print("No cross-sell available.")