import streamlit as st
def run():
    # -------------------------------
    # Page Configuration
    # -------------------------------
    st.set_page_config(
        page_title="About IPL Stats Filter",
        page_icon="ℹ️",
        layout="centered"
    )

    # -------------------------------
    # Project Title & Description
    # -------------------------------
    st.title("ℹ️ About IPL Player Stats Filter - Group 13")
    st.markdown("""
    This project allows users to explore IPL player statistics with filtering, comparison, and visualizations.  
    It provides insights into player performance and team performance over seasons.
    """)
    st.markdown("---")

    # -------------------------------
    # Team Members
    # -------------------------------
    st.subheader("👥 Team Members")
    st.markdown("""
    - Member 1: Your Name  
    - Member 2: Your Name  
    - Member 3: Your Name  
    - Member 4: Your Name  
    - Member 5: Your Name  
    """)

    # -------------------------------
    # Mentor
    # -------------------------------
    st.subheader("🧑‍🏫 Mentor")
    st.markdown("Dr./Mr./Ms. Mentor Name")

    # -------------------------------
    # Dataset Credits
    # -------------------------------
    st.subheader("📊 Dataset Credits")
    st.markdown("""
    - IPL Player Stats dataset obtained from [Kaggle IPL Dataset](https://www.kaggle.com/datasets/your-dataset-link)  
    - Images sourced from official IPL teams & players websites  
    """)

    # -------------------------------
    # Optional Footer / Banner
    # -------------------------------
    st.markdown("---")
    st.markdown("© 2025 Group 13 | IPL Player Stats Filter Project")
