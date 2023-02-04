import pandas as pd
import streamlit as st

# Load dataframe
#df = pd.read_csv("ofcroyalties.xlsx")

# Determine game type and number of players
st.title("OFC Royalty Calculator")
gametype = st.selectbox("Select Game", ("Standard", "Deuce to Seven"))
number_of_players = st.selectbox("Select Number of Players", ("2", "3", "4"))