import streamlit as st
import pandas as pd


def show_bar_chart(data):

    df = pd.DataFrame(data)

    st.bar_chart(df)