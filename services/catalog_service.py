import pandas as pd


class CatalogService:

    def __init__(self, file_path="data/products.csv"):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def _clean_record(self, record):
        cleaned = {}

        for key, value in record.items():

            if pd.isna(value):
                cleaned[key] = None
            elif hasattr(value, "item"):
                cleaned[key] = value.item()
            else:
                cleaned[key] = value

        return cleaned

    def get_all_products(self):

        records = self.df.to_dict(orient="records")

        return [
            self._clean_record(record)
            for record in records
        ]

    def search_products(self, query):

        query = query.lower()

        mask = (
            self.df["product_name"].fillna("").str.lower().str.contains(query)
            |
            self.df["category"].fillna("").str.lower().str.contains(query)
            |
            self.df["description"].fillna("").str.lower().str.contains(query)
            |
            self.df["tags"].fillna("").str.lower().str.contains(query)
        )

        records = self.df[mask].to_dict(orient="records")

        return [
            self._clean_record(record)
            for record in records
        ]

    def get_product(self, product_id):

        result = self.df[
            self.df["product_id"].astype(str) == str(product_id)
        ]

        if result.empty:
            return None

        record = result.iloc[0].to_dict()

        return self._clean_record(record)


if __name__ == "__main__":

    catalog = CatalogService()

    print("Total products:", len(catalog.get_all_products()))

    print("\nGoa products:")

    for product in catalog.search_products("goa"):
        print(product)

    print("\nProduct P001:")

    print(catalog.get_product("P001"))