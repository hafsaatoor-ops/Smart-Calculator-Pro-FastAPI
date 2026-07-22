import streamlit as st

from utils.auth import require_login
from services.api import statistics
from components.cards import stat_card

require_login()

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard")

st.caption("Welcome to Smart Calculator Pro")

user = st.session_state.get("user")

if user:
    st.success(f"Welcome {user['full_name']} 👋")

response = statistics()

if response.status_code == 200:

    data = response.json()

    col1, col2 = st.columns(2)

    with col1:

        stat_card(
            "📊 Total Calculations",
            data["total_calculations"]
        )

        stat_card(
            "⭐ Average Result",
            round(data["average_result"], 2)
        )

    with col2:

        stat_card(
            "📅 Today's Calculations",
            data["today_calculations"]
        )

        stat_card(
            "🔥 Most Used Operation",
            data["most_used_operation"]
        )

    st.divider()

    st.subheader("⚡ Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("🧮 Calculator", key="dashboard_calculator"):
            st.switch_page("pages/4_Calculator.py")

    with col2:

        if st.button("📜 History", key="dashboard_history"):
            st.switch_page("pages/5_History.py")

    with col3:

        if st.button("👤 Profile", key="dashboard_profile"):
            st.switch_page("pages/6_Profile.py")

else:

    st.error("Statistics could not be loaded.")