import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

st.set_page_config(layout="wide")

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

colunasUteis = ['MÊS','PRODUTO','REGIÃO','ESTADO','PREÇO MÉDIO REVENDA']
df = df[colunasUteis]

with st.sidebar
    st.sidebar('PRODUTIVIDADE 1000%')
    logo_teste = Image.open('logo_br_distribuidora.png')
    st.image(logo_teste,use_column_width=True)
    st.subheader('SELEÇÃO DE FILTROS')
    fProduto = st.selectbox(
        "Selecione o combustivel"
        options=df['Produto'].unique()
    )

    fEstado = st.selectbox(
        'Selecione o Estado',
        options=df['Estado'].unique()
    )

    dadosUsuarios = df.loc[(
        df['PRODUTO'] == fProduto) &
        (df['ESTADO'] == fEstado)
    ]
    
updateDatas = dadosUsuarios['MÊS'].dt.strftime('%Y/%b')
dadosUsuarios['MÊS'] = updateDatas[0:]

st.header('PREÇOS DOS COMBUSTÍVEIS NO BRASIL: 2013 À 2024')
st.markdown('**Combustível selecionado** ' + fProduto)
st.markdown('**Estado:** ' + fEstado)

grafCombEstado = alt.Chart(dadosUsuarios).mark_line(
    point=alt.OverlayMarkDef(color='red', size=20)
).encode(
    x = 'MÊS:T',
    y = 'PREÇO MÉDIO REVENDA',
    strokeWidth=alt.value(3)    
).properties(
    height = 700,
    width = 1500
)

st.altair_chart(grafCombEstado)


