import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

@st.cache_data
def gerar_df():
    df = pd.read_excel(
        io = "database_anp.xlsx",
        engine= "openpyxl",
        sheet_name="Planilha1",
        usecols="A:Q",
        nrows=21583
    )
    return df
df = gerar_df()
