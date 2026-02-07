import streamlit as st

# Hello World Streamlit App
st.title("Hello World!")
st.write("Welcome to my first Streamlit application!")

# Add some interactive elements
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! 👋")

# Add a simple button
if st.button("Click me!"):
    st.balloons()
    st.success("You clicked the button!")
