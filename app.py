import streamlit as st
from datetime import datetime
from chatbot import get_bot_response
import time

st.set_page_config(page_title="InciteBot Chat Interface", page_icon="🤖")

# Custom CSS including neon blue glow for submit and clear buttons
st.markdown("""
    <style>
    /* General chat bubble styling */
    .chat-container {
        max-width: 700px;
        margin: auto;
    }
    .user-message {
        background-color: #dcf8c6;
        padding: 12px 20px;
        border-radius: 20px 20px 0 20px;
        margin: 8px 0;
        max-width: 80%;
        font-size: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        align-self: flex-end;
        color: #202124;
    }
    .bot-message {
        background-color: #e1e4f2;
        padding: 12px 20px;
        border-radius: 20px 20px 20px 0;
        margin: 8px 0;
        max-width: 80%;
        font-size: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        align-self: flex-start;
        color: #202124;
    }
    .message-row {
        display: flex;
        align-items: center;
        max-width: 700px;
        margin: 0 auto;
    }
    .avatar {
        font-size: 28px;
        margin-right: 10px;
        user-select: none;
    }
    /* Emoji reaction blocks styling */
    .emoji-reaction-container {
        display: inline-flex;
        border: 1px solid #ccc;
        border-radius: 12px;
        overflow: hidden;
        user-select: none;
        margin-left: 44px;
        margin-top: -10px;
        vertical-align: middle;
    }
    .emoji-reaction-block {
        background-color: #fff;
        padding: 4px 10px;
        font-size: 18px;
        cursor: pointer;
        border-right: 1px solid #ccc;
        transition: background-color 0.2s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        user-select: none;
        outline: none;
        border: none;
    }
    .emoji-reaction-block:last-child {
        border-right: none;
    }
    .emoji-reaction-block:hover {
        background-color: #f0f0f0;
    }
    .reaction-count-badge {
        background-color: #ffd700;
        border-radius: 9999px;
        padding: 2px 6px;
        font-size: 12px;
        user-select: none;
    }
    .stButton > button {
        margin: 0 !important;
        padding: 4px 10px !important;
        font-size: 18px !important;
        min-width: unset !important;
        width: auto !important;
        border-radius: 0 !important;
        border: none !important;
        display: flex !important;
        align-items: center !important;
        gap: 6px !important;
    }
    .stButton > button:first-child {
        border-top-left-radius: 12px !important;
        border-bottom-left-radius: 12px !important;
        border: 1px solid #ccc !important;
        border-right: none !important;
        background-color: #fff !important;
    }
    .stButton > button:last-child {
        border-top-right-radius: 12px !important;
        border-bottom-right-radius: 12px !important;
        border: 1px solid #ccc !important;
        background-color: #fff !important;
    }

    /* Neon Blue Glow Styling for Submit Age and Clear Chat buttons */
    button#submit_age > button, button#clear_chat > button {
        background-color: #1e90ff !important; /* Neon Blue */
        color: white !important;              /* White text */
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        box-shadow: 0px 0px 10px rgba(30, 144, 255, 0.7) !important; /* Glow */
        border: none !important;
        transition: background-color 0.3s ease;
    }
    button#submit_age > button:hover, button#clear_chat > button:hover {
        background-color: #1a78d8 !important; /* Darker neon blue on hover */
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("InciteBot — Your Flirty Chatbot")

# Initialize session state variables
if "age" not in st.session_state:
    st.session_state.age = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "reactions" not in st.session_state:
    st.session_state.reactions = {}
if "personality" not in st.session_state:
    st.session_state.personality = "Playful"
if "bot_name" not in st.session_state:
    st.session_state.bot_name = "Amora"

def add_reaction(msg_idx, emoji):
    if msg_idx not in st.session_state.reactions:
        st.session_state.reactions[msg_idx] = {}
    st.session_state.reactions[msg_idx][emoji] = st.session_state.reactions[msg_idx].get(emoji, 0) + 1

bot_choice = st.selectbox("Choose your chat partner:", ["Amora (Female)", "Phillip (Male)"])
st.session_state.bot_name = "Amora" if bot_choice.startswith("Amora") else "Phillip"

if st.session_state.age is None:
    age = st.number_input("Please enter your age:", min_value=1, max_value=120)
    if st.button("Submit Age", key="submit_age"):
        st.session_state.age = age
        st.rerun()
else:
    st.selectbox("Choose Chatbot Personality", ["Playful", "Formal", "Sarcastic"], key="personality")

    for idx, msg in enumerate(st.session_state.messages):
        author = "You" if msg["role"] == "user" else st.session_state.bot_name
        avatar = "👩" if st.session_state.bot_name == "Amora" else "👨"
        msg_class = "user-message" if msg["role"] == "user" else "bot-message"

        st.markdown(f"""
            <div class="message-row" style="justify-content:{'flex-end' if msg['role']=='user' else 'flex-start'};">
                <div class="avatar">{avatar if msg['role']=='assistant' else '🧑'}</div>
                <div class="{msg_class}">
                    <b>{author}</b>: {msg["content"]}
                </div>
            </div>
        """, unsafe_allow_html=True)

        if msg["role"] == "assistant":
            emojis = ["❤️", "🔥", "😂", "😍", "👏"]
            cols = st.columns(len(emojis))
            for i, emoji in enumerate(emojis):
                btn_key = f"react_{idx}_{emoji}"
                count = st.session_state.reactions.get(idx, {}).get(emoji, 0)
                label = f"{emoji} {count if count > 0 else ''}"
                if cols[i].button(label, key=btn_key, help=f"React with {emoji}"):
                    add_reaction(idx, emoji)
                    st.rerun()

    if st.button("Clear Chat", key="clear_chat"):
        st.session_state.messages = []
        st.session_state.reactions = {}
        st.rerun()

    prompt = st.chat_input(f"Message {st.session_state.bot_name}...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt, "time": datetime.now()})
        st.rerun()

    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        avatar = "👩" if st.session_state.bot_name == "Amora" else "👨"
        with st.chat_message("assistant", avatar=avatar):
            typing_placeholder = st.empty()
            typing_placeholder.markdown(f"_**{st.session_state.bot_name}** is typing..._")
            time.sleep(2)

            context = st.session_state.messages[-6:]
            reply = get_bot_response(
                st.session_state.messages[-1]["content"],
                age=st.session_state.age,
                conversation_history=context,
                personality=st.session_state.personality,
                bot_name=st.session_state.bot_name,
            )
            typing_placeholder.markdown(f"**{st.session_state.bot_name}**: {reply}")
            st.session_state.messages.append({"role": "assistant", "content": reply, "time": datetime.now()})
            st.rerun()
