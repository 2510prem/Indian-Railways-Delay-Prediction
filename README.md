# 🚆 Indian Railways Train Delay Prediction System

## 📌 Project Overview
Train delays are a common issue in Indian Railways and significantly impact passengers.  
This project aims to predict expected train delays using machine learning based on train type, route, distance, day of travel, and seasonal factors.

The project covers the complete machine learning lifecycle — from data generation and analysis to model deployment using Streamlit.

---

## 🎯 Problem Statement
Passengers often do not know whether a train will arrive on time or be delayed.  
This project predicts the expected delay (in minutes) to help passengers plan their journeys better.

---

## 📊 Dataset
- The dataset used in this project is **synthetic data** generated using realistic assumptions.
- Due to the absence of a public Indian Railways delay API, data was simulated considering:
  - Train type
  - Route distance
  - Day of week
  - Seasonal effects (monsoon, winter fog)

📌 The dataset is intended for **academic and learning purposes**.

---

## 🔍 Exploratory Data Analysis (EDA)
EDA was performed to understand delay patterns and trends:
- Distribution of train delays
- Delay vs train type
- Delay vs distance
- Seasonal and weekday effects
- Route-level delay analysis

Automated EDA was also generated using **YData Profiling** to validate manual findings.

---

## ⚙️ Feature Engineering
- Removed high-cardinality identifiers like `train_number`
- Encoded categorical variables using **One-Hot Encoding**
- Retained numerical features such as distance and month
- Prepared data using `ColumnTransformer`

---

## 🤖 Machine Learning Models
The following models were trained and evaluated:
- Linear Regression (baseline)
- Decision Tree Regressor
- Random Forest Regressor ✅ (best performing)

### 📈 Evaluation Metrics
- RMSE (Root Mean Squared Error)
- R² Score

Random Forest achieved the best performance due to its ability to capture non-linear patterns.

---

## 🚀 Deployment
The trained model was deployed using **Streamlit** as an interactive web application.  
Users can input train and journey details to get real-time delay predictions.

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- YData Profiling
- Streamlit
- Git & GitHub

---

## ▶️ How to Run the Project Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/2510prem/Indian-Railways-Delay-Prediction.git
