import pandas as pd

class InsightsGenerator:
    def __init__(self, df):
        self.df = df

    def generate_category_summary(self):
        return self.df.groupby("category")["amount"].sum().to_dict()

    def detect_anomalies(self):
        anomalies = {}
        for cat in self.df["category"].unique():
            cat_df = self.df[self.df["category"] == cat]
            mean_amount = cat_df["amount"].mean()
            outliers = cat_df[cat_df["amount"] > 2*mean_amount]
            anomalies[cat] = outliers.to_dict('records')
        return anomalies

    def generate_insights(self):
        return {
            "category_summary": self.generate_category_summary(),
            "anomalies": self.detect_anomalies()
        }

if __name__ == "__main__":
    df = pd.read_csv("../sample-data/categorized_output.csv")
    insights = InsightsGenerator(df)
    print(insights.generate_insights())
