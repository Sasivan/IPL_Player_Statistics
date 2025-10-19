import streamlit as st
from ui import home_page, player_filter, player_compare, visualization, about_page

# -------------------------------
# Navbar (HTML)
# -------------------------------
st.markdown("""
<style>
.nav-bar {
    display: flex;
    justify-content: center;
    background-color: #1e1e1e;
    padding: 12px;
    border-radius: 8px;
    margin-bottom: 20px;
}
.nav-item {
    color: white;
    margin: 0 15px;
    text-decoration: none;
    font-weight: bold;
    font-size: 16px;
}
.nav-item:hover {
    color: #00c4ff;
    text-decoration: underline;
}
.active {
    color: #00c4ff;
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Page Query Handling (Modern API)
# -------------------------------
# Get current page
page = st.query_params.get("page", "Home")

# Navbar links with active highlighting
def nav_link(label, page_name, icon):
    active_class = "active" if page == page_name else ""
    return f'<a class="nav-item {active_class}" href="?page={page_name}">{icon} {label}</a>'

st.markdown(
    f"""
    <div class="nav-bar">
        {nav_link("Home", "Home", "🏠")}
        {nav_link("Filter", "Filter", "🔍")}
        {nav_link("Compare", "Compare", "📊")}
        {nav_link("Visualize", "Visualization", "📈")}
        {nav_link("About", "About", "ℹ️")}
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Page Routing
# -------------------------------
if page == "Home":
    home_page.run()
elif page == "Filter":
    player_filter.run()
elif page == "Compare":
    player_compare.run()
elif page == "Visualization":
    visualization.run()
elif page == "About":
    about_page.run()
else:
    st.error("❌ Page not found.")
