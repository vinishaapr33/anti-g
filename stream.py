st.markdown("""
    <style>
    .antigravity {
        position: relative;
        display: inline-block;
        padding: 12px 20px;
        background: #4CAF50;
        color: white;
        border-radius: 8px;
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0%   { transform: translateY(0); }
        50%  { transform: translateY(-10px); }
        100% { transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

import streamlit as st

# Page setup
st.set_page_config(page_title="🎶 Anti-Gravity Music App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Upload Music", "API Music", "Visualizer", "About"])

# Home Page
if page == "Home":
    st.title("🎶 Anti-Gravity Music App")
    st.write("Play, explore, and visualize music with a floating touch ✨")
    st.markdown('<button class="antigravity">Start Exploring 🎵</button>', unsafe_allow_html=True)

# Upload Music Page
elif page == "Upload Music":
    st.title("📂 Upload Your Music")
    uploaded_file = st.file_uploader("Upload an MP3 file", type=["mp3"])
    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/mp3")

# API Music Page
elif page == "API Music":
    st.title("🌐 Music via API")
    st.write("Search and play tracks using Spotify/YouTube API (coming soon).")

# Visualizer Page
elif page == "Visualizer":
    st.title("📊 Music Visualizer")
    st.write("Waveforms, spectrograms, and charts will appear here.")

# About Page
elif page == "About":
    st.title("ℹ️ About This App")
    st.write("Created by Vinishaa. Built with Streamlit. Safe use of music via APIs and uploads.")
