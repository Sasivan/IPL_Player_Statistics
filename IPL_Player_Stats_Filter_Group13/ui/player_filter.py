import os
import sys
import streamlit as st
from PIL import Image
def run():
    # -------------------------------
    # Add project root to sys.path before importing backend
    # -------------------------------
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)

    # -------------------------------
    # Backend imports
    # -------------------------------
    from backend.data_loader import load_ipl_data
    from backend.stats_filter import filter_players
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
        page_title="IPL Player Filter",
        page_icon="🔍",
        layout="wide"
    )

    st.title("🔍 IPL Player Stats Filter - Filter Page")
    st.markdown("Use the sidebar to filter players by team, role, and performance metrics.")
    st.markdown("---")

    # -------------------------------
    # Load Data
    # -------------------------------
    df = load_ipl_data(DATA_FILE)

    # -------------------------------
    # Sidebar Filters
    # -------------------------------
    st.sidebar.header("Filters")

    teams = sorted(df["TEAM"].dropna().unique())
    selected_team = st.sidebar.selectbox("Select Team", ["All"] + teams)

    roles = sorted(df["Paying_Role"].dropna().unique())
    selected_role = st.sidebar.selectbox("Select Role", ["All"] + roles)

    min_avg = st.sidebar.slider("Minimum Batting Average", 0.0, 100.0, 0.0)
    min_sr = st.sidebar.slider("Minimum Strike Rate", 0.0, 300.0, 0.0)
    min_runs = st.sidebar.number_input("Minimum Runs", min_value=0, value=0)
    min_wickets = st.sidebar.number_input("Minimum Wickets", min_value=0, value=0)

    # -------------------------------
    # Apply Filters
    # -------------------------------
    team_filter = None if selected_team == "All" else selected_team
    role_filter = None if selected_role == "All" else selected_role

    filtered_df = filter_players(
        df,
        team=team_filter,
        role=role_filter,
        min_avg=min_avg,
        min_sr=min_sr,
        min_runs=min_runs,
        min_wickets=min_wickets
    )

    st.write(f"### Filtered Players: {filtered_df.shape[0]} found")

    # -------------------------------
    # Sort Option
    # -------------------------------
    sort_option = st.sidebar.selectbox("Sort by", ["None", "Runs", "B_Wkts", "Avg", "SR", "SOLD_PRICE"])
    if sort_option != "None":
        filtered_df = filtered_df.sort_values(by=sort_option, ascending=False)

    # -------------------------------
    # Display Player Cards with Robust Image Handling
    # -------------------------------
    if not filtered_df.empty:
        player_objects = [Player(row, IMAGE_FOLDER) for _, row in filtered_df.head(12).iterrows()]
        cols = st.columns(3)  # 3 cards per row

        for idx, player in enumerate(player_objects):
            col = cols[idx % 3]
            with col:
                if player.image_path:
                    try:
                        # Attempt to open with PIL to verify image
                        with Image.open(player.image_path) as img:
                            img.verify()  # Raises exception if corrupt
                        st.image(player.image_path, width=150)
                    except Exception:
                        st.image("https://via.placeholder.com/150x150.png?text=No+Image", width=150)
                else:
                    st.image("https://via.placeholder.com/150x150.png?text=No+Image", width=150)

                st.subheader(player.name)
                st.write(f"**Team:** {player.team}")
                st.write(f"**Role:** {player.role}")
                st.write(f"**Runs:** {player.runs} | **Wickets:** {player.b_wkts}")
                st.write(f"**Avg:** {player.avg} | **SR:** {player.sr}")
    else:
        st.warning("No players match the selected filters.")
