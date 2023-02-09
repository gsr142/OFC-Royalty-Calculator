import streamlit as st
import pandas as pd
# Load the data frames and create dictionaries for bottom, middle, and top hands
bottom_df = pd.read_excel("ofcroyalties.xlsx", "BottomHand")
bottom_vals_dict = bottom_df.set_index('HAND VALUE').to_dict()['UNITS']

middle_df = pd.read_excel("ofcroyalties.xlsx", "MiddleHand")
middle_vals_dict = middle_df.set_index('HAND VALUE').to_dict()['UNITS']

top_df = pd.read_excel("ofcroyalties.xlsx", "TopHand")
top_vals_dict = top_df.set_index('HAND VALUE').to_dict()['UNITS']


class HandVals:
    def __init__(self, player_hands, hand_dict, pt_val_dict):
        self.player_hands = player_hands
        self.hand_dict = hand_dict
        self.pt_val_dict = pt_val_dict

    # Iterates through the hand value dictionaries to assign points based on hand strength
    def hand_points(self, player_hands, hand_dict):
        player_vals = []
        for hand in player_hands:
            for key in hand_dict.keys():
                if hand == key:
                    player_vals.append(hand_dict[key])
        return player_vals

    # Method for comparing hands to each other, and assigning payouts for each player
    def compare_dict_values(self, pt_val_dict):
        values = list(pt_val_dict.values())
        keys = list(pt_val_dict.keys())
        payouts = ""
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                if values[i] < values[j]:
                    payouts += f"{keys[i]} owes {values[j] - values[i]} to {keys[j]}. "
                elif values[i] > values[j]:
                    payouts += f"{keys[j]} owes {values[i] - values[j]} to {keys[i]}. "
                else:
                    payouts += f"{keys[i]} and {keys[j]} cancel out. "
        return payouts


