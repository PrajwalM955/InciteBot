# 🤖 🥂 🧑‍🤝‍🧑 InciteBot — Smart Conversational AI

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-v1.24.1-orange.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Code Quality](https://img.shields.io/badge/code%20quality-passing-brightgreen.svg)]()

An interactive AI chatbot built with Streamlit and Python featuring adaptive personalities, sentiment-aware replies, and a clean modern interface.

---

## 📋 Key Features

- 👥 **Multiple Personas** — Select between Amora (female) or Phillip (male).  
- 🎭 **Flexible Personality Modes** — Playful, Formal, or Sarcastic.  
- 🔍 **Sentiment-Aware Responses** — Bot tailors replies based on your mood.  
- 👍 **Emoji Reactions** — React directly to chatbot messages with visible counts.  
- 🖼️ **Clean UI** — Well-designed chat bubbles, avatars, and typing indicators.  
- 🎉 **Age-Based Personalization** — Chat experience customized by your age.

---

## 💡 Moral Motivation Behind InciteBot

InciteBot was built with the vision of being more than just a chatbot. Its purpose is to act as a compassionate, adaptive conversational partner that:

- Understands user emotions through sentiment analysis  
- Adjusts tone & personality for personalized engagement  
- Encourages positive, expressive interactions with emojis  
- Supports emotional well-being by fostering empathy in conversations

Ultimately, InciteBot represents a step toward humane, emotionally intelligent AI, designed to support, entertain, and engage users in an ethical and respectful way.

---

## 🖼️ Demo

Here's a quick look at InciteBot in action (replace with actual screenshots/GIFs):

- 🔹 Chat Interface  
- 🔹 Emoji Reactions  
- 🔹 Persona Selection  

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8+  
- pip package manager

### Steps

git clone https://github.com/PrajwalM955/InciteBot.git
cd InciteBot

text

(Optional) Create a virtual environment:

python -m venv .venv

text

Activate it:

- **Windows:**  
  `.venv\Scripts\activate`  
- **macOS/Linux:**  
  `source .venv/bin/activate`

Install dependencies:

pip install -r requirements.txt
python -m textblob.download_corpora

text

---

## 🚀 Running the App

streamlit run app.py

text

Then open `http://localhost:8501` in your browser.

---

## 📂 Project Structure

| File              | Description                              |
|-------------------|------------------------------------------|
| `app.py`          | Streamlit app — UI & chat logic           |
| `chatbot.py`      | Chatbot response generation & sentiment analysis |
| `requirements.txt`| Python dependencies list                   |

---

## 🤝 Contributing

Contributions are welcome!  

1. Fork this repository.  
2. Create a feature branch.  
3. Submit a pull request.  
4. Or open an issue for bug reports & feature requests.

---

## 📜 License

This project is licensed under the MIT License.

---

## 📬 Contact

**Maintainer:** Prajwal Murthy  
For questions, open an issue on GitHub.

---

InciteBot blends AI, sentiment analysis, and creative personas into a meaningful chatbot experience aiming to make digital communication more human.
