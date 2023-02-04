import streamlit as st
import pandas as pd
# Load the data frames
bottom_df = pd.read_excel("ofcroyalties.xlsx", "BottomHand")
middle_df = pd.read_excel("ofcroyalties.xlsx", "MiddleHand")
top_df = pd.read_excel("ofcroyalties.xlsx", "TopHand")

class NumPlayers:
    def __init__(self, num_players,
                 p1_top, p1_middle, p1_bottom,
                 p2_top, p2_middle, p2_bottom,
                 p3_top, p3_middle, p3_bottom,
                 p4_top, p4_middle, p4_bottom,):
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
            p1_top = st.selectbox("Player 1 Top Hand",
                                  ("Non-scoring Hand", "Sixes", "Sevens", "Eights", "Nines",
                                   "Tens", "Jacks", "Queens", "Kings",
                                   "Aces", "Trip Deuces", "Trip Threes",
                                   "Trip Fours", "Trip Fives", "Trip Sixes",
                                   "Trip Sevens", "Trip Eights", "Trip Nines",
                                   "Trip Tens", "Trip Jacks", "Trip Queens",
                                   "Trip Kings", "Trip Aces"))
            p1_middle = st.selectbox("Player 1 Middle Hand",
                                     ("Non-scoring Hand", "Set", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush", "Nine Low", "Eight Low",
                                      "Seven Low", "Wheel"))

            p1_bottom = st.selectbox("Player 1 Bottom Hand",
                                     ("Non-scoring Hand", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush"))

        with col2:
            st.subheader("Player 2 Hands")
            p2_top = st.selectbox("Player 2 Top Hand",
                                  ("Non-scoring Hand", "Sixes", "Sevens", "Eights", "Nines",
                                   "Tens", "Jacks", "Queens", "Kings",
                                   "Aces", "Trip Deuces", "Trip Threes",
                                   "Trip Fours", "Trip Fives", "Trip Sixes",
                                   "Trip Sevens", "Trip Eights", "Trip Nines",
                                   "Trip Tens", "Trip Jacks", "Trip Queens",
                                   "Trip Kings", "Trip Aces"))
            p2_middle = st.selectbox("Player 2 Middle Hand",
                                     ("Non-scoring Hand", "Set", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush", "Nine Low", "Eight Low",
                                      "Seven Low", "Wheel"))
            p2_bottom = st.selectbox("Player 2 Bottom Hand",
                                     ("Non-scoring Hand", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush"))

        with col3:
            st.subheader("Player 3 Hands")
            p3_top = st.selectbox("Player 3 Top Hand",
                                  ("Non-scoring Hand", "Sixes", "Sevens", "Eights", "Nines",
                                   "Tens", "Jacks", "Queens", "Kings",
                                   "Aces", "Trip Deuces", "Trip Threes",
                                   "Trip Fours", "Trip Fives", "Trip Sixes",
                                   "Trip Sevens", "Trip Eights", "Trip Nines",
                                   "Trip Tens", "Trip Jacks", "Trip Queens",
                                   "Trip Kings", "Trip Aces"))
            p3_middle = st.selectbox("Player 3 Middle Hand",
                                     ("Non-scoring Hand", "Set", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush", "Nine Low", "Eight Low",
                                      "Seven Low", "Wheel"))
            p3_bottom = st.selectbox("Player 3 Bottom Hand",
                                     ("Non-scoring Hand", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush"))

        with col4:
            st.subheader("Player 4 Hands")
            p4_top = st.selectbox("Player 4 Top Hand",
                                  ("Non-scoring Hand", "Sixes", "Sevens", "Eights", "Nines",
                                   "Tens", "Jacks", "Queens", "Kings",
                                   "Aces", "Trip Deuces", "Trip Threes",
                                   "Trip Fours", "Trip Fives", "Trip Sixes",
                                   "Trip Sevens", "Trip Eights", "Trip Nines",
                                   "Trip Tens", "Trip Jacks", "Trip Queens",
                                   "Trip Kings", "Trip Aces"))
            p4_middle = st.selectbox("Player 4 Middle Hand",
                                     ("Non-scoring Hand", "Set", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush", "Nine Low", "Eight Low",
                                      "Seven Low", "Wheel"))
            p4_bottom = st.selectbox("Player 4 Bottom Hand",
                                     ("Non-scoring Hand", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush"))

        player_hands = [p1_top, p1_middle, p1_bottom, p2_top, p2_middle, p2_bottom,
                        p3_top, p3_middle, p3_bottom, p4_top, p4_middle, p4_bottom]
        return player_hands

    def three_players(self):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Player 1 Hands")
            p1_top = st.selectbox("Player 1 Top Hand",
                                  ("Non-scoring Hand", "Sixes", "Sevens", "Eights", "Nines",
                                   "Tens", "Jacks", "Queens", "Kings",
                                   "Aces", "Trip Deuces", "Trip Threes",
                                   "Trip Fours", "Trip Fives", "Trip Sixes",
                                   "Trip Sevens", "Trip Eights", "Trip Nines",
                                   "Trip Tens", "Trip Jacks", "Trip Queens",
                                   "Trip Kings", "Trip Aces"))
            p1_middle = st.selectbox("Player 1 Middle Hand",
                                     ("Non-scoring Hand", "Set", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush", "Nine Low", "Eight Low",
                                      "Seven Low", "Wheel"))
            p1_bottom = st.selectbox("Player 1 Bottom Hand",
                                     ("Non-scoring Hand", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush"))

        with col2:
            st.subheader("Player 2 Hands")
            p2_top = st.selectbox("Player 2 Top Hand",
                                  ("Non-scoring Hand", "Sixes", "Sevens", "Eights", "Nines",
                                   "Tens", "Jacks", "Queens", "Kings",
                                   "Aces", "Trip Deuces", "Trip Threes",
                                   "Trip Fours", "Trip Fives", "Trip Sixes",
                                   "Trip Sevens", "Trip Eights", "Trip Nines",
                                   "Trip Tens", "Trip Jacks", "Trip Queens",
                                   "Trip Kings", "Trip Aces"))
            p2_middle = st.selectbox("Player 2 Middle Hand",
                                     ("Non-scoring Hand", "Set", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush", "Nine Low", "Eight Low",
                                      "Seven Low", "Wheel"))
            p2_bottom = st.selectbox("Player 2 Bottom Hand",
                                     ("Non-scoring Hand", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush"))

        with col3:
            st.subheader("Player 3 Hands")
            p3_top = st.selectbox("Player 3 Top Hand",
                                  ("Non-scoring Hand", "Sixes", "Sevens", "Eights", "Nines",
                                   "Tens", "Jacks", "Queens", "Kings",
                                   "Aces", "Trip Deuces", "Trip Threes",
                                   "Trip Fours", "Trip Fives", "Trip Sixes",
                                   "Trip Sevens", "Trip Eights", "Trip Nines",
                                   "Trip Tens", "Trip Jacks", "Trip Queens",
                                   "Trip Kings", "Trip Aces"))
            p3_middle = st.selectbox("Player 3 Middle Hand",
                                     ("Non-scoring Hand", "Set", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush", "Nine Low", "Eight Low",
                                      "Seven Low", "Wheel"))
            p3_bottom = st.selectbox("Player 3 Bottom Hand",
                                     ("Non-scoring Hand", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush"))

        player_hands = [p1_top, p1_middle, p1_bottom, p2_top, p2_middle, p2_bottom,
                        p3_top, p3_middle, p3_bottom]
        return player_hands

    def two_players(self):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Player 1 Hands")
            p1_top = st.selectbox("Player 1 Top Hand",
                                  ("Non-scoring Hand", "Sixes", "Sevens", "Eights", "Nines",
                                   "Tens", "Jacks", "Queens", "Kings",
                                   "Aces", "Trip Deuces", "Trip Threes",
                                   "Trip Fours", "Trip Fives", "Trip Sixes",
                                   "Trip Sevens", "Trip Eights", "Trip Nines",
                                   "Trip Tens", "Trip Jacks", "Trip Queens",
                                   "Trip Kings", "Trip Aces"))
            p1_middle = st.selectbox("Player 1 Middle Hand",
                                     ("Non-scoring Hand", "Set", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush", "Nine Low", "Eight Low",
                                      "Seven Low", "Wheel"))
            p1_bottom = st.selectbox("Player 1 Bottom Hand",
                                     ("Non-scoring Hand", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush"))

        with col2:
            st.subheader("Player 2 Hands")
            p2_top = st.selectbox("Player 2 Top Hand",
                                  ("Non-scoring Hand", "Sixes", "Sevens", "Eights", "Nines",
                                   "Tens", "Jacks", "Queens", "Kings",
                                   "Aces", "Trip Deuces", "Trip Threes",
                                   "Trip Fours", "Trip Fives", "Trip Sixes",
                                   "Trip Sevens", "Trip Eights", "Trip Nines",
                                   "Trip Tens", "Trip Jacks", "Trip Queens",
                                   "Trip Kings", "Trip Aces"))
            p2_middle = st.selectbox("Player 2 Middle Hand",
                                     ("Non-scoring Hand", "Set", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush", "Nine Low", "Eight Low",
                                      "Seven Low", "Wheel"))
            p2_bottom = st.selectbox("Player 2 Bottom Hand",
                                     ("Non-scoring Hand", "Straight", "Flush",
                                      "Full House", "Quads", "Straight Flush",
                                      "Royal Flush"))

        player_hands = [p1_top, p1_middle, p1_bottom, p2_top, p2_middle, p2_bottom]
        return player_hands


