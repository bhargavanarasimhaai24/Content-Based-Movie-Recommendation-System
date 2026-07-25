import streamlit as st
import pickle

df = pickle.load(open('movies.pkl', 'rb'))
movies_list = df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    idx = df[df['title'] == movie].index[0]
    relation = similarity[idx]
    movies_closer = sorted(list(enumerate(relation)), reverse=True, key=lambda x: x[1])[1:6]
    recs = []
    for movie in movies_closer:
        recs.append(df.iloc[movie[0]].title)
    return recs

st.title('🎬 Content-Based Movie Recommendation System')
input_movie = st.selectbox('Select the MOVIE', movies_list)

if st.button("Recommend"):
    recs = recommend(input_movie)
    for i in recs:
        st.write(i)
