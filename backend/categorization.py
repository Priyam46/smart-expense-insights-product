import pandas as pd

CATEGORY_RULES = {
    "grocery": ["supermarket", "grocery", "mart"],
    "entertainment": ["cinema", "netflix", "spotify"],
    "transport": ["uber", "ola", "metro"],
    "subscription": ["subscription", "membership", "spotify"],
    "utilities": ["electricity", "water", "internet"],
    "others": []
}

class TransactionCategorizer:
    def __init__(self, df):
        self.df = df

    def categorize(self):
        self.df["category"] = self.df["description"].apply(self._categorize_transaction)
        return self.df

    def _categorize_transaction(self, description):
        desc = str(description).lower()
        for cat, keywords in CATEGORY_RULES.items():
            if any(word in desc for word in keywords):
                return cat
        return "others"

if __name__ == "__main__":
    df = pd.read_csv("../sample-data/transactions.csv")
    categorizer = TransactionCategorizer(df)
    df = categorizer.categorize()
    df.to_csv("../sample-data/categorized_output.csv", index=False)
    print(df.head())
