
# 🧠 Multiple Disease Prediction System

A machine learning web application that predicts the risk of **Heart Disease**, **Diabetes**, and **Parkinson's Disease** based on clinical parameters. Built using Python, Streamlit, and Scikit-learn.

---

## 📌 Problem Statement

Early detection of chronic diseases can save lives and improve quality of life. This project aims to provide a quick, accessible tool to help predict the likelihood of three major diseases using trained ML classifiers.

---

## 🚀 Features

- Predicts:
  - ❤️ Heart Disease
  - 🩸 Diabetes
  - 🧠 Parkinson’s Disease
- Web-based interface built with **Streamlit**
- Clean, responsive UI
- Outputs probability/confidence of prediction

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Backend/ML**: Python, Scikit-learn, Pandas
- **Models Used**: Logistic Regression, SVM, Random Forest (disease-specific)

---

## 🧬 Input Parameters

Each prediction model accepts user input via form fields:
- Heart: age, cholesterol, resting bp, etc.
- Diabetes: glucose, BMI, insulin, etc.
- Parkinson’s: vocal tremor features (MDVP), jitter, etc.

---

## 📊 Model Performance

| Disease       | Model              | Accuracy |
|---------------|--------------------|----------|
| Heart Disease | Logistic Regression| 85%      |
| Diabetes      | SVM                | 88%      |
| Parkinson’s   | Random Forest      | 91%      |

---

## ▶️ How to Run

```bash
git clone https://github.com/yourusername/multiple-disease-predictor
cd multiple-disease-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## 🖼️ Screenshots

> (Add 2–3 screenshots here showing the app UI + prediction result)

---

## 🧠 Key Learning

- Importance of feature scaling for medical data
- Different ML algorithms perform better for different diseases
- Deployment with Streamlit is fast and user-friendly

---

## 🙋‍♂️ Author

**Anurag Singh**  
[LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/yourusername)

---

## 📌 License

This project is licensed under the MIT License.
