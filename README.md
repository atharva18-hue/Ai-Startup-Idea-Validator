# <p align="center">🚀 <span style="color:#4CAF50">AI Startup Idea Validator (LangChain + BERT)</span></p>

<p align="center">
  <img src="https://img.shields.io/badge/Frontend-Streamlit-blue?style=flat&logo=streamlit&logoColor=white" alt="Frontend"/>
  <img src="https://img.shields.io/badge/AI-Python%20%26%20LangChain-orange?style=flat&logo=python&logoColor=white" alt="AI Pipeline"/>
  <img src="https://img.shields.io/badge/NLP-BERT-red?style=flat&logo=transformers&logoColor=white" alt="NLP"/>
  <img src="https://img.shields.io/badge/Visualization-Matplotlib-lightblue?style=flat&logo=matplotlib&logoColor=black" alt="Visualization"/>
  <img src="https://img.shields.io/badge/Dependencies-Python%203.11+-yellow?style=flat" alt="Python Version"/>
</p>

---

## 🔹 **Project Overview**
The AI Startup Idea Validator is designed to provide instant, AI-powered insights for startup ideas, enabling founders and innovators to assess viability and potential market impact efficiently.

Traditional evaluation methods—manual research, SWOT analysis, market surveys, and sentiment evaluation—are time-consuming, subjective, and prone to inconsistencies. This project automates the process using AI, making it interactive, fast, and highly accurate.

-------------------------------------

## Key Capabilities:

🚀 **Instant SWOT Analysis** – Automatically generates Strengths, Weaknesses, Opportunities, and Threats, giving immediate, actionable insights to guide early-stage decision-making.

📊 **Sentiment Scoring** – Leverages a BERT-based NLP model to quantify idea positivity or negativity, providing a clear and objective evaluation of user-submitted ideas.

🏆 **Top Competitor Identification** – Uses AI logic to discover relevant competitors, with future integration for live market data, helping innovators benchmark their ideas effectively.

🎨 **Visual Insights** – Presents results in an interactive, user-friendly interface with dynamic cards and radar charts, enabling users to visualize strengths, weaknesses, and opportunities at a glance.

---

## ⚡ **Features**

### 1️⃣ Full Dark Theme UI
- Modern, stylish aur **user-friendly interface**.  
- Hover effects on SWOT / competitor cards.  
- Consistent dark background for sidebar, main content, aur charts
- ------------------------------------------------------------------------------------------------------------------------------

### 2️⃣ Startup Idea Input
- Users apna idea type kar sakte hai ya **pre-defined examples** select kar sakte hai:  
  - AI Mental Health Companion  
  - Personalized Nutrition Planner  
  - Smart Waste Management  
  - AI Tutor for Programming  
  - Virtual AI Travel Guide
  - -----------------------------------------------------------------------------------------

### 3️⃣ SWOT Analysis
- Strengths, Weaknesses, Opportunities, Threats ke liye **dynamic cards**.  
- Har category ke liye **colored left border**:  
  - 🟢 Strengths → Green  
  - 🔴 Weaknesses → Red  
  - 🔵 Opportunities → Blue  
  - 🟠 Threats → Orange
  - ----------------------------------------------------------------------------------------

### 4️⃣ Sentiment Analysis (BERT)
- Idea ki **positivity / negativity** score karta hai.  
- Score **0-100** aur label (Positive / Neutral / Negative) show hota hai.  
- Card me **visual indicator** ke sath display.
---------------------------------------------------------------------------------------------------------------------
### 5️⃣ Top Competitors
- AI-based idea ke liye **relevant competitors fetch** karta hai (placeholder / future API integration).  
- Card me **name + website link** show hota hai.
------------------------------------------------------------------------------------
### 6️⃣ Radar Chart for SWOT
- Interactive polar chart showing **number of points per SWOT category**.  
- Helps user visually compare strengths vs weaknesses vs opportunities vs threats.
- -----------------------------------------------------------------------------------------

### 7️⃣ LangChain Pipeline Integration
- Multiple AI steps ek chain me run hote hai.  
- Future enhancements: **Market trend analysis**, AI-powered **recommendations**, **investor scoring**.

---------------------------------------------------------------------------------

## 🛠 **Technology Stack**

| Layer | Tool / Technology |
|-------|-----------------|
| **Frontend / UI** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) |
| **AI Pipeline** | ![LangChain](https://img.shields.io/badge/LangChain-00BFFF?style=flat) |
| **NLP / Sentiment** | ![BERT](https://img.shields.io/badge/BERT-FF6F61?style=flat) / HuggingFace Transformers |
| **Visualization** | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white) |
| **Python Version** | 3.11+ |
| **Other Libraries** | scikit-learn, numpy |

---

### ✅ Explanation of project structure and of Each Component

| File / Folder             | Description |
|---------------------------|-------------|
| **app.py**                | Entry point of the application. Handles Streamlit UI, user input, and renders output cards, charts, and sentiment. |
| **utils.py**              | Contains core logic for SWOT analysis. Functions take user input and generate Strengths, Weaknesses, Opportunities, and Threats dynamically. |
| **competitor_fetcher.py** | Placeholder module to fetch competitors. Currently uses dummy data. Can be upgraded to real API integration in future. |
| **sentiment_model.py**    | Uses BERT (HuggingFace Transformers) for sentiment analysis. Returns positivity score and label. |
| **requirements.txt**      | Lists all Python dependencies needed to run the project. Easy setup in virtual environment. |
| **README.md**             | Detailed project documentation including features, setup, usage, and future improvements. |
| **.gitignore**            | Ensures unwanted files like cache, compiled Python files, and venv are ignored by Git. |
| **venv/**                 | Virtual environment folder. Contains all installed libraries and Python interpreter. Should not be pushed to Git. |
