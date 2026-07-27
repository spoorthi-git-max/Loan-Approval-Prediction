# 🏦 Loan Approval Prediction System

A Machine Learning-based web application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on applicant details. The application is built using **Python**, **Scikit-learn**, and **Streamlit**, providing an interactive interface for users to explore the dataset and make real-time predictions.

---
## 🚀 Live Demo

**Streamlit App:** https://loan-approval-prediction-tg2rxdvdcvmhnory9jz4pz.streamlit.app/
## 📌 Project Overview

Financial institutions receive thousands of loan applications every day. Evaluating each application manually is time-consuming and prone to human error.

This project leverages **Machine Learning** to automate the loan approval prediction process by analyzing applicant information such as income, education, employment status, credit history, and loan amount.

The application allows users to:
- Explore the loan dataset
- Visualize key insights
- Enter applicant information
- Predict loan approval instantly
- View the model's confidence score

---

## 🎯 Objectives

- Analyze the loan approval dataset.
- Perform data preprocessing and cleaning.
- Train a Machine Learning model for loan prediction.
- Build an interactive web application using Streamlit.
- Provide accurate loan approval predictions.

---

## 📂 Dataset

The dataset contains applicant information such as:

- Loan ID
- Gender
- Marital Status
- Number of Dependents
- Education
- Self Employed
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area
- Loan Status (Target)

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

## 📊 Machine Learning Algorithm

The project uses:

- **Logistic Regression**

The workflow includes:

1. Data Cleaning
2. Missing Value Handling
3. Label Encoding
4. Train-Test Split
5. Model Training
6. Prediction
7. Performance Evaluation

The application trains a Logistic Regression model on the processed dataset and reports its prediction accuracy. :contentReference[oaicite:0]{index=0}

---

## 📱 Application Features

- 📊 Dataset Overview
- 📋 Dataset Preview
- 📈 Summary Statistics
- 🔍 Missing Value Analysis
- 📉 Loan Status Visualization
- 🤖 Loan Approval Prediction
- 📌 Prediction Confidence Score

The Streamlit app includes dataset exploration, model training, and an interactive form for predicting loan approval based on user input. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

---

## 📁 Project Structure

```
Loan-Approval-Prediction/
│
├── app.py
├── Loan.ipynb
├── loan_data_set.csv
├── clean_loan_data_set.csv
├── README.md
└── requirements.txt
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Loan-Approval-Prediction.git
```

Move to the project directory

```bash
cd Loan-Approval-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📸 Application Workflow

```
Load Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Encoding
      │
      ▼
Train Logistic Regression Model
      │
      ▼
Evaluate Model
      │
      ▼
User Inputs Applicant Details
      │
      ▼
Predict Loan Status
      │
      ▼
Display Approval/Rejection & Confidence
```

---

## 📈 Results

The trained Logistic Regression model predicts whether a loan application will be:

- ✅ Approved
- ❌ Rejected

The application also displays the confidence level of each prediction.

---

## 🔮 Future Enhancements

- Deploy on Streamlit Community Cloud
- Save trained model using Pickle/Joblib
- Compare multiple Machine Learning algorithms
- Hyperparameter tuning
- Feature importance visualization
- User authentication
- Database integration
- Model explainability using SHAP

---

## 📚 Learning Outcomes

Through this project, the following concepts were implemented:

- Data preprocessing
- Handling missing values
- Label encoding
- Exploratory Data Analysis (EDA)
- Logistic Regression
- Model evaluation
- Streamlit application development
- Machine Learning deployment

---

## 👨‍💻 Author

**Your Name**

Capstone Project

---

## 📄 License

This project is developed for educational and learning purposes.
