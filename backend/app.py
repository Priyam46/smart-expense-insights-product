from flask import Flask, jsonify
import pandas as pd
from categorization import TransactionCategorizer
from insights import InsightsGenerator

app = Flask(__name__)
TRANSACTION_FILE = "../sample-data/transactions.csv"

@app.route("/transactions", methods=["GET"])
def transactions():
    df = pd.read_csv(TRANSACTION_FILE)
    df = TransactionCategorizer(df).categorize()
    return df.to_json(orient="records")

@app.route("/insights", methods=["GET"])
def insights():
    df = pd.read_csv(TRANSACTION_FILE)
    df = TransactionCategorizer(df).categorize()
    insights = InsightsGenerator(df).generate_insights()
    return jsonify(insights)

if __name__ == "__main__":
    app.run(debug=True)
