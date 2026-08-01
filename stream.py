import streamlit as st
import yt_dlp   # keep imports at the top

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
        st.write("Filename:", uploaded_file.name)
        st.write("Size:", uploaded_file.size, "bytes")

# API Music Page
elif page == "API Music":
    st.title("🎶 YouTube Music Search (No Billing)")
    import moviepy.editor as mp

# MP4 to MP3 Converter Page
elif page == "Convert MP4 to MP3":
    st.title("🎥 MP4 to MP3 Converter")

    uploaded_file = st.file_uploader("Upload an MP4 file", type=["mp4"])
    if uploaded_file is not None:
        # Save uploaded file temporarily
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract audio
        video = mp.VideoFileClip(uploaded_file.name)
        audio = video.audio
        audio.write_audiofile("output.mp3")

        # Play converted audio
        st.audio("output.mp3")
        st.success("✅ Converted to MP3 successfully!")


    query = st.text_input("Search for a song:")
    if query:
        ydl_opts = {"quiet": True, "skip_download": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch5:{query}", download=False)
            for entry in info['entries']:
                title = entry['title']
                video_id = entry['id']
                st.write(f"🎵 {title}")
                st.markdown(f"""
                    <iframe width="560" height="315" 
                    src="https://www.youtube.com/embed/{video_id}" 
                    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen></iframe>
                """, unsafe_allow_html=True)

# Visualizer Page
elif page == "Visualizer":
    st.title("📊 Music Visualizer")
    st.write("Waveforms, spectrograms, and charts will appear here.")

# About Page
elif page == "About":
    st.title("ℹ️ About This App")
    st.write("Created by Vinishaa. Built with Streamlit. Safe use of music via APIs and uploads.")
    import moviepy.editor as mp

# MP4 to MP3 Converter Page
elif page == "Convert MP4 to MP3":
    st.title("🎥 MP4 to MP3 Converter")

    uploaded_file = st.file_uploader("Upload an MP4 file", type=["mp4"])
    if uploaded_file is not None:
        # Save uploaded file temporarily
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract audio
        video = mp.VideoFileClip(uploaded_file.name)
        audio = video.audio
        audio.write_audiofile("output.mp3")

        # Play converted audio
        st.audio("output.mp3")
        st.success("✅ Converted to MP3 successfully!")

