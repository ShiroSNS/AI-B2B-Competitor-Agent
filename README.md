# 🕵️‍♂️ B2B Competitor Intelligence Agent

An automated market research pipeline that extracts unstructured text from any B2B startup website and uses **Gemini 3.5 Flash** to transform it into a structured competitive intelligence dashboard.

## 🎯 The Problem It Solves
Market research is traditionally a manual, time-consuming process. This tool automates the extraction of core business metrics—specifically the **Value Proposition**, **Target Audience**, and **Pricing Strategy**—allowing sales and product teams to instantly analyze competitors without reading through marketing fluff.

## 🛠️ Tech Stack
* **Frontend UI:** Streamlit
* **Data Orchestration & AI:** Google Gemini 3.5 Flash API, JSON parsing
* **Web Scraping Pipeline:** Python, Requests, BeautifulSoup4

## 🏗️ System Architecture
The application is built using a modular, three-part architecture:
1. `scraper.py`: A custom crawler that disguises itself as a standard browser to bypass basic blocks, extracts the DOM, and sanitizes raw HTML into readable text limits.
2. `agent.py`: The AI orchestrator. It passes the raw data to the Gemini 3.5 Flash model with strict system prompts to force the output into a cleanly formatted, programmatic JSON object.
3. `app.py`: The user-facing Streamlit application that handles API authentication, triggers the data pipeline, and renders the extracted JSON into clean UI metric cards.

## 🚀 How to Run Locally

**1. Clone the repository**
`git clone https://github.com/YOUR_GITHUB_USERNAME/AI-B2B-Competitor-Agent.git`
`cd AI-B2B-Competitor-Agent`

**2. Install dependencies**
`pip install streamlit google-genai beautifulsoup4 requests`

**3. Launch the application**
`streamlit run app.py`

**4. Authenticate**
* Obtain a Gemini API Key from Google AI Studio.
* Paste the key securely into the Streamlit sidebar (keys are never hardcoded or saved).

## 🔮 Future Roadmap
* Implement automated PDF/CSV report exporting.
* Add multi-URL batch processing to compare several competitors at once.
