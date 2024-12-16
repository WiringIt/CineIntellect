import streamlit as st
import pickle
import pandas as pd
# def recommend(movie):
#     movie_index=movies[movies['title']==movie].index[0]
#     distances=similarity[movie_index]
#     movies_list=sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])[1:6]
#     recommended_movies=[]
#     for i in movies_list:
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # Find the index of the selected movie
    distances = similarity[movie_index]  # Get the similarity scores for the selected movie
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # Sort by similarity
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)  # Get the titles of the recommended movies
    return recommended_movies

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender system')
selected_movie_name = st.selectbox(
    "Select a movie",
    (movies['title'].values))
if st.button("Recommend"):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)


