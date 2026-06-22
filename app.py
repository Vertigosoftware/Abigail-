import streamlit as st
import base64
import time
import requests

# 1. Setup page configuration
st.set_page_config(page_title="Abigail's Terminal", page_icon="⚡", layout="centered")

# Telegram Notification Function
TELEGRAM_BOT_TOKEN = "7336712396:AAFx_Yy5QG9_A393N9Sj3Xy6SJyV5QYyA39"  # Restored from your original config
TELEGRAM_CHAT_ID = "6193791234"

def send_notification(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
        requests.post(url, json=payload)
    except Exception:
        pass

# Music URL setup
MUSIC_URL = "https://raw.githubusercontent.com/Vertigosoftware/Abigail-/main/33019.mp3"

# 2. Keep background music playing across all steps globally
if 'audio_played' not in st.session_state:
    st.markdown(f"""
        <iframe src="{MUSIC_URL}" allow="autoplay" style="display:none;"></iframe>
        <audio autoplay loop hidden>
            <source src="{MUSIC_URL}" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)
    st.session_state.audio_played = True

# 3. Custom CSS for the cyber-noir glowing aesthetic
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0c10;
        color: #c5c6c7;
        font-family: 'Courier New', Courier, monospace;
    }
    .cyber-header {
        color: #66fcf1 !important;
        text-shadow: 0 0 10px #66fcf1, 0 0 20px #66fcf1;
        text-align: center;
        font-size: 32px;
    }
    .cyber-text {
        color: #c5c6c7;
        font-size: 16px;
        text-align: center;
        line-height: 1.6;
    }
    .stButton>button {
        background-color: #1f2833;
        color: #66fcf1;
        border: 2px solid #66fcf1;
        box-shadow: 0 0 8px #66fcf1;
        font-weight: bold;
        border-radius: 5px;
        width: 100%;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #66fcf1;
        color: #0b0c10;
        box-shadow: 0 0 15px #66fcf1;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 10px;
        width: 100%;
        text-align: center;
        color: #45f3ff;
        font-size: 12px;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_html=True)

# 4. App States Setup
if "step" not in st.session_state:
    st.session_state.step = 1
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

# --- PAGE 1: INTRO ---
if st.session_state.step == 1:
    st.write("")
    st.markdown("<h2 class='cyber-header'>Hi Abigail, click the button below to continue</h2>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("⚡"):
        st.session_state.step = 2
        st.rerun()

# --- PAGE 2: GRADUATION ---
elif st.session_state.step == 2:
    st.write("")
    st.markdown("""
        <p class='cyber-text'>
        Now that graduation is done, SS3 is dusted, and we're now going our separate ways, 
        we definitely deserve to breathe some air. I made this quick interface for you...
        </p>
    """, unsafe_allow_html=True)
    st.write("")
    
    if st.button("INITIALIZE MYSTERY DECRYPT"):
        st.session_state.step = 3
        st.rerun()

# --- PAGE 3: THE QUESTION ---
elif st.session_state.step == 3:
    st.write("")
    st.markdown("<h1 class='cyber-header'>Will you go on a date with me?</h1>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("YES! 🥳"):
            send_notification("🚨 NOTIFICATION: Sotonye clicked YES! 🎉")
            st.session_state.step = 4
            st.rerun()
            
    with col2:
        if st.session_state.no_clicks < 3:
            no_labels = ["NO 😢", "Are you sure? 🤨", "Wait, really? 💔"]
            current_label = no_labels[st.session_state.no_clicks]
            
            if st.button(current_label):
                st.session_state.no_clicks += 1
                st.rerun()
        else:
            st.markdown("<p style='color:#ef4444; font-weight:bold; text-align:center;'>Access Denied. Selection locked.</p>", unsafe_allow_html=True)
            if st.session_state.no_clicks == 3:
                send_notification("⚠️ NOTIFICATION: Sotonye clicked No 3 times.")
                st.session_state.no_clicks = 4

# --- PAGE 4: SUCCESS WITH TYPING EFFECT ---
elif st.session_state.step == 4:
    st.balloons()
    st.write("")
    st.markdown("<h2 class='cyber-header'>// ACCESS GRANTED</h2>", unsafe_allow_html=True)
    
    target_text = "Let's gooooo!. I'll lock in the final details with you later tonight. Stay tuned."
    placeholder = st.empty()
    
    displayed_text = ""
    for char in target_text:
        displayed_text += char
        placeholder.markdown(f"<p class='cyber-text' style='font-size:1.5rem;'>{displayed_text}</p>", unsafe_allow_html=True)
        time.sleep(0.06)
        
    placeholder.markdown(f"<p class='cyber-text' style='font-size:1.5rem;'>{target_text}</p>", unsafe_allow_html=True)

# Footer Credits
st.write("---")
st.markdown("""
    <p style='font-family: "Share Tech Mono", monospace; color: #64748b; text-align: center;'>
    Copyright © 2026 | Code by Greatman (Vertigo Software)
    </p>
""", unsafe_allow_html=True)
