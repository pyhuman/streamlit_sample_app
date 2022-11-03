import streamlit as st
from PIL import Image

st.title('Sample Streamlit APP')
st.caption('This is a sample app by STREAMLIT')
st.subheader('Introduction')
st.text('Python is a programming language to learn easy. You can develop many apps!\n'
        'Python is a programming language to learn easy. You can develop many apps!\n')

st.subheader('Image')
image = Image.open('./data/sinw2187.jpg')
st.image(image)
