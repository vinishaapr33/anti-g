import streamlit as st

st.set_page_config(page_title="Anti-Gravity Demo", layout="centered")

st.title("🌌 Anti-Gravity Effect in Web Dev")

# Inject custom CSS for floating animation
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

# Render floating button
st.markdown('<button class="antigravity">Click Me</button>', unsafe_allow_html=True)
