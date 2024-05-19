import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2= st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Elias Tamer")
    content= """
    Software Engineer focused on building products with extra attention to detail. \n
    With over 5 years in the tech industry, I specialize in React,
    Next.js, TypeScript, and Node.js.
    Passionate about crafting efficient solutions
    and delivering top-notch user experiences.
    """
    st.info(content)


content2 = """ Below you can find some of the apps i have built in Python.
    Feel free to contact me!
    """

st.write(content2)


col3, empty_col,col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[SourceCode]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[SourceCode]({row['url']})")