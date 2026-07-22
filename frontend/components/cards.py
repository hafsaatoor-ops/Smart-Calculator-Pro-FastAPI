import streamlit as st


def stat_card(title, value):

    st.markdown(
        f"""
        <div style="
        background:#ffffff;
        padding:20px;
        border-radius:15px;
        box-shadow:0px 3px 10px rgba(0,0,0,.15);
        text-align:center;
        margin-bottom:15px;
        ">

        <h4>{title}</h4>

        <h2 style="color:#0066FF;">
        {value}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

st.subheader("⚡ Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("🧮 Calculator"):

        st.switch_page(
            "pages/4_Calculator.py"
        )

with col2:

    if st.button("📜 History"):

        st.switch_page(
            "pages/5_History.py"
        )

with col3:

    if st.button("👤 Profile"):

        st.switch_page(
            "pages/6_Profile.py"
        )