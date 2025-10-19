import streamlit as st
import pandas as pd
import plotly.express as px

import os, sys
def run():
    # Add project root to sys.path
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)

    from backend.data_loader import load_ipl_data
    from backend.player_model import Player
    # -------------------------------
    # Page Configuration
    # -------------------------------
    st.set_page_config(
        page_title="IPL Player Comparison",
        page_icon="📊",
        layout="wide"
    )

    st.title("📊 IPL Player Stats Comparison")
    st.markdown("Select 2 or more players to compare their batting and bowling statistics.")
    st.markdown("---")

    # -------------------------------
    # Load Data
    # -------------------------------
    df = load_ipl_data()
    players_list = df["Player"].tolist()

    # -------------------------------
    # Player Selection
    # -------------------------------
    selected_players = st.multiselect(
        "Select Players to Compare",
        options=players_list,
        default=players_list[:2]  # default first 2 players
    )

    if selected_players:
        compare_df = df[df["Player"].isin(selected_players)]
        player_objects = [Player(row) for _, row in compare_df.iterrows()]

        # -------------------------------
        # Display Player Images
        # -------------------------------
        cols = st.columns(len(player_objects))
        for idx, player in enumerate(player_objects):
            col = cols[idx]
            with col:
                if player.image_path and os.path.exists(player.image_path):
                    st.image(player.image_path, width=200)
                else:
                    st.image("https://via.placeholder.com/200x200.png?text=No+Image", width=200)
                st.subheader(player.name)
                st.write(f"**Team:** {player.team}")
                st.write(f"**Role:** {player.role}")

        st.markdown("---")

        # -------------------------------
        # Batting Comparison Chart
        # -------------------------------
        batting_metrics = ["Runs", "Avg", "SR", "50s", "100s"]
        batting_data = compare_df[["Player"] + batting_metrics].set_index("Player")
        st.subheader("Batting Stats Comparison")
        fig_batting = px.bar(
            batting_data,
            barmode="group",
            height=400,
            labels={"value": "Value", "Player": "Player"},
        )
        st.plotly_chart(fig_batting, use_container_width=True)

        # -------------------------------
        # Bowling Comparison Chart
        # -------------------------------
        bowling_metrics = ["B_Wkts", "B_Avg", "B_Econ", "B_4w", "B_5w"]
        bowling_data = compare_df[["Player"] + bowling_metrics].set_index("Player")
        st.subheader("Bowling Stats Comparison")
        fig_bowling = px.bar(
            bowling_data,
            barmode="group",
            height=400,
            labels={"value": "Value", "Player": "Player"},
        )
        st.plotly_chart(fig_bowling, use_container_width=True)

    else:
        st.warning("Please select at least 2 players to compare.")
