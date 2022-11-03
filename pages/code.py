import streamlit as st

st.subheader('Code')

code = '''
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

st.subheader('Form')

with st.form(key='profile_form'):
    name = st.text_input('Name')
    address = st.text_input('Address')

    age_category = st.radio(
        'Age',
        ('Kid', 'Adult')
    )
    hobby = st.multiselect(
        'Hobby',
        ('Sports', 'Reading', 'Programming', 'Movie', 'Cooking')
    )

    submit_btn = st.form_submit_button('Submit')
    cancel_btn = st.form_submit_button('Cancel')
    if submit_btn:
        st.text(f'Welcome {name}! Your address is {address}.')
        st.text(f'Age: {age_category}')
        st.text(f'Hobby: {",".join(hobby)}')
'''

st.code(code, language='python')