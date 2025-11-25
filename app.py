
import streamlit as st
import pandas as pd
import pickle
import requests

# --------------------------
# LOAD DATA
# --------------------------

movies = pd.read_csv("movies.csv")

similarity = pickle.load(open("similarity.pkl", "rb"))
movies_list = movies['title'].values

# --------------------------
# GET MOVIE POSTER FUNCTION
# --------------------------

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=72a5bd467f3b0d9442e5d4021ba38d4b"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    return "https://via.placeholder.com/500x750?text=No+Image"


# --------------------------
# RECOMMENDATION FUNCTION
# --------------------------



