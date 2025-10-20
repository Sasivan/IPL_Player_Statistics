import os
import sys
import PIL
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
    player_objects = [Player(row, IMAGE_FOLDER) for _, row in df.iterrows()]

    # -------------------------------
    # Search Bar (Centered)
    # -------------------------------
    st.markdown("<h5 style='text-align:center;'>🔍 Search for a Player</h5>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        player_names = sorted([p.name for p in player_objects])
        selected_name = st.selectbox("Select Player", [""] + player_names, label_visibility="collapsed")

    # -------------------------------
    # Show Selected Player Details
    # -------------------------------
    if selected_name:
        st.markdown("---")
        st.subheader(f"📋 Player Details: {selected_name}")

        selected_player = next((p for p in player_objects if p.name == selected_name), None)
        if selected_player:
            left, right = st.columns([1, 2])

            # Left: Big Image
            with left:
                try:
                    if selected_player.image_path and os.path.exists(selected_player.image_path):
                        st.image(selected_player.image_path, width=350)
                    else:
                        st.image("https://via.placeholder.com/350x350.png?text=No+Image", width=350)
                except PIL.UnidentifiedImageError:
                    st.image("https://via.placeholder.com/350x350.png?text=Invalid+Image", width=350)

            # Right: Filtered Stats
            with right:
                st.markdown("""
                    <style>
                        .stats-box {
                            background-color: #1e1e1e;
                            border-radius: 15px;
                            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
                            width: 90%;
                            margin: auto;
                            color: white;
                            text-align: center;
                        }
                        .stats-box h3 {
                            margin-bottom: 15px;
                            color: #FFD700;
                        }
                        .stat-row {
                            padding: 10px 0;
                            border-radius: 8px;
                            font-size: 16px;
                            text-align: center;
                        }
                        .stat-row:nth-child(odd) {
                            background-color: rgba(255,255,255,0.05);
                        }
                        .stat-row:nth-child(even) {
                            background-color: rgba(255,255,255,0.1);
                        }
                    </style>

                    <div class="stats-box">
                        <h3>📊 Player Stats</h3>
                """, unsafe_allow_html=True)

                stats = selected_player.__dict__
                for key, value in stats.items():
                    if key not in ["image_path"] and value not in [0, None, "", "0"]:
                        st.markdown(
                            f"<div class='stat-row'><b>{key.replace('_', ' ').title()}:</b> {value}</div>",
                            unsafe_allow_html=True,
                        )

                st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------
    # Display Player Cards (Random on top)
    # -------------------------------
    st.markdown("---")
    st.subheader("Featured Players")
    sample_players = random.sample(player_objects, 6)
    cols = st.columns(3)
    for idx, player in enumerate(sample_players):
        col = cols[idx % 3]
        with col:
            try:
                if player.image_path and os.path.exists(player.image_path):
                    st.image(player.image_path, width=200)
                else:
                    st.image("https://via.placeholder.com/200x200.png?text=No+Image", width=200)
            except PIL.UnidentifiedImageError:
                st.image("https://via.placeholder.com/200x200.png?text=Invalid+Image", width=200)

            st.subheader(player.name)
            st.write(f"**Team:** {player.team}")
            st.write(f"**Runs:** {player.runs} | **Wickets:** {player.b_wkts}")
            st.write(f"**Strike Rate:** {player.sr} | **Average:** {player.avg}")
