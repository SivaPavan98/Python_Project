import streamlit as st
import pandas

st.set_page_config(layout= "wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width = 600)

with col2:
    st.title("TO DO APP")

    content =""" This is TO DO Application created by Siva."""
    st.info(content)

content2 = """Below you can find some apps I have built in python. Feel free to contact me...!"""

st.info(content2)
col3, empty_col, col4 = st.columns([2,0.3,2])

df = pandas.read_csv("data.csv", sep=";")

with col3 :
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.markdown(f"[{row['title']}]({row['url']})")

with col4 :
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row ["image"])
        st.markdown(f"[{row['title']}]({row['url']})")

