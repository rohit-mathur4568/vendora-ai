import pandas as pd
from pathlib import Path


class CatalogService:

    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        self.file_path = base_dir / "data" / "products.csv"

        self.products = pd.read_csv(self.file_path)

    def get_all_products(self):
        return self.products

    def search_products(self, query):
        query = query.lower()

        mask = (
            self.products["product_name"].str.lower().str.contains(query, na=False)
            |
            self.products["category"].str.lower().str.contains(query, na=False)
            |
            self.products["description"].str.lower().str.contains(query, na=False)
            |
            self.products["tags"].str.lower().str.contains(query, na=False)
        )

        return self.products[mask]

    def get_product(self, product_id):
        result = self.products[
            self.products["product_id"] == product_id
        ]

        if result.empty:
            return None

        return result.iloc[0].to_dict()


if __name__ == "__main__":
    catalog = CatalogService()

    print("\nAvailable Products:\n")
    print(catalog.get_all_products()[
        ["product_id", "product_name", "price"]
    ].to_string(index=False))

    print("\nSearch Result for 'Goa':\n")
    print(catalog.search_products("Goa")[
        ["product_id", "product_name", "price"]
    ].to_string(index=False))