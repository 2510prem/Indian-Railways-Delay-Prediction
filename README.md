## Automated EDA (YData Profiling)
An automated exploratory data analysis report was generated using YData Profiling to validate manual EDA findings. The report includes statistical summaries, distribution analysis, correlation insights, and data quality checks.

## Data Quality & Profiling Alerts
- Delay values show right-skewed distribution due to occasional extreme delays
- Train number has high cardinality and requires careful handling during modeling
- Distance shows positive correlation with delay, indicating cumulative operational impact
- Outliers in delay represent real-world disruptions and were retained

## Feature Engineering
- Removed high-cardinality identifiers such as train number
- Encoded categorical features using one-hot encoding
- Prepared numerical features for model training
- Split data into training and testing sets

## Model Training & Evaluation
- Trained Linear Regression as a baseline model
- Implemented Decision Tree and Random Forest regressors
- Evaluated models using RMSE and R² score
- Selected Random Forest as the final model

## Model Deployment
The trained machine learning model was deployed using Streamlit to create an interactive web application where users can input train and journey details to predict expected delays.

## Deployment
The trained machine learning model was deployed using Streamlit. The web application allows users to input train and journey details to predict expected train delays in real time.