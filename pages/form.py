import streamlit as st

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
