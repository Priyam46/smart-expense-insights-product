import streamlit as st
import pandas as pd
import sys
sys.path.append("../backend")
from categorization import TransactionCategorizer
from insights import InsightsGenerator

st.title("Smart Expense Insights Dashboard")

df = pd.read_csv("../sample-data/transactions.csv")
df = TransactionCategorizer(df).categorize()
st.subheader("Transactions")
st.dataframe(df)

insights = InsightsGenerator(df).generate_insights()
st.subheader("Insights")
st.json(insights)
