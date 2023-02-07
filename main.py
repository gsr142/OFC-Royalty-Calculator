import streamlit as st
import classes

st.title("OFC Royalty Calculator")

# Determine number of players
number_of_players = st.selectbox("Select Number of Players", ("2", "3", "4"), key=31)

# Set page up for number of players
if number_of_players == "4":
    classes.NumPlayers.four_players(number_of_players)
    st.button(label="Calculate Royalties",key=28)

elif number_of_players == "3":
    classes.NumPlayers.three_players(number_of_players)
    st.button(label="Calculate Royalties",key=29)

else:
    classes.NumPlayers.two_players(number_of_players)

