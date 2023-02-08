import streamlit as st
import classes

st.title("OFC Royalty Calculator")

# Determine number of players
number_of_players = st.selectbox("Select Number of Players", ("2", "3", "4"))

# Set page up for number of players
if number_of_players == "4":
    classes.Calculate.four_players(number_of_players)

elif number_of_players == "3":
    classes.Calculate.three_players(number_of_players)

else:
    classes.Calculate.two_players(number_of_players)

