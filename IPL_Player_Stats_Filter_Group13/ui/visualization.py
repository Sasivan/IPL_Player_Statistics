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
    # 🏆 Top Players Section (Dynamic Chart Type)
    # -------------------------------
    st.subheader("🏆 Top Players")

    metric = st.selectbox("Select metric to rank players", ["Runs", "B_Wkts", "SOLD_PRICE"], index=0)
    chart_type = st.selectbox("Select chart type", ["Line", "Bar", "Scatter", "Area"], index=3)
    top_n = st.slider("Number of top players to display", 5, 20, 10)

    top_players = df.sort_values(by=metric, ascending=False).head(top_n)

    # Create chart based on selection
    if chart_type == "Line":
        fig_top = px.line(
            top_players, x="Player", y=metric, color="TEAM",
            markers=True, title=f"Top {top_n} Players by {metric} (Line Chart)"
        )
    elif chart_type == "Bar":
        fig_top = px.bar(
            top_players, x="Player", y=metric, color="TEAM", text=metric,
            title=f"Top {top_n} Players by {metric} (Bar Chart)"
        )
    elif chart_type == "Scatter":
        fig_top = px.scatter(
            top_players, x="Player", y=metric, color="TEAM", size=metric,
            title=f"Top {top_n} Players by {metric} (Scatter Plot)"
        )
    elif chart_type == "Area":
        fig_top = px.area(
            top_players, x="Player", y=metric, color="TEAM",
            title=f"Top {top_n} Players by {metric} (Area Chart)"
        )

    fig_top.update_layout(
        height=400,
        xaxis_title="Player",
        yaxis_title=metric,
        hovermode="x unified"
    )
    st.plotly_chart(fig_top, use_container_width=True)

    # -------------------------------
    # Team Performance Section (Pie Chart)
    # -------------------------------
    st.subheader("🏟 Team Performance")
    team_metric = st.selectbox("Select metric for team performance", ["Runs", "B_Wkts", "Avg", "SR"], index=0)

    team_stats = df.groupby("TEAM")[team_metric].sum().reset_index()
    fig_team = px.pie(
        team_stats,
        names="TEAM",
        values=team_metric,
        color="TEAM",
        title=f"Team Contribution by {team_metric}",
        hole=0.4
    )
    fig_team.update_traces(textposition="inside", textinfo="percent+label")
    st.plotly_chart(fig_team, use_container_width=True)

    # -------------------------------
    # Player Strike Rate vs Average (Scatter Plot)
    # -------------------------------
    st.subheader("⚡ Performance Comparison")
    fig_scatter = px.scatter(
        df,
        x="Avg",
        y="SR",
        size="Runs",
        color="TEAM",
        hover_name="Player",
        height=400,
        title="Player Strike Rate vs Batting Average"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

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
