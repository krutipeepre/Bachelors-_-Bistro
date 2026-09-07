# 🍳 Bachelors' Bistro - AI Chef Chatbot

A sleek, Gen-Z friendly AI-powered recipe assistant built specifically for hostel students and bachelors. Tell it what random ingredients you have left in your fridge, and it will instantly cook up quick, practical, and delicious meal ideas using basic pantry staples!

🔗 **Live App:** [Bachelors' Bistro Live](https://bachelors-bistro.streamlit.app/)

## ✨ Features

- **Fridge-to-Table Recipes:** Input whatever ingredients you have, and get 2-3 tailored recipes with cooking times and step-by-step instructions.
- **Custom Tech-Blue UI:** Strictly styled with a clean Blue, Grey, Black, and White dark mode palette.
- **Modern Chat Interface:** Clean vector-style avatars and a custom gradient border chat input without annoying default highlights.
- **Groq API Powered:** Utilizes high-speed LLM processing via the Groq API for rapid responses.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI & Hosting Framework)
- **Groq API** (LLM inference)

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/krutipeepre/Bachelors-Bistro.git](https://github.com/krutipeepre/Bachelors-Bistro.git)
   cd Bachelors-Bistro

## Install dependencies:

Bash
pip install -r requirements.txt

## Set up your Groq API Key:
Create a .streamlit/secrets.toml file in your project root directory and add your key:

Ini, TOML
GROQ_API_KEY = "your_actual_groq_api_key_here"

## Run the Streamlit app:

Bash
streamlit run app.py

# ☁️ Deployment on Streamlit Cloud

1. Push this repository to your GitHub.
2. Go to Streamlit Community Cloud and click Create app.
3. Select your repository, branch (main), and main file (app.py).
4. In your app settings on Streamlit Cloud, go to Secrets and add:

    Ini, TOML
    GROQ_API_KEY = "your_actual_groq_api_key_here"

5. Hit Deploy and enjoy!
