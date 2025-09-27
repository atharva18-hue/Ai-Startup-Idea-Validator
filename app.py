# app.py - Polished Full Dark Theme AI Startup Idea Validator
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import analyze_idea
from competitor_fetcher import fetch_competitors
from sentiment_model import get_sentiment

# --- Page Config ---
st.set_page_config(
    page_title="AI Startup Idea Validator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Dark Theme CSS ---
st.markdown("""
<style>
/* Full dark background */
.stApp, .main .block-container {
    background-color: #0f172a;
    color: #f0f0f0;
    padding: 0px 30px 30px 30px;
}

/* Sidebar */
.css-1d391kg {
    background-color: #111827;
    color: #f0f0f0;
}

/* Card style */
.swot-card {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(0,0,0,0.6);
    margin-bottom: 12px;
    transition: transform 0.2s;
}
.swot-card:hover {
    transform: translateY(-3px);
}

/* Links */
a {color: #38bdf8; text-decoration:none; font-weight:600;}
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("💡 AI Startup Idea Validator")
st.sidebar.subheader("Enter or select a startup idea")

examples = [
    "AI Mental Health Companion",
    "Personalized Nutrition Planner",
    "Smart Waste Management",
    "AI Tutor for Programming",
    "Virtual AI Travel Guide"
]

selected_example = st.sidebar.selectbox("Select Example Idea", [""] + examples)
idea_input = st.sidebar.text_area("Or type your idea here:", height=120, value=selected_example)
analyze_button = st.sidebar.button("🚀 Analyze Idea")

# --- Main Title ---
st.title("🚀 AI Startup Idea Validator")
st.subheader("LangChain + BERT Demo")

if analyze_button and idea_input.strip() != "":
    st.markdown("## 🔍 Analysis Results")

    # --- Analyze ---
    swot = analyze_idea(idea_input)
    sentiment = get_sentiment(idea_input)
    competitors = fetch_competitors(idea_input)

    # --- SWOT Cards ---
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🟢 Strengths")
        for s in swot['Strengths']:
            st.markdown(f"<div class='swot-card' style='border-left:5px solid #22c55e'>• {s}</div>", unsafe_allow_html=True)
        st.markdown("### 🔴 Weaknesses")
        for w in swot['Weaknesses']:
            st.markdown(f"<div class='swot-card' style='border-left:5px solid #ef4444'>• {w}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("### 🔵 Opportunities")
        for o in swot['Opportunities']:
            st.markdown(f"<div class='swot-card' style='border-left:5px solid #3b82f6'>• {o}</div>", unsafe_allow_html=True)
        st.markdown("### 🟠 Threats")
        for t in swot['Threats']:
            st.markdown(f"<div class='swot-card' style='border-left:5px solid #f97316'>• {t}</div>", unsafe_allow_html=True)

    # --- Radar Chart ---
    labels = ["Strengths", "Weaknesses", "Opportunities", "Threats"]
    scores = [len(swot['Strengths']), len(swot['Weaknesses']), len(swot['Opportunities']), len(swot['Threats'])]
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    scores += scores[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True), facecolor="#0f172a")
    ax.plot(angles, scores, marker='o', color='#38bdf8', linewidth=3)
    ax.fill(angles, scores, alpha=0.3, color='#38bdf8')
    ax.set_thetagrids(np.degrees(angles[:-1]), labels, color="white")
    ax.set_ylim(0, max(scores)+1)
    ax.tick_params(colors='white')
    st.pyplot(fig)

    # --- Sentiment ---
    st.markdown("### 📝 Sentiment Analysis")
    st.markdown(f"<div class='swot-card' style='border-left:5px solid #facc15'>"
                f"**Sentiment:** {sentiment['sentiment']}  |  **Score:** {sentiment['score']}</div>",
                unsafe_allow_html=True)

    # --- Competitors ---
    st.markdown("### 🏆 Top Competitors")
    for c in competitors:
        st.markdown(
            f"<div class='swot-card'><b>{c['name']}</b><br>Website: <a href='{c['url']}' target='_blank'>{c['url']}</a></div>",
            unsafe_allow_html=True
        )

# --- Footer ---
st.markdown("---")
st.markdown("<center>© 2025 Atharv Chavhan</center>", unsafe_allow_html=True)
