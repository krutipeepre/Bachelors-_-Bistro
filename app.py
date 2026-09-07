import streamlit as st
from groq import Groq

# Configure standard Streamlit page settings
st.set_page_config(
    page_title="Bachelors' Bistro Chatbot", page_icon="🍳", layout="centered"
)

# Custom CSS targeting Streamlit's exact chat input element to remove red borders completely
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    h1, h2, h3 {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }
    p {
        color: #b0b8c4;
    }
    
    /* Forcefully override Streamlit chat input border and focus outline */
    div[data-testid="stChatInput"] {
        border: 2px solid #3b82f6 !important;
        border-radius: 12px !important;
        background-color: #161b22 !important;
    }
    div[data-testid="stChatInput"]:focus-within {
        border: 2px solid #60a5fa !important;
        box-shadow: 0 0 10px rgba(59, 130, 246, 0.4) !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Main Dashboard Header without the omelette emoji
st.title("Bachelors' Bistro - AI Chef Chatbot")
st.markdown(
    "*Tell me what's left in your fridge, and I'll cook up some recipes for"
    " you!*"
)
st.markdown("---")

# Securely fetch API key from Streamlit Secrets (Safe for Public Repositories)
API_KEY = st.secrets.get("GROQ_API_KEY", "YOUR_API_KEY")

if not API_KEY or API_KEY == "YOUR_API_KEY":
  st.error(
      "⚠️ Groq API key is missing! Please configure it in your Streamlit Cloud"
      " Secrets."
  )
else:
  client = Groq(api_key=API_KEY)

  # Initialize chat history in Streamlit session state if not already present
  if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": (
            "Hey! I'm your hostel chef assistant. What items do you have in"
            " your fridge right now? (e.g., 'bread, cheese, eggs and a tomato')"
        ),
    }]

  # Display prior chat messages using clean vector-style emojis for avatars
  for message in st.session_state.messages:
    avatar_icon = "🧑‍🍳" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar_icon):
      st.markdown(message["content"])

  # Get user input from the chat bar at the bottom
  if user_input := st.chat_input(
      "Type what's in your fridge (e.g., leftover rice, onion, butter)..."
  ):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="👤"):
      st.markdown(user_input)

    with st.chat_message("assistant", avatar="🧑‍🍳"):
      with st.spinner("Chef AI is thinking of recipes..."):
        try:
          system_prompt = (
              "You are an expert, friendly hostel chef for a platform called"
              " 'Bachelors' Bistro'. The user will tell you what ingredients"
              " they have in their fridge. Give them 2 or 3 quick, practical,"
              " and tasty recipes they can make using those ingredients (plus"
              " basic pantry items like salt, water, oil). Keep the tone fun,"
              " casual, and Gen Z friendly. Format clearly with Recipe Name,"
              " Cooking Time, and Step-by-step instructions."
          )

          messages_payload = [{"role": "system", "content": system_prompt}] + [
              {"role": m["role"], "content": m["content"]}
              for m in st.session_state.messages
          ]

          chat_completion = client.chat.completions.create(
              messages=messages_payload, model="openai/gpt-oss-20b"
          )

          bot_response = chat_completion.choices[0].message.content
          st.markdown(bot_response)

          st.session_state.messages.append(
              {"role": "assistant", "content": bot_response}
          )

        except Exception as e:
          st.error(f"❌ An error occurred: {e}")
