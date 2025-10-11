# <p align="center"> <span style="color:#4CAF50">AI Startup Idea Validator (LangChain + BERT)</span></p>

<p align="center">
  <img src="https://img.shields.io/badge/Frontend-Streamlit-blue?style=flat&logo=streamlit&logoColor=white" alt="Frontend"/>
  <img src="https://img.shields.io/badge/AI-Python%20%26%20LangChain-orange?style=flat&logo=python&logoColor=white" alt="AI Pipeline"/>
  <img src="https://img.shields.io/badge/NLP-BERT-red?style=flat&logo=transformers&logoColor=white" alt="NLP"/>
  <img src="https://img.shields.io/badge/Visualization-Matplotlib-lightblue?style=flat&logo=matplotlib&logoColor=black" alt="Visualization"/>
  <img src="https://img.shields.io/badge/Dependencies-Python%203.11+-yellow?style=flat" alt="Python Version"/>
</p>

---

##  **Project Overview**
The AI Startup Idea Validator is designed to provide instant, AI-powered insights for startup ideas, enabling founders and innovators to assess viability and potential market impact efficiently.

Traditional evaluation methods—manual research, SWOT analysis, market surveys, and sentiment evaluation—are time-consuming, subjective, and prone to inconsistencies. This project automates the process using AI, making it interactive, fast, and highly accurate.

-------------------------------------

## Key Capabilities:

 **Instant SWOT Analysis** – Automatically generates Strengths, Weaknesses, Opportunities, and Threats, giving immediate, actionable insights to guide early-stage decision-making.

 **Sentiment Scoring** – Leverages a BERT-based NLP model to quantify idea positivity or negativity, providing a clear and objective evaluation of user-submitted ideas.

 **Top Competitor Identification** – Uses AI logic to discover relevant competitors, with future integration for live market data, helping innovators benchmark their ideas effectively.

 **Visual Insights** – Presents results in an interactive, user-friendly interface with dynamic cards and radar charts, enabling users to visualize strengths, weaknesses, and opportunities at a glance.

---

##  **Features**
**1️. Full Dark Theme UI**

**.**Modern, stylish, and user-friendly interface.

**.**Hover effects on SWOT and competitor cards.

**.**Consistent dark background for sidebar, main content, and charts.

-----------------------------------------------------------

**2️. Startup Idea Input**

Users can type their own idea or select from pre-defined examples such as:

AI Mental Health Companion

Personalized Nutrition Planner

Smart Waste Management

AI Tutor for Programming

Virtual AI Travel Guide

-------------------------------------------------

**3️. SWOT Analysis**

Dynamic cards for Strengths, Weaknesses, Opportunities, and Threats.

Each category has a colored left border:

Strengths → Green

Weaknesses → Red

Opportunities → Blue

Threats → Orange

-----------------------------------------------

**4️. Sentiment Analysis (BERT)**

Evaluates the positivity or negativity of the idea.

Displays a 0–100 score along with a label (Positive / Neutral / Negative).

Shown inside a card with a visual indicator.

--------------------------------------

**5️. Top Competitors**

Fetches relevant competitors for the AI-based idea (currently using placeholders, future API integration planned).

Displays name and website link on each card.

---------------------------------------------------

**6️. Radar Chart for SWOT**

Interactive polar chart showing the number of points per SWOT category.

Helps users visually compare strengths vs. weaknesses vs. opportunities vs. threats.

-------------------------------------------

**7️. LangChain Pipeline Integration**

Multiple AI steps are executed sequentially in a single chain.

Future enhancements: Market trend analysis, AI-powered recommendations, and investor scoring.

---------------------------------------------------------------------------------

##  **Technology Stack**


| Layer | Tool / Technology |
|-------|-----------------|
| **Frontend / UI** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) |
| **AI Pipeline** | ![LangChain](https://img.shields.io/badge/LangChain-00BFFF?style=flat) |
| **NLP / Sentiment** | ![BERT](https://img.shields.io/badge/BERT-FF6F61?style=flat) / HuggingFace Transformers |
| **Visualization** | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white) |
| **Python Version** | 3.11+ |
| **Other Libraries** | scikit-learn, numpy |

---

###  Explanation of project structure and of Each Component


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

----------------------------------------------
## Project Screenshot

<img width="1403" height="973" alt="Screenshot 2025-10-07 074603" src="https://github.com/user-attachments/assets/958c205c-16e1-45af-9b2b-0bf2fa32e966" />

------------------------------------------
<img width="1917" height="893" alt="Screenshot 2025-10-07 074722" src="https://github.com/user-attachments/assets/add86d71-ee6a-462b-9812-69973ff8af5f" />

-----------------------------------------
<img width="1919" height="963" alt="Screenshot 2025-10-07 074747" src="https://github.com/user-attachments/assets/ead8c60c-a5a4-4588-983b-415bf4e95ac5" />

---------------------------------
<img width="1918" height="960" alt="Screenshot 2025-10-07 074824" src="https://github.com/user-attachments/assets/f0ad3b43-e362-4e6c-9b6e-ce4d8ac2ec2e" />

----------------------------------------
<img width="1918" height="966" alt="Screenshot 2025-10-07 074846" src="https://github.com/user-attachments/assets/f8b0ede9-5e41-47ec-8f5b-1d03c1ab0f46" />

----------------------------------------------
<img width="1919" height="961" alt="Screenshot 2025-10-07 074946" src="https://github.com/user-attachments/assets/6d44acbe-5e39-47f8-ae1d-73ad088118a6" />

-----------------------------------------------------------------
<img width="1919" height="968" alt="Screenshot 2025-10-07 075019" src="https://github.com/user-attachments/assets/2cfd0e96-811a-4aca-a42f-bc1bf92998c3" />

----------------------------------------------------------


##  Installation & Setup

**Clone repository**

git clone <repo-link>
cd ai_startup_validator_langchain/ai_startup_validator_langchain

-----------------------------------------------------------------
**Create virtual environment (recommended)**

python -m venv venv
.\venv\Scripts\activate    # Windows
source venv/bin/activate   # Linux / Mac

---------------------------------------------------------------------------
**Install dependencies**

pip install -r requirements.txt

------------------------------------------------------------------------------------

**Run the app**
streamlit run app.py

------------------------------------------------------------------

**Open in browser**

Local URL: http://localhost:8501

Network URL (if LAN): http://<your-ip>:8501

----------------------------------------------------------------

##  Usage

Select a predefined example idea or type your own in the sidebar.

Click “ Analyze Idea”.

----------------------------------------------------------------

## View results:

SWOT analysis cards

Radar chart for comparison

Sentiment score

Top competitors

--------------------------------------------------

##  Future Improvements

Real-time competitor fetching using SerpAPI / Google API

Integration with LangChain agents for idea scoring & suggestions

Market trend analytics & investor suitability score

Multi-language support for non-English ideas

-------------------------------------------
##  Author

Atharva Chavhan

GitHub: https://github.com/atharva18-hue

LinkedIn: https://www.linkedin.com/in/atharva-chavhan-b5742b259/

Email: atharvachavhan18@gmail.com

--------------------------------------

##  License

© 2025 Atharv Chavhan. All rights reserved.

----------------------------------------------------
