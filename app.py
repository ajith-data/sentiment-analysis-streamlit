import streamlit as st
import pandas as pd
import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="📊",
    layout="wide"
)

# ---------------- SAFE UI THEME ----------------
st.markdown("""
<style>
.stApp {
    background-color: #f8fafc;
    color: #0f172a;
}

h1, h2, h3 {
    color: #0f172a;
}

.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    font-weight: 600;
}
.stButton>button:hover {
    background-color: #1d4ed8;
}

textarea, input {
    background-color: white !important;
    color: #0f172a !important;
}

[data-testid="stFileUploader"] {
    background-color: white;
    border-radius: 8px;
    padding: 10px;
}

[data-testid="stDataFrame"] {
    background-color: white;
}

[data-testid="stAlert"] {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SENTIMENT SETUP ----------------
sia = SentimentIntensityAnalyzer()

# Session state for recent reviews
if "recent_reviews" not in st.session_state:
    st.session_state.recent_reviews = []

# Session state for OVERALL COUNTS
if "overall_counts" not in st.session_state:
    st.session_state.overall_counts = {
        "Positive": 0,
        "Negative": 0,
        "Neutral": 0
    }

# ---------------- FUNCTIONS ----------------
def analyze_sentiment(text):
    score = sia.polarity_scores(text)
    if score["compound"] >= 0.05:
        return "Positive"
    elif score["compound"] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def read_file(uploaded_file):
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        return df.iloc[:, 0].dropna().tolist()

    elif uploaded_file.name.endswith(".json"):
        data = json.load(uploaded_file)
        if isinstance(data, list):
            return [list(d.values())[0] for d in data]
        return list(data.values())

    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8").splitlines()

    return []

# ---------------- UI ----------------
st.title("📊 AI Sentiment Analysis Dashboard")
st.markdown("Analyze **Text, CSV, JSON reviews** and track **overall sentiment points**")

col1, col2 = st.columns([2, 1])

# ---------- INPUT ----------
with col1:
    st.subheader("🔹 Upload File or Enter Text")

    uploaded_file = st.file_uploader(
        "Upload CSV / JSON / TXT file",
        type=["csv", "json", "txt"]
    )

    manual_text = st.text_area(
        "Or enter review text manually",
        height=140,
        placeholder="Enter a review here..."
    )

    analyze_btn = st.button("Analyze Sentiment 🚀")

# ---------- RECENT REVIEWS ----------
with col2:
    st.subheader("🕒 Recent Reviews")
    if st.session_state.recent_reviews:
        for r in st.session_state.recent_reviews[:5]:
            st.write("•", r[:80] + "...")
    else:
        st.info("No recent reviews yet")

# ---------------- PROCESS ----------------
if analyze_btn:
    reviews = []

    if uploaded_file:
        reviews = read_file(uploaded_file)
    elif manual_text.strip():
        reviews = [manual_text]

    if not reviews:
        st.warning("Please upload a file or enter text")
    else:
        current_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
        results = []

        for review in reviews:
            sentiment = analyze_sentiment(review)
            results.append((review, sentiment))

            # current counts
            current_counts[sentiment] += 1

            # overall counts
            st.session_state.overall_counts[sentiment] += 1

            st.session_state.recent_reviews.insert(0, review)

        # ---------- RESULTS ----------
        st.subheader("📋 Sentiment Results (Current Input)")
        df_results = pd.DataFrame(results, columns=["Review", "Sentiment"])
        st.dataframe(df_results, use_container_width=True)

        # ---------- CURRENT BAR CHART ----------
        st.subheader("📈 Current Sentiment Distribution")
        current_df = pd.DataFrame.from_dict(
            current_counts, orient="index", columns=["Count"]
        )
        st.bar_chart(current_df)

        # ---------- OVERALL BAR CHART ----------
        st.subheader("📊 Overall Sentiment Distribution")
        overall_df = pd.DataFrame.from_dict(
            st.session_state.overall_counts,
            orient="index",
            columns=["Total Count"]
        )
        st.bar_chart(overall_df)

        # ---------- SUMMARY ----------
        st.success(
            f"Current → Positive: {current_counts['Positive']} | "
            f"Neutral: {current_counts['Neutral']} | "
            f"Negative: {current_counts['Negative']}"
        )

        st.info(
            f"Overall → Positive: {st.session_state.overall_counts['Positive']} | "
            f"Neutral: {st.session_state.overall_counts['Neutral']} | "
            f"Negative: {st.session_state.overall_counts['Negative']}"
        )
