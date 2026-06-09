# 💻 Laptop Price Predictor

A Machine Learning web application that predicts laptop prices based on hardware specifications such as brand, processor, RAM, storage, display characteristics, operating system, and GPU configuration.

This project demonstrates the complete Machine Learning workflow, including Data Cleaning, Exploratory Data Analysis (EDA), Feature Engineering, Model Training, Evaluation, and Deployment using Streamlit.

---

## 🚀 Project Overview

Laptop prices vary significantly depending on their specifications. The objective of this project is to build a regression model capable of accurately predicting laptop prices based on various hardware and software features.

The project covers:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Development
- Model Evaluation
- Streamlit-based User Interface
- Real-Time Price Prediction

---

## 📊 Dataset

### Original Features

| Feature | Description |
|----------|------------|
| Unnamed: 0 | Index Column |
| Company | Laptop Brand |
| TypeName | Laptop Category |
| Inches | Screen Size |
| ScreenResolution | Display Resolution |
| Cpu | Processor Information |
| Ram | RAM Capacity |
| Memory | Storage Information |
| Gpu | Graphics Card Information |
| OpSys | Operating System |
| Weight | Laptop Weight |
| Price | Target Variable |

---

## ⚙️ Feature Engineering

Several raw features were transformed into meaningful features to improve model performance.

### Screen Resolution

Extracted:

- Touchscreen (0/1)
- IPS Panel (0/1)
- PPI (Pixels Per Inch)

### CPU

Extracted:

- CPU Brand

### Memory

Separated into:

- HDD Storage
- SSD Storage

### GPU

Extracted:

- GPU Brand

### Operating System

Categorized into:

- Windows
- Mac
- Linux
- Other OS

---

## 📌 Final Features Used for Training

```python
[
    'Company',
    'TypeName',
    'Ram',
    'Weight',
    'Touchscreen',
    'IPSPanel',
    'ppi',
    'CPU_brand',
    'HDD',
    'SSD',
    'Gpu_brand',
    'os'
]
```

### Target Variable

```python
Price
```

---

## 🔍 Exploratory Data Analysis (EDA)

Performed detailed analysis to understand:

- Brand-wise laptop distribution
- Price trends across companies
- Impact of RAM on laptop prices
- Relationship between storage and price
- CPU and GPU influence on pricing
- Weight vs Price correlation
- Operating system trends
- Display quality impact on laptop prices

Visualization tools used:

- Matplotlib
- Seaborn

---

## 🧹 Data Preprocessing

The following preprocessing techniques were applied:

- Missing Value Handling
- Data Cleaning
- Feature Extraction
- Categorical Encoding
- Feature Transformation
- Log Transformation of Target Variable
- Scikit-Learn Pipelines

---

## 🤖 Machine Learning Model

### Algorithm Used

**Random Forest Regressor**

Random Forest was chosen because it effectively captures complex relationships between laptop specifications and prices while maintaining strong generalization performance.

---

## 📈 Model Performance

| Metric | Value |
|----------|----------|
| Model | Random Forest Regressor |
| Accuracy (R² Score) | ~80% |

The model achieved approximately **80% prediction accuracy**, providing reliable laptop price estimations based on user-selected specifications.

---

## 🖥️ Streamlit Application

An interactive Streamlit web application was developed to allow users to predict laptop prices in real time.

### User Inputs

- Company
- Laptop Type
- RAM
- Weight
- Touchscreen Availability
- IPS Display
- Screen Resolution
- CPU Brand
- HDD Capacity
- SSD Capacity
- GPU Brand
- Operating System

### Output

- Predicted Laptop Price

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-Learn
- Random Forest Regressor

### Deployment

- Streamlit

---

## 📂 Project Structure

```bash
Laptop-Price-Predictor/
│
├── data/
│   └── laptop.csv
│
├── notebooks/
│   ├── EDA.ipynb
│   └── Model_Training.ipynb
│
├── artifacts/
│   ├── pipe.pkl
│   └── df.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## ▶️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Laptop-Price-Predictor.git
cd Laptop-Price-Predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Select laptop specifications through the Streamlit interface.
2. The input data is processed using the same preprocessing pipeline used during training.
3. The Random Forest model predicts the laptop price.
4. The predicted price is displayed instantly.

---

## 🎯 Key Learning Outcomes

Through this project, I gained practical experience in:

- Data Cleaning and Preprocessing
- Feature Engineering
- Exploratory Data Analysis
- Regression Modeling
- Model Evaluation
- Scikit-Learn Pipelines
- Streamlit Deployment
- End-to-End Machine Learning Project Development

---

## 🔮 Future Enhancements

- Hyperparameter Tuning
- XGBoost Implementation
- LightGBM Integration
- CatBoost Comparison
- AWS Deployment
- Model Explainability using SHAP
- Laptop Recommendation System

---

## 👨‍💻 Author

### Asmit Pandey

B.Tech (Artificial Intelligence & Data Science)

**Areas of Interest:**

- Machine Learning
- Large Language Models (LLMs)
- Data Science
- Full-Stack Development
- AI Applications

---

⭐ If you found this project useful, feel free to star the repository.
