import streamlit as st
import classes_file
import pandas as pd
st.title("OFC Royalty Calculator")
# Load the data frames
top_df = pd.read_excel("ofcroyalties.xlsx", "TopHand",index_col=False)
middle_df = pd.read_excel("ofcroyalties.xlsx", "MiddleHand")
bottom_df = pd.read_excel("ofcroyalties.xlsx", "BottomHand")
# Determine number of players
number_of_players = st.selectbox("Select Number of Players", ("2", "3", "4"))

# Set page up for number of players
if number_of_players == "4":
    classes_file.Calculate.four_players(number_of_players)

elif number_of_players == "3":
    classes_file.Calculate.three_players(number_of_players)

else:
    classes_file.Calculate.two_players(number_of_players)

st.header("Quick Reference Hand Charts")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Top Hands")
    st.dataframe(top_df, width=350)

with col2:
    st.subheader("Middle Hands")
    st.dataframe(middle_df, width=350)

with col3:
    st.subheader("Bottom Hands")
    st.dataframe(bottom_df, width=350)