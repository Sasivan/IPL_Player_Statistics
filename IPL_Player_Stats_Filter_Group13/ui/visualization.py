import os
import sys
import streamlit as st
import pandas as pd
import plotly.express as px

def run():
    # -------------------------------
    # Add project root to sys.path
    # -------------------------------
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
    from backend.data_loader import load_ipl_data
    from backend.player_model import Player
    # -------------------------------
    # Paths for CSV and images
    # -------------------------------
    DATA_FILE = os.path.join(PROJECT_ROOT, "data", "ipl_player_stats_clean.csv")
    IMAGE_FOLDER = os.path.join(PROJECT_ROOT, "player_images")

    # -------------------------------
    # Page Configuration
    # -------------------------------
    st.set_page_config(
        page_title="IPL Visualizations",
        page_icon="📊",
        layout="wide"
    )

    st.title("📊 IPL Player & Team Visualizations")
    st.markdown("Visualize top players and team performances with charts.")
    st.markdown("---")

    # -------------------------------
    # Load Data
    # -------------------------------
    df = load_ipl_data(DATA_FILE)

    # -------------------------------
    # Top Players Section
    # -------------------------------
    st.subheader("🏆 Top Players")
    metric = st.selectbox("Select metric to rank players", ["Runs", "B_Wkts", "SOLD_PRICE"], index=0)
    top_n = st.slider("Number of top players to display", 5, 20, 10)

    top_players = df.sort_values(by=metric, ascending=False).head(top_n)
    fig_top = px.bar(
        top_players,
        x="Player",
        y=metric,
        color="TEAM",
        text=metric,
        height=400
    )
    st.plotly_chart(fig_top, use_container_width=True)

    # -------------------------------
    # Team Performance Section
    # -------------------------------
    st.subheader("🏟 Team Performance")
    team_metric = st.selectbox("Select metric for team performance", ["Runs", "B_Wkts", "Avg", "SR"], index=0)

    team_stats = df.groupby("TEAM")[team_metric].sum().reset_index()
    fig_team = px.bar(
        team_stats,
        x="TEAM",
        y=team_metric,
        color="TEAM",
        text=team_metric,
        height=400
    )
    st.plotly_chart(fig_team, use_container_width=True)

    # -------------------------------
    # Runs per Match / Season
    # -------------------------------
    st.subheader("📈 Runs per Match Distribution")
    runs_per_match = df[["Player", "Mat", "Runs"]].copy()
    runs_per_match["Runs_per_Match"] = runs_per_match["Runs"] / runs_per_match["Mat"]
    fig_rpm = px.bar(
        runs_per_match.sort_values("Runs_per_Match", ascending=False).head(top_n),
        x="Player",
        y="Runs_per_Match",
        color="Player",
        text="Runs_per_Match",
        height=400
    )
    st.plotly_chart(fig_rpm, use_container_width=True)
