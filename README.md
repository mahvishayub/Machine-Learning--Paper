# Adult Income Prediction – Machine Learning Project

This project predicts whether an individual earns **more than $50K per year** using the **Adult Census Income Dataset**.  
The model is built using Python, Scikit-Learn, and a complete ML pipeline including preprocessing, model training, evaluation, and deployment with FastAPI + Streamlit.

---

## Project Workflow

### **1. Data Loading**
- Dataset: `adult.csv`
- Read using Pandas
- Missing values checked and handled

### **2. Exploratory Data Analysis (EDA)**
- Distribution of key features
- Class imbalance check
- Basic statistical summary

### **3. Preprocessing**
- **Categorical features** → OneHotEncoder  
- **Numerical features** → StandardScaler  
- Combined using **ColumnTransformer**

### **4. Baseline vs ML Modeling**
- Baseline: Predict most frequent class
- ML Models:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - XGBoost (optional)

### **5. Model Evaluation**
Metrics used:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Best model is selected for deployment.

---

## Best Model Used for Deployment
- Model: **Random Forest Classifier**
- Achieved accuracy: **XX%** (replace with your score)
- Model saved as:
