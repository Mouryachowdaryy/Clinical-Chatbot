🩺 Clinical Assistant Chatbot (Streamlit + Gemini AI)

A real-time, AI-powered medical chatbot built using **Streamlit** and **Google Gemini 1.5 Flash**. This chatbot provides helpful responses to health-related questions, but it's **not a substitute for professional medical advice**.

🚀 Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/your-username/clinical-chatbot.git
cd clinical-chatbot
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set your Gemini API key**

Open `app.py` and replace the value of `genai.configure(api_key="...")` with your actual Gemini API key.

4. **Run the app**

```bash
streamlit run app.py
```

5. **Ask questions**

The chatbot UI will open in your browser. Start chatting by asking health-related questions.

🎯 Features

* 🤖 Powered by **Google Gemini 1.5 Flash**
* 🩺 Tailored for **medical and clinical conversations**
* 💬 Supports full **chat history with persistent state**
* 🎨 Custom UI theme via `config.toml`
* 🧠 Smart responses to health-related prompts
* ⚠️ Displays disclaimers for medical liability

🛠️ How It Works

1. `streamlit` serves the chat interface.
2. User inputs are handled via `st.chat_input`.
3. Gemini AI receives queries using `google-generativeai`.
4. Responses are streamed back to the interface in real-time.
5. Conversation state is preserved across turns using `st.session_state`.

📂 Repository Structure

```bash
clinical-chatbot/
├── app.py              ← Main Streamlit application with Gemini API
├── requirements.txt    ← Python package dependencies
├── config.toml         ← Theme customization for Streamlit
└── README.md           ← This documentation
```

🔐 API Key Setup

You’ll need a Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey) or [Google Cloud Console](https://console.cloud.google.com/).

Then edit:

```python
genai.configure(api_key="YOUR_API_KEY")
```
