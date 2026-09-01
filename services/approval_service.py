class ApprovalService:

    def ask_customer(self, suggestions):

        print("\n========== ADD-ON OPTIONS ==========")

        if suggestions["upsell"]:
            item = suggestions["upsell"]

            print(
                f"1. Add {item['product_name']} "
                f"- ₹{item['price']}"
            )

        if suggestions["cross_sell"]:
            item = suggestions["cross_sell"]

            print(
                f"2. Add {item['product_name']} "
                f"- ₹{item['price']}"
            )

        print("3. Continue without add-ons")

        choice = input("\nChoose an option: ")

        return choice


if __name__ == "__main__":

    approval = ApprovalService()

    test_suggestions = {
        "upsell": {
            "product_name": "Premium Hotel Upgrade",
            "price": 1999
        },
        "cross_sell": {
            "product_name": "Airport Transfer",
            "price": 799
        }
    }

    choice = approval.ask_customer(test_suggestions)

    print(f"\nCustomer selected option: {choice}")