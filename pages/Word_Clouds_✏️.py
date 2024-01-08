import streamlit as st

word_cloud = st.header("Word Clouds")

st.image("./images/word-cloud-2016.png", caption="Generated From 2016-2019 Posts")
st.image("./images/word-cloud-2020.png", caption="Generated From 2020-2023 Posts")
st.image("./images/word-cloud-negative.png", caption="Generated From Negative Sentiment Posts")
st.image("./images/word-cloud-positive.png", caption="Generated From Positive Sentiment Posts")