import streamlit as st

st.title("Favorite Color App")

# Get user input for their favorite color
favorite_color = st.text_input("What is your favorite color?", "Enter color here")

# Display the result
if favorite_color:  # Check if the user has entered a color
    st.write(f"Your favorite color is: {favorite_color}")
else:
    st.write("Please enter your favorite color above.")
