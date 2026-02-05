📊 AI Sentiment Analysis App (Streamlit)

Project Link(https://sentiment-analysis-app-jaszyp52ffl3gjffsyhrun.streamlit.app/)

An interactive Sentiment Analysis web application built using Python, Streamlit, and NLTK (VADER).
The app analyzes reviews from Text, CSV, JSON files and classifies them as Positive, Neutral, or Negative, with visual insights.

🚀 Features

📁 Upload CSV / JSON / TXT files

✍️ Manual text input support

😊 Sentiment classification:

Positive

Neutral

Negative

📊 Bar charts for:

Current input sentiment

Overall (cumulative) sentiment

🕒 Recent reviews history

🎨 Clean and user-friendly UI

⚡ Fast and lightweight

🛠️ Tech Stack

Python

Streamlit

NLTK (VADER Sentiment Analyzer)

Pandas

HTML/CSS (Streamlit custom styling)

📂 Project Structure
sentiment-analysis-streamlit/
│
├── app.py
├── requirements.txt
├── README.md
│
└── sample_data/
    ├── positive_reviews.csv
    ├── negative_reviews.txt
    └── neutral_reviews.json

📥 Input Formats
✅ Text

Single review entered manually

✅ CSV
review
The product quality is excellent
Delivery was late and disappointing

✅ JSON
[
  {"review": "Amazing experience"},
  {"review": "The service was average"}
]

✅ TXT
The app works well
Customer support is slow

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/sentiment-analysis-streamlit.git
cd sentiment-analysis-streamlit

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Run the App
streamlit run app.py

📊 Output

Sentiment label for each review

Current sentiment distribution (bar chart)

Overall sentiment distribution across sessions

Recent review history

🧠 Sentiment Logic

Uses VADER sentiment scores:

compound ≥ 0.05 → Positive

compound ≤ -0.05 → Negative

Otherwise → Neutral

🔮 Future Enhancements

🔁 Reset overall sentiment stats

📈 Percentage-based charts

📥 Download analyzed results

🤖 Transformer-based sentiment models

🌐 Deploy on Streamlit Cloud

👨‍💻 Author

Ajith
Aspiring Data Analyst | Python | Streamlit | NLP
📍 India
