import streamlit as st
import pandas as pd
# Load the data frames and create dictionaries for bottom, middle, and top hands
bottom_df = pd.read_excel("ofcroyalties.xlsx", "BottomHand")
bottom_vals_dict = bottom_df.set_index('HAND VALUE').to_dict()['UNITS']

middle_df = pd.read_excel("ofcroyalties.xlsx", "MiddleHand")
middle_vals_dict = middle_df.set_index('HAND VALUE').to_dict()['UNITS']

top_df = pd.read_excel("ofcroyalties.xlsx", "TopHand")
top_vals_dict = top_df.set_index('HAND VALUE').to_dict()['UNITS']

class NumPlayers:
    def __init__(self, num_players,
                 p1_top, p1_middle, p1_bottom,
                 p2_top, p2_middle, p2_bottom,
                 p3_top, p3_middle, p3_bottom,
                 p4_top, p4_middle, p4_bottom):
        self.num_players = num_players
        self.p1_top = p1_top
        self.p1_middle = p1_middle
        self.p1_bottom = p1_bottom
        self.p2_top = p2_top
        self.p2_middle = p2_middle
        self.p2_bottom = p2_bottom
        self.p3_top = p3_top
        self.p3_middle = p3_middle
        self.p3_bottom = p3_bottom
        self.p4_top = p4_top
        self.p4_middle = p4_middle
        self.p4_bottom = p4_bottom

    def four_players(self):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.subheader("Player 1 Hands")
            p1_top = st.selectbox("Player 1 Top Hand", tuple(top_vals_dict),key=1)
            p1_middle = st.selectbox("Player 1 Middle Hand", tuple(middle_vals_dict),key=2)
            p1_bottom = st.selectbox("Player 1 Bottom Hand", tuple(bottom_vals_dict),key=3)

        with col2:
            st.subheader("Player 2 Hands")
            p2_top = st.selectbox("Player 2 Top Hand", tuple(top_vals_dict),key=4)
            p2_middle = st.selectbox("Player 2 Middle Hand", tuple(middle_vals_dict),key=5)
            p2_bottom = st.selectbox("Player 2 Bottom Hand", tuple(bottom_vals_dict),key=6)

        with col3:
            st.subheader("Player 3 Hands")
            p3_top = st.selectbox("Player 3 Top Hand", tuple(top_vals_dict),key=7)
            p3_middle = st.selectbox("Player 3 Middle Hand", tuple(middle_vals_dict),key=8)
            p3_bottom = st.selectbox("Player 3 Bottom Hand", tuple(bottom_vals_dict),key=9)

        with col4:
            st.subheader("Player 4 Hands")
            p4_top = st.selectbox("Player 4 Top Hand", tuple(top_vals_dict),key=10)
            p4_middle = st.selectbox("Player 4 Middle Hand", tuple(middle_vals_dict),key=11)
            p4_bottom = st.selectbox("Player 4 Bottom Hand", tuple(bottom_vals_dict),key=12)

        player_hands = [p1_top, p1_middle, p1_bottom, p2_top, p2_middle, p2_bottom,
                        p3_top, p3_middle, p3_bottom, p4_top, p4_middle, p4_bottom]
        return player_hands

    def three_players(self):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Player 1 Hands")
            p1_top = st.selectbox("Player 1 Top Hand", tuple(top_vals_dict), key=13)
            p1_middle = st.selectbox("Player 1 Middle Hand", tuple(middle_vals_dict), key=14)
            p1_bottom = st.selectbox("Player 1 Bottom Hand", tuple(bottom_vals_dict), key=15)

        with col2:
            st.subheader("Player 2 Hands")
            p2_top = st.selectbox("Player 2 Top Hand", tuple(top_vals_dict), key=16)
            p2_middle = st.selectbox("Player 2 Middle Hand", tuple(middle_vals_dict), key=17)
            p2_bottom = st.selectbox("Player 2 Bottom Hand", tuple(bottom_vals_dict), key=18)

        with col3:
            st.subheader("Player 3 Hands")
            p3_top = st.selectbox("Player 3 Top Hand", tuple(top_vals_dict), key=19)
            p3_middle = st.selectbox("Player 3 Middle Hand", tuple(middle_vals_dict), key=20)
            p3_bottom = st.selectbox("Player 3 Bottom Hand", tuple(bottom_vals_dict), key=21)

        player_hands = [p1_top, p1_middle, p1_bottom, p2_top, p2_middle, p2_bottom,
                        p3_top, p3_middle, p3_bottom]
        return player_hands

    def two_players(self):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Player 1 Hands")
            p1_top = st.selectbox("Player 1 Top Hand", tuple(top_vals_dict), key=43)
            p1_middle = st.selectbox("Player 1 Middle Hand", tuple(middle_vals_dict), key=23)
            p1_bottom = st.selectbox("Player 1 Bottom Hand", tuple(bottom_vals_dict), key=24)

        with col2:
            st.subheader("Player 2 Hands")
            p2_top = st.selectbox("Player 2 Top Hand", tuple(top_vals_dict), key=25)
            p2_middle = st.selectbox("Player 2 Middle Hand", tuple(middle_vals_dict), key=26)
            p2_bottom = st.selectbox("Player 2 Bottom Hand", tuple(bottom_vals_dict), key=27)

        player_hands = [p1_top, p1_middle, p1_bottom, p2_top, p2_middle, p2_bottom]
        st.button(label="Calculate Royalties", key=30, on_click=(print(player_hands)))
        return player_hands

