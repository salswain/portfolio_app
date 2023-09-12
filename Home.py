import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Salvatore Swain")
    content = """
    Hi, I am Salvatore! I am an Artist, Engineer & Entrepreneur from New Jersey! I have been 
    coding since high school and have been fascinated with the intersection of Art, Data, Science, Medicine, 
    & how Technology can provide innovative solutions for all those categories. """
    st.info(content)

content = """
As you can see, my portfolio is filled with diverse technological projects!
"""
st.write(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")