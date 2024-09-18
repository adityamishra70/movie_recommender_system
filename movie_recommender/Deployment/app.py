import streamlit as st
import pickle
import pandas as pd

# Load pre-trained recommender model and movie data
# @st.cache_resource 


def load_distance():
    with open('distances.pkl', 'rb') as file:
        distances = pickle.load(file)
    return distances

# @st.cache_resource
def load_movies():
    movies = pd.read_csv('movies.csv')  # Assuming movies.csv contains movie information
    return movies

# Get movie recommendations
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = distances[movie_index]
    movie_list = sorted(list(enumerate(distance)) ,reverse=True, key=lambda x:x[1])[1:6]
    l = []
    for i in movie_list:
        l.append(movies.iloc[i[0]].title)
    return l

# Load model and movie data 
distances = load_distance()
movies = load_movies()

# Streamlit app layout
st.title('Movie Recommender System')

selected_movie = st.selectbox('Select a movie you like:', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.write('Recommendations:')
        j = 1
        for movie in recommendations:
            st.write(j ,movie)
            j += 1
    else:
        st.write('No recommendations found. Please try a different movie.')

# Run the app using: streamlit run movie_recommender.py