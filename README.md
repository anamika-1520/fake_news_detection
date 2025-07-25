# 📰 Fake News Detection Using Multinomial Naive Bayes and Streamlit

## 🚀 Project Overview

This project detects whether a given news article is **fake or real** using **Natural Language Processing (NLP)** and the **Multinomial Naive Bayes algorithm**. A user-friendly **Streamlit app** is provided for real-time predictions.

---

## 📌 Key Features

* ✅ Clean and reproducible ML pipeline
* ✅ Text vectorization with TF-IDF
* ✅ Multinomial Naive Bayes classifier
* ✅ Streamlit app for live predictions
* ✅ Lightweight and fast model

---

## 📂 Project Structure

```
fake_news_detection/
├── streamlit_app.py           # Streamlit web app
├── model.pkl                  # Trained Naive Bayes model
├── vectorizer.pkl             # Saved TfidfVectorizer
├── utils.py                   # Preprocessing functions
├── news.csv                   # Dataset with labeled news
├── requirements.txt           # Python dependencies
└── README.md                  # Project description
```

---

## 📊 Dataset

Using a dataset with news labeled as FAKE or REAL. Example:

* **text**: full article
* **label**: FAKE (1) or REAL (0)

Dataset source (optional): [Kaggle - Fake News Dataset](<img width="1917" height="976" alt="image" src="https://github.com/user-attachments/assets/83593e49-5f9e-4cd3-82c0-e2b00ddafe7b" />
)

---

## 🔍 Model Details

* **Classifier**: Multinomial Naive Bayes (from `sklearn.naive_bayes`)
* **Text Vectorizer**: `TfidfVectorizer`
* **Pipeline**:

  * Clean and tokenize text
  * Transform to TF-IDF features
  * Predict using Naive Bayes model

---

## 📐 How It Works

1. Load and preprocess text
2. Vectorize with TF-IDF
3. Predict using saved model
4. Show result in Streamlit app

---

## 🖼️ Streamlit App Demo

> Paste news content and check if it's FAKE or REAL in real-time.

[Demo Screenshot](<C:\Users\wwwan\OneDrive\Pictures\Screenshots\Screenshot 2025-07-25 191125.png />)

---

## 💪 Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/fake_news_detection.git
cd fake_news_detection
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Sample Inputs

* ✅ "NASA launches new satellite to explore outer space." ➔ REAL
* ❌ "PM arrested in scam worth 300 crores, no proof yet." ➔ FAKE

---

## 🤔 Future Enhancements

* Integrate deep learning (LSTM, BERT)
* Show top keywords using SHAP or LIME
* Deploy to Streamlit Cloud or Hugging Face Spaces

---

## 📃 requirements.txt

```
streamlit
pandas
scikit-learn
nltk
joblib
```

---

## 🌟 Author

**Anamika**
GitHub: [@anamika-1520](https://github.com/anamika-1520)

---

## 📄 License

MIT License - free to use and modify.