class Calculate(HandVals):
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
        # Collects hand data from each player and calculates royalty payments
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.subheader("Player 1 Hands")
            p1_top = st.selectbox("Player 1 Top Hand", tuple(top_vals_dict))
            p1_middle = st.selectbox("Player 1 Middle Hand", tuple(middle_vals_dict))
            p1_bottom = st.selectbox("Player 1 Bottom Hand", tuple(bottom_vals_dict))

        with col2:
            st.subheader("Player 2 Hands")
            p2_top = st.selectbox("Player 2 Top Hand", tuple(top_vals_dict))
            p2_middle = st.selectbox("Player 2 Middle Hand", tuple(middle_vals_dict))
            p2_bottom = st.selectbox("Player 2 Bottom Hand", tuple(bottom_vals_dict))

        with col3:
            st.subheader("Player 3 Hands")
            p3_top = st.selectbox("Player 3 Top Hand", tuple(top_vals_dict))
            p3_middle = st.selectbox("Player 3 Middle Hand", tuple(middle_vals_dict))
            p3_bottom = st.selectbox("Player 3 Bottom Hand", tuple(bottom_vals_dict))

        with col4:
            st.subheader("Player 4 Hands")
            p4_top = st.selectbox("Player 4 Top Hand", tuple(top_vals_dict))
            p4_middle = st.selectbox("Player 4 Middle Hand", tuple(middle_vals_dict))
            p4_bottom = st.selectbox("Player 4 Bottom Hand", tuple(bottom_vals_dict))

        player_hands_top = [p1_top, p2_top, p3_top, p4_top]
        player_hands_middle = [p1_middle, p2_middle, p3_middle, p4_middle]
        player_hands_bottom = [p1_bottom, p2_bottom, p3_bottom, p4_bottom]

        player_vals_top = HandVals.hand_points(self, player_hands_top, top_vals_dict)
        player_vals_middle = HandVals.hand_points(self, player_hands_middle, middle_vals_dict)
        player_vals_bottom = HandVals.hand_points(self, player_hands_bottom, bottom_vals_dict)

        players = ["Player 1", "Player 2", "Player 3", "Player 4"]
        player_points_dict_top = dict(zip(players, player_vals_top))
        player_points_dict_middle = dict(zip(players, player_vals_middle))
        player_points_dict_bottom = dict(zip(players, player_vals_bottom))

        if st.button(label="Calculate Royalties"):
            # Compares all top hands and returns royalty payments for each player
            st.write(f"Top Hand: {HandVals.compare_dict_values(self, player_points_dict_top)}")
            # Compares all middle hands and returns royalty payments for each player
            st.write(f"Middle Hand: {HandVals.compare_dict_values(self, player_points_dict_middle)}")
            # Compares all bottom hands and returns royalty payments for each player
            st.write(f"Bottom Hand: {HandVals.compare_dict_values(self, player_points_dict_bottom)}")


    def three_players(self):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Player 1 Hands")
            p1_top = st.selectbox("Player 1 Top Hand", tuple(top_vals_dict))
            p1_middle = st.selectbox("Player 1 Middle Hand", tuple(middle_vals_dict))
            p1_bottom = st.selectbox("Player 1 Bottom Hand", tuple(bottom_vals_dict))

        with col2:
            st.subheader("Player 2 Hands")
            p2_top = st.selectbox("Player 2 Top Hand", tuple(top_vals_dict))
            p2_middle = st.selectbox("Player 2 Middle Hand", tuple(middle_vals_dict))
            p2_bottom = st.selectbox("Player 2 Bottom Hand", tuple(bottom_vals_dict))

        with col3:
            st.subheader("Player 3 Hands")
            p3_top = st.selectbox("Player 3 Top Hand", tuple(top_vals_dict))
            p3_middle = st.selectbox("Player 3 Middle Hand", tuple(middle_vals_dict))
            p3_bottom = st.selectbox("Player 3 Bottom Hand", tuple(bottom_vals_dict))

        player_hands_top = [p1_top, p2_top, p3_top]
        player_hands_middle = [p1_middle, p2_middle, p3_middle]
        player_hands_bottom = [p1_bottom, p2_bottom, p3_bottom]

        player_vals_top = HandVals.hand_points(self, player_hands_top, top_vals_dict)
        player_vals_middle = HandVals.hand_points(self, player_hands_middle, middle_vals_dict)
        player_vals_bottom = HandVals.hand_points(self, player_hands_bottom, bottom_vals_dict)

        players = ["Player 1", "Player 2", "Player 3"]
        player_points_dict_top = dict(zip(players, player_vals_top))
        player_points_dict_middle = dict(zip(players, player_vals_middle))
        player_points_dict_bottom = dict(zip(players, player_vals_bottom))

        if st.button(label="Calculate Royalties"):
            # Compares all top hands and returns royalty payments for each player
            st.write(f"Top Hand: {HandVals.compare_dict_values(self, player_points_dict_top)}")
            # Compares all middle hands and returns royalty payments for each player
            st.write(f"Middle Hand: {HandVals.compare_dict_values(self, player_points_dict_middle)}")
            # Compares all bottom hands and returns royalty payments for each player
            st.write(f"Bottom Hand: {HandVals.compare_dict_values(self, player_points_dict_bottom)}")


    def two_players(self):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Player 1 Hands")
            p1_top = st.selectbox("Player 1 Top Hand", tuple(top_vals_dict))
            p1_middle = st.selectbox("Player 1 Middle Hand", tuple(middle_vals_dict))
            p1_bottom = st.selectbox("Player 1 Bottom Hand", tuple(bottom_vals_dict))

        with col2:
            st.subheader("Player 2 Hands")
            p2_top = st.selectbox("Player 2 Top Hand", tuple(top_vals_dict))
            p2_middle = st.selectbox("Player 2 Middle Hand", tuple(middle_vals_dict))
            p2_bottom = st.selectbox("Player 2 Bottom Hand", tuple(bottom_vals_dict))

        player_hands_top = [p1_top, p2_top]
        player_hands_middle = [p1_middle, p2_middle]
        player_hands_bottom = [p1_bottom, p2_bottom]

        player_vals_top = HandVals.hand_points(self, player_hands_top, top_vals_dict)
        player_vals_middle = HandVals.hand_points(self, player_hands_middle, middle_vals_dict)
        player_vals_bottom = HandVals.hand_points(self, player_hands_bottom, bottom_vals_dict)

        players = ["Player 1", "Player 2"]
        player_points_dict_top = dict(zip(players, player_vals_top))
        player_points_dict_middle = dict(zip(players, player_vals_middle))
        player_points_dict_bottom = dict(zip(players, player_vals_bottom))
        print(player_points_dict_top)
        if st.button(label="Calculate Royalties"):
            #Compares all top hands and returns royalty payments for each player
            st.write(f"Top Hand: {HandVals.compare_dict_values(self, player_points_dict_top)}")
            # Compares all middle hands and returns royalty payments for each player
            st.write(f"Middle Hand: {HandVals.compare_dict_values(self, player_points_dict_middle)}")
            # Compares all bottom hands and returns royalty payments for each player
            st.write(f"Bottom Hand: {HandVals.compare_dict_values(self, player_points_dict_bottom)}")


