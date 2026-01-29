# 📉 Telco Customer Churn Prediction
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-v1.0%20Released-green)

## 🚀 Project Overview
This project focuses on predicting customer churn for a telecommunications company using Machine Learning techniques.

The main objective is to identify customers who are likely to leave (churn) and provide actionable insights to reduce revenue loss.  
Special attention is given to **imbalanced data** and the **trade-off between Accuracy and Recall**.

---

## 📂 Project Structure
```text
├── data/
│   └── data.csv
├── notebooks/
│   └── churn_analysis.ipynb
├── models/              # (Future releases)
├── README.md
└── .gitignore
```


## 🛠️ Technologies Used
- **Python 3.11**
- **Pandas & NumPy** – Data manipulation
- **Matplotlib & Seaborn** – Data visualization
- **Scikit-Learn** – Machine Learning models


## 📊 Key Business Insights
- High Monthly Charges increase churn probability.
- Month-to-month contracts have significantly higher churn rates.
- Fiber Optic users show higher dissatisfaction.
- New customers churn more frequently during the first months.


## 📈 Model Performance & Evolution

### ⚠️ Challenge: Imbalanced Dataset
- 73% Loyal customers
- 26% Churn customers

A naive model achieves high accuracy but fails to detect churners.

### ✅ Solution Strategy
- **Class Weighting:** `class_weight='balanced'`
- **Threshold Tuning:** Probability threshold adjusted from `0.50 → 0.30`


## 📊 Model Comparison

| Model                    | Accuracy | Recall (Churn) | Comment |
|--------------------------|----------|----------------|---------|
| Logistic Regression      | 74%      | 83%            | Aggressive detection, high False Positives |
| Random Forest (Default)  | 79%      | 46%            | High accuracy but missed too many churners |
| Random Forest (Tuned) ✅ | 77%      | 73%            | Selected Model – Best balance |


## ▶️ How to Run
```bash
git clone https://github.com/fferhatakr/Telco-Customer-Churn-Prediction.git
cd Telco-Customer-Churn-Prediction
pip install pandas numpy matplotlib seaborn scikit-learn
```

