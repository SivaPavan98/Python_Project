import streamlit as st
import pandas
st.set_page_config(layout= 'wide')
st.title("The Best Company")
content = """TBC delivers innovative, customer-focused solutions in industry. We combine advanced technology, expert insight, and a commitment to quality to drive real impact. Our mission is to solve complex challenges, create value, and empower businesses to thrive in a rapidly changing world."""
st.info(content)
st.subheader("Our Team")

first_Col, Empty_Col_1, Second_Col,Empty_Col_2,Third_Col, Empty_Col_3 = st.columns([1,0.5,1,0.5,1,0.5])
df=pandas.read_csv("data.csv")

with first_Col:
    for index, row in df[0:4].iterrows():
        st.subheader(f'{row["first name"].capitalize()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/"+ row["image"])

with Second_Col:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with Third_Col:
    for index, row in df[8:12].iterrows():
        st.subheader(row['first name'].capitalize()+" "+row['last name'].capitalize())
        st.write(row["role"])
        st.image("images/"+ row["image"])

