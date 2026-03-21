# US Accidents Severity Prediction (2016–2023)

This project predicts **accident severity** using the public **US Accidents Dataset**, containing over 7 million records of traffic incidents across the United States.  
The goal is to build an **end-to-end machine learning pipeline**, including:


- Exploratory Data Analysis (EDA)
- Missing value treatment
- Outlier handling
- Feature engineering (time, weather, geographical, traffic conditions)
- Data preprocessing using pipelines
- Model training (Logistic Regression, Random Forest, XGBoost)
- Evaluation metrics & visualizations
- SHAP explainability
- Reproducible Jupyter Notebook
- 
---

## 📁 Project Structure

```text
US-Accidents-Prediction/
│
├── data/
│ └── US_Accidents.csv
│
├── notebooks/
│ └── accident_severity_analysis.ipynb
│
├── src/
│ ├── preprocessing.py
│ ├── eda.py
│ └── model_training.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
