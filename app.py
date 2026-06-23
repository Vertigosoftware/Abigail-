import streamlit as st
import requests
import time

# 1. WEBHOOK & MUSIC CONFIGURATION
WEBHOOK_URL = "https://discord.com/api/webhooks/1518332304261644338/oSB0Va4IsPo3NHUNLBNIkkTl_Rv4NrTbvHaSkjtGwMfd_QcM4rO4kPoVJfrMoikOW9kU"
MUSIC_URL = "https://files.catbox.moe/ky4mr2.mp3"
def send_notification(message):
    try:
        requests.post(WEBHOOK_URL, json={"content": message})
    except:
        pass

# 2. Page Setup
st.set_page_config(page_title="Terminal_Sotonye", page_icon="✨", layout="centered")

# 3. Cyber-Noir (Female Vibe) Custom CSS Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Space+Grotesk:wght@400;600&display=swap');
    
    .main { 
        background-color: #090d16; 
        color: #f1f5f9; 
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .cyber-text {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.25rem;
        line-height: 1.6;
        color: #cbd5e1;
        text-align: center;
    }
    
    .cyber-header {
        font-family: 'Share Tech Mono', monospace;
        color: #38bdf8;
        text-align: center;
        text-shadow: 0px 0px 12px rgba(192, 132, 252, 0.5);
        margin-bottom: 2rem;
    }
    
    .stButton>button { 
        background-color: #0284c7; 
        color: #ffffff;
        border: none;
        padding: 12px;
        border-radius: 8px; 
        width: 100%;
        box-shadow: 0px 0px 15px rgba(56, 189, 248, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #0369a1;
        box-shadow: 0px 0px 25px rgba(192, 132, 252, 0.7);
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# 4. App States Setup
if "step" not in st.session_state:
    st.session_state.step = 1
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

# Persistent Music Component (Plays globally across pages once step 1 is left)
if st.session_state.step > 1:
    st.markdown(f"""
        <iframe src="{MUSIC_URL}" allow="autoplay" style="display:none" id="iframeAudio"></iframe>
        <audio autoplay loop hidden>
            <source src="{MUSIC_URL}" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

# --- PAGE 1: INTRO ---
if st.session_state.step == 1:
    st.write("")
    st.markdown("<h2 class='cyber-header'>Hi Abigail, click the button below to continue</h2>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("⚡"): 
        st.session_state.step = 2
        st.rerun()

# --- PAGE 2: GRADUATION & MUSIC INITIALIZATION ---
elif st.session_state.step == 2:
    st.write("")
    st.markdown("""<p class='cyber-text'>Now that graduation is done, SS3 is dusted, and we're now going to the university, we definitely deserve to breathe some air. I made this quick interface to ask you something...</p>""", unsafe_allow_html=True)
    st.write("")
    
    if st.button("INITIALIZE MYSTERY DECRYPT"):
        st.session_state.step = 3
        st.rerun()

# --- PAGE 3: THE QUESTION ---
elif st.session_state.step == 3:
    st.write("")
    st.markdown("<h1 class='cyber-header'>Will you go on a date with me? ☕</h1>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("YES! 🥳"):
            send_notification("🚨 NOTIFICATION: Sotonye clicked YES! 🎉")
            st.session_state.step = 4
            st.rerun()
            
    with col2:
        if st.session_state.no_clicks < 3:
            no_labels = ["NO 😢", "Are you sure? 🤨", "Wait, really? 😭"]
            current_label = no_labels[st.session_state.no_clicks]
            
            if st.button(current_label):
                st.session_state.no_clicks += 1
                st.rerun()
        else:
            st.markdown("<p style='color:#ef4444; font-weight:bold; text-align:center;'>Are you sure? If not, click yes.</p>", unsafe_allow_html=True)
            if st.session_state.no_clicks == 3:
                send_notification("⚠️ NOTIFICATION: Sotonye clicked No 3 times. Locked out! 😉")
                st.session_state.no_clicks = 4

# --- PAGE 4: SUCCESS WITH TYPING EFFECT ---
elif st.session_state.step == 4:
    st.balloons()
    st.write("")
    st.markdown("<h2 class='cyber-header'>// ACCESS GRANTED</h2>", unsafe_allow_html=True)
    
    target_text = "Let's gooooo!. I'll lock in the final details with you later, get some rest."
    placeholder = st.empty()
    
    displayed_text = ""
    for char in target_text:
        displayed_text += char
        placeholder.markdown(f"<p class='cyber-text' style='font-size:1.5rem; color:#fdf4ff;'>{displayed_text}█</p>", unsafe_allow_html=True)
        time.sleep(0.06)
        
    placeholder.markdown(f"<p class='cyber-text' style='font-size:1.5rem; color:#fdf4ff;'>{target_text}</p>", unsafe_allow_html=True)

# --- FOOTER CREDITS ---
st.write("---")
st.markdown("""
    <p style='font-family: "Share Tech Mono", monospace; color: #64748b; text-align: center; font-size: 0.85rem; letter-spacing: 1px;'>
        Copyright © 2026 | Code by Greatman (Vertigo Software)
    </p>
""", unsafe_allow_html=True)
