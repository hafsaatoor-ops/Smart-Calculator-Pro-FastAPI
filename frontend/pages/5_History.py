import streamlit as st
import pandas as pd
from services.api import (
    get_history,
    delete_history,
    export_csv
)

from utils.auth import require_login

require_login()

st.set_page_config(
    page_title="History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Calculation History")

search = st.text_input("🔍 Search Operation")

col1, col2 = st.columns([1, 1])

with col1:
    page = st.number_input(
        "Page",
        min_value=1,
        value=1,
        step=1
    )

with col2:
    limit = st.selectbox(
        "Records Per Page",
        [5, 10, 20, 50],
        index=1
    )

response = get_history(
    page=page,
    limit=limit,
    search=search
)

if response.status_code == 200:

    history = response.json()

    if len(history) == 0:

        st.info("No calculations found.")

    else:

        df = pd.DataFrame(history)

        st.dataframe(
            df,
            use_container_width=True
        )

        st.divider()

        st.subheader("🗑 Delete History")

        ids = [item["id"] for item in history]

        selected = st.selectbox(
            "Select History ID",
            ids
        )

        if st.button(
            "Delete",
            key="delete_history_btn"
        ):

            delete_response = delete_history(
                selected
            )

            if delete_response.status_code == 200:

                st.success(
                    "History deleted successfully."
                )

                st.rerun()

            else:

                st.error(
                    "Unable to delete history."
                )

else:

    st.error("Unable to load history.")


st.divider()

st.subheader("📥 Export History")

if st.button(
    "Download CSV",
    key="download_csv"
):

    response = export_csv()

    if response.status_code == 200:

        st.download_button(
            label="⬇️ Click Here To Download",
            data=response.content,
            file_name="history.csv",
            mime="text/csv"
        )

    else:

        st.error("Unable to export history.")      