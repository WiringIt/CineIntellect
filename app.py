# import streamlit as st
# import pickle
# import pandas as pd
# # def recommend(movie):
# #     movie_index=movies[movies['title']==movie].index[0]
# #     distances=similarity[movie_index]
# #     movies_list=sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])[1:6]
# #     recommended_movies=[]
# #     for i in movies_list:
# #         recommended_movies.append(movies.iloc[i[0]].title)
# #     return recommended_movies
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]  # Find the index of the selected movie
#     distances = similarity[movie_index]  # Get the similarity scores for the selected movie
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # Sort by similarity
#     recommended_movies = []
#     for i in movies_list:
#         recommended_movies.append(movies.iloc[i[0]].title)  # Get the titles of the recommended movies
#     return recommended_movies
#
# movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies=pd.DataFrame(movie_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))
# st.title('Movie Recommender system')
# selected_movie_name = st.selectbox(
#     "Select a movie",
#     (movies['title'].values))
# if st.button("Recommend"):
#     recommendations=recommend(selected_movie_name)
#     for i in recommendations:
#         st.write(i)
import streamlit as st
import pickle
import pandas as pd
import requests  # Used to make requests to OMDb API


# Function to fetch movie poster from OMDb using the movie title
def get_movie_poster(movie_title):
    api_key = '328c6cdf'  # Replace with your OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"  # OMDb API URL
    response = requests.get(url)
    data = response.json()  # Convert the response to a JSON object

    # Check if the response is successful and contains a poster
    if data.get("Response") == "True":
        poster_url = data.get("Poster")  # Extract the poster URL
        return poster_url
    return None  # Return None if no poster is found or if the movie is not found


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Load the necessary data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app setup
st.title('Movie Recommender System')
selected_movie_name = st.selectbox("Select a movie", (movies['title'].values))

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)

    # Create columns to display posters side by side
    cols = st.columns(5)  # We will create 5 columns for the 5 recommendations

    for idx, movie in enumerate(recommendations):
        poster_url = get_movie_poster(movie)  # Get the movie poster URL
        with cols[idx]:  # Use the index to place the poster in the respective column
            st.write(movie)
            if poster_url:
                st.image(poster_url, width=200)  # Display the poster side by side
            else:
                st.write("Poster not available")  # Fallback if no poster is found


