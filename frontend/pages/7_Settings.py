import streamlit as st

from utils.auth import require_login

require_login()

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Settings")

st.markdown("## Application Settings")

theme = st.radio(
    "Choose Theme",
    ["Light", "Dark"]
)

notifications = st.checkbox(
    "Enable Notifications",
    value=True
)

balloons = st.checkbox(
    "Show Balloons After Calculation",
    value=True
)

if st.button("💾 Save Settings", key="save_settings"):
    st.success("Settings saved successfully ✅")