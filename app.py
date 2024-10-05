import streamlit as st
import pandas as pd
import numpy as np
import pickle
# import git

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:11]

    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

movies_dick = pickle.load(open('moive_dict.pkl','rb'))
movies = pd.DataFrame(movies_dick)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

select_movie_name = st.selectbox(
    "How would you like to be contacted?",movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(select_movie_name)
    for i in recommendations:
        st.write(i)