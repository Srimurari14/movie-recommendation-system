import pickle
import streamlit as st
import requests
import base64


def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(m):
    index=movies[movies['title']==m].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommended_movies=[]
    recommended_movie_posters=[]
    for i in distances[1:13]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies,recommended_movie_posters



st.title('Movie Recommendation System')
movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

def add_bg(image_file):
    with open(image_file,"rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg("C:\\Users\\murar\\OneDrive\\Desktop\\Wallpapers\\mrs.jpeg")

movie_list=movies['title'].values
selected_movie=st.selectbox("Type or select a movie from the dropdown",movie_list)

if st.button('Recommend'):
    with st.spinner(text='In progress'):
        recommended_movies,recommended_movie_posters=recommend(selected_movie)
        col1,col2,col3=st.columns(3)
        with col1:
            st.text(recommended_movies[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movies[1])
            st.image(recommended_movie_posters[1])
        with col3:
            st.text(recommended_movies[2])
            st.image(recommended_movie_posters[2])
        col1,col2,col3=st.columns(3)
        with col1:
            st.text(recommended_movies[3])
            st.image(recommended_movie_posters[3])
        with col2:
            st.text(recommended_movies[4])
            st.image(recommended_movie_posters[4])
        with col3:
            st.text(recommended_movies[5])
            st.image(recommended_movie_posters[5])
        col1,col2,col3=st.columns(3)
        with col1:
            st.text(recommended_movies[6])
            st.image(recommended_movie_posters[6])
        with col2:
            st.text(recommended_movies[7])
            st.image(recommended_movie_posters[7])
        with col3:
            st.text(recommended_movies[8])
            st.image(recommended_movie_posters[8])
        col1,col2,col3=st.columns(3)
        with col1:
            st.text(recommended_movies[9])
            st.image(recommended_movie_posters[9])
        with col2:
            st.text(recommended_movies[10])
            st.image(recommended_movie_posters[10])
        with col3:
            st.text(recommended_movies[11])
            st.image(recommended_movie_posters[11])
