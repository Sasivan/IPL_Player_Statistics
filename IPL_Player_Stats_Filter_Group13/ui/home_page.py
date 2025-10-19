import os
import sys
import streamlit as st
import random
def run():
    # -------------------------------
    # Add project root dynamically
    # -------------------------------
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
    from backend.data_loader import load_ipl_data
    from backend.player_model import Player
    # -------------------------------
    # Paths
    # -------------------------------
    DATA_FILE = os.path.join(PROJECT_ROOT, "data", "ipl_player_stats_clean.csv")
    IMAGE_FOLDER = os.path.join(PROJECT_ROOT, "player_images")

    # -------------------------------
    # Page config
    # -------------------------------
    st.set_page_config(page_title="IPL Player Stats Filter", page_icon="🏏", layout="wide")


    # -------------------------------
    # Banner & Title
    # -------------------------------
    st.title("🏏 IPL Player Stats Filter - Group 13")
    st.markdown("<h4 style='text-align: center; color: gray;'>Explore IPL Players with Stats and Images</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # -------------------------------
    # Load Data & Players
    # -------------------------------
    df = load_ipl_data(DATA_FILE)
    top_players = df.head(6)
    player_objects = [Player(row, IMAGE_FOLDER) for _, row in top_players.iterrows()]

    # -------------------------------
    # Display Player Cards
    # -------------------------------
    cols = st.columns(3)  # 3 cards per row
    for idx, player in enumerate(player_objects):
        col = cols[idx % 3]
        with col:
            if player.image_path and os.path.exists(player.image_path):
                st.image(player.image_path, width=200)
            else:
                st.image("https://via.placeholder.com/200x200.png?text=No+Image", width=200)
            
            st.subheader(player.name)
            st.write(f"**Team:** {player.team}")
            st.write(f"**Runs:** {player.runs} | **Wickets:** {player.b_wkts}")
            st.write(f"**Strike Rate:** {player.sr} | **Average:** {player.avg}")
