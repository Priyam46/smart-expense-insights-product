import pandas as pd
from datetime import datetime

def generate_alerts(df):
    alerts = []
    for cat in df["category"].unique():
        cat_df = df[df["category"] == cat]
        mean = cat_df["amount"].mean()
        high_spend = cat_df[cat_df["amount"] > 2*mean]
        for _, row in high_spend.iterrows():
            alerts.append(f"High spending alert: {row['description']} - ₹{row['amount']} in {cat}")
    return alerts

if __name__ == "__main__":
    df = pd.read_csv("../sample-data/categorized_output.csv")
    alerts = generate_alerts(df)
    for alert in alerts:
        print(alert)
