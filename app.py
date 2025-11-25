
import streamlit as st
import pandas as pd
import pickle
from streamlit_option_menu import option_menu

# Load movie data
movies = pickle.load(open('movies.pkl', 'rb'))

# Set page config
st.set_page_config(page_title="MovieFlix", layout="wide")

# Custom CSS for Netflix‑style UI
st.markdown("""
<style>
body {
    background-color: #000000 !important;
}

.main-title {
    font-size: 48px;
    font-weight: 800;
    color: #e50914;
    text-align: center;
    margin-bottom: 30px;
    font-family: 'Arial Black';
}

.movie-card {
    background-color: #141414;
    border-radius: 12px;
    padding: 10px;
    text-align: center;
    transition: 0.3s;
}

.movie-card:hover {
    transform: scale(1.06);
    background-color: #1f1f1f;
}

.movie-title {
    color: white;
    font-size: 18px;
    font-weight: 600;
}

section {
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title\st.markdown('<div class="main-title">🎬 MovieFlix Recommendations</div>', unsafe_allow_html=True)

# Dropdown
title = st.selectbox("Select a movie to get recommendations:", movies['title'].values)

# Recommend Function

def recommend(movie):
    # Dummy recommendations for now
    return movies['title'].head(6).values

if st.button("Show Recommendations", use_container_width=True):
    recs = recommend(title)
    st.markdown("<h2 style='color:white;'>Recommended for you</h2>", unsafe_allow_html=True)

    cols = st.columns(3)
    idx = 0
    for col in cols:
        with col:
            for _ in range(2):
                st.markdown(f"<div class='movie-card'><p class='movie-title'>{recs[idx]}</p></div>", unsafe_allow_html=True)
                idx += 1
