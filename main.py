import streamlit as st
import classes

# Determine game type and number of players
st.title("OFC Royalty Calculator")
number_of_players = st.selectbox("Select Number of Players", ("2", "3", "4"))

# Enter player hands
if number_of_players == "4":
    classes.NumPlayers.four_players(number_of_players)
elif number_of_players == "3":
    classes.NumPlayers.three_players(number_of_players)
else:
    classes.NumPlayers.two_players(number_of_players)

