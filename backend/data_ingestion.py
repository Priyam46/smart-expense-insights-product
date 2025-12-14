import pandas as pd

class DataIngestion:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_csv(self):
        """Load transactions from CSV."""
        self.df = pd.read_csv(self.file_path)
        required_cols = ["date", "description", "amount", "category"]
        for col in required_cols:
            if col not in self.df.columns:
                self.df[col] = None
        return self.df

    def preview(self, n=5):
        return self.df.head(n)

if __name__ == "__main__":
    ingestion = DataIngestion("../sample-data/transactions.csv")
    df = ingestion.load_csv()
    print(df.head())
