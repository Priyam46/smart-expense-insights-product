# Product Requirements Document (PRD) – Smart Expense Insights

## 1. Product Overview
**Product Name:** Smart Expense Insights  
**Category:** Personal Finance / Expense Management  
**Target Platforms:** Web (desktop MVP via Streamlit), future mobile app  
**Objective:** Help users **track, categorize, and analyze personal expenses**, receive actionable insights, and optimize spending to increase savings.  

---

## 2. Problem Statement
Users face multiple challenges managing personal finances:  
- Difficulty understanding **where their money is going** each month.  
- **Unidentified recurring expenses**, leading to overspending.  
- Lack of **personalized, actionable recommendations** for saving.  
- Existing solutions are often **manual, generic, or confusing**, leading to poor engagement.  

---

## 3. Goals & Success Metrics

### Goals
- Automate categorization of user transactions.  
- Provide **visual dashboards** with monthly trends, category breakdowns, and alerts.  
- Deliver **personalized recommendations** for cost-saving and budgeting.  
- Enable tracking of **financial goals and spending behavior** over time.  

### Success Metrics
| Metric | Target / Measure |
|--------|-----------------|
| Engagement | Daily/weekly active users |
| Categorization Accuracy | ≥90% transactions correctly categorized |
| Retention | ≥70% users retained at 3 months |
| Financial Impact | Average ₹ saved per user per month |
| User Satisfaction | Survey rating ≥4/5 |

---

## 4. User Personas

### Persona 1: Young Professionals (22–35)
- Goals: Track expenses, optimize budget, save efficiently  
- Behavior: Tech-savvy, prefers quick insights, minimal manual entry  
- Pain Points: Hard to identify overspending or recurring subscriptions  

### Persona 2: Students / Early Career
- Goals: Budget efficiently, save for goals  
- Behavior: Needs gamified or simple guidance  
- Pain Points: Overwhelmed by manual tracking, lacks insights  

---

## 5. Solution Overview
Smart Expense Insights will provide:  
1. **Automated Transaction Categorization** – ML/Rule-based engine to classify expenses.  
2. **Visual Dashboards** – Monthly trends, category breakdowns, anomalies.  
3. **Alerts & Notifications** – Detect unusual spending patterns or high expenses.  
4. **Personalized Recommendations** – Suggestions to save money or adjust budget.  
5. **Goal Tracking** – Users can set financial targets and monitor progress.  

---

## 6. Features / Modules

### 6.1 Data Ingestion
- Upload CSV or connect via bank API (mock CSV for MVP)  
- Validate and preprocess transaction data  

### 6.2 Categorization Engine
- ML or rule-based classification of transactions  
- Handles unknown merchants via fallback rules  
- Stores category for further insights  

### 6.3 Insights Engine
- Aggregate spending by category  
- Detect anomalies: spending >2x category average  
- Generate actionable recommendations  

### 6.4 Dashboard / Visualization
- Table of transactions with categories  
- Monthly spending charts per category  
- Highlight anomalies and alerts  

### 6.5 Notifications & Alerts
- Daily or weekly alerts for unusual spending  
- Personalized messages for saving opportunities  

### 6.6 Feedback Loop
- Users can correct misclassified transactions  
- Engine retrains to improve accuracy over time  

---

## 7. Technical Considerations
- **Backend:** Python, Flask  
- **Frontend:** Streamlit for MVP, React.js in future  
- **Database:** CSV (MVP), scalable to PostgreSQL  
- **ML:** Scikit-learn or rule-based categorization  
- **Deployment:** Docker + GitHub repo for version control  

---

## 8. Roadmap
**Phase 1 – MVP:**  
- CSV upload, rule-based categorization, dashboard with trends, alerts  

**Phase 2 – Enhanced Features:**  
- Bank API integration, personalized recommendations, gamification  

**Phase 3 – Scaling:**  
- ML-powered predictive insights, mobile app integration, advanced analytics  

---

## 9. Trade-offs
- **Rule-based vs ML categorization:** Rule-based for explainability and fast MVP.  
- **CSV vs API ingestion:** CSV easier for MVP, API for scale.  
- **Alert frequency:** Only notify significant deviations to reduce alert fatigue.  

---

## 10. Mockups / Wireframes
- Dashboard: Transaction table, category breakdown chart, anomaly highlights  
- Alerts: Simple notification panel with actionable suggestions  
- Goal Tracking: Progress bar visualization for each financial goal  

---

## 11. References
- Personal finance management best practices  
- Banking CSV data structures  

