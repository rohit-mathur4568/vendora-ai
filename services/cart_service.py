class CartService:

    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product_id):
        self.items = [
            item for item in self.items
            if item["product_id"] != product_id
        ]

    def get_total(self):
        return sum(
            item["price"] for item in self.items
        )

    def get_items(self):
        return self.items

    def clear_cart(self):
        self.items = []

    def show_cart(self):

        if not self.items:
            print("\nCart is empty.")
            return

        print("\n========== CART ==========")

        for item in self.items:
            print(
                f"{item['product_name']} "
                f"- ₹{item['price']}"
            )

        print("--------------------------")
        print(f"Total: ₹{self.get_total()}")
        print("==========================")


if __name__ == "__main__":

    from services.catalog_service import CatalogService

    catalog = CatalogService()
    cart = CartService()

    # Main product
    main_product = catalog.get_product("P001")

    # Upsell
    hotel_upgrade = catalog.get_product("P002")

    # Add products
    cart.add_item(main_product)
    cart.add_item(hotel_upgrade)

    cart.show_cart()