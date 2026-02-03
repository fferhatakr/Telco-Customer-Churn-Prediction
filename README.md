# 📉 Telco Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-v1.0%20Released-green)

## 🚀 Project Overview

This project focuses on predicting customer churn for a telecommunications company using Machine Learning techniques.

The main objective is to identify customers who are likely to leave (churn) and provide actionable insights to reduce revenue loss.  
Special attention is given to **imbalanced data** and the **trade-off between Accuracy and Recall**.

Special focus is given to:

- **Imbalanced datasets**
- **Recall–Accuracy trade-offs**
- **Real-world data quality issues**

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
- **Pandas & NumPy** – Data manipulation and preprocessing
- **Matplotlib & Seaborn** – Exploratory Data Analysis (EDA)
- **Scikit-Learn** – Machine Learning models and evaluation

## 📊 Key Business Insights

- High Monthly Charges increase churn probability.
- Month-to-month contracts have significantly higher churn rates.
- Fiber Optic users show higher dissatisfaction.
- New customers churn more frequently during the first months.
  -Senior customers combined with low tenure exhibit higher churn risk

## 📈 Model Performance & Evolution

### ⚠️ Challenge: Imbalanced Dataset

- 73% Loyal customers
- 26% Churn customers

A naive model achieves high accuracy but fails to detect churners.

### ✅ Solution Strategy

- **Class Weighting:** `class_weight='balanced'`
- **Threshold Tuning:** Probability threshold adjusted from `0.50 → 0.30`

## 📊 Model Comparison

| Model                              | Accuracy  | Recall (Churn Detection) | Verdict                                                                     |
| :--------------------------------- | :-------- | :----------------------- | :-------------------------------------------------------------------------- |
| **Logistic Regression**            | 74.8%     | 65.0%                    | Good recall but low precision (High False Alarms).                          |
| **Random Forest**                  | 79.2%     | 47.0%                    | High accuracy but missed >50% of churners.                                  |
| **KNN**                            | 76.4%     | 43.0%                    |                                                                             |
| **Standard XGBoost**               | 80.5%     | 46.0%                    |                                                                             |
| **GridSearch XGBoost**             | 80.9%     | 46.0%                    |                                                                             |
| **Weighted XGBoost (Selected) 🌟** | **75.0%** | **82.5%**                | **Best Model.** Sacrificed some accuracy to catch 82% of leaving customers. |

## ▶️ How to Run

```bash
git clone https://github.com/fferhatakr/Telco-Customer-Churn-Prediction.git
cd Telco-Customer-Churn-Prediction
pip install pandas numpy matplotlib seaborn scikit-learn
```
