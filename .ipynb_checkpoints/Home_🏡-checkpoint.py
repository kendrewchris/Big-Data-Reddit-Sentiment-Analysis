import pandas as pd
import streamlit as st
import mysql.connector

# Verbose version
db_connection = mysql.connector.connect(user="group6", password="1234")
db_cursor = db_connection.cursor()
db_cursor.execute("USE cs179g;")

st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=78)

st.title("Reddit Political Sentiment Analysis")

st.write(
    """<p style="color:#9c9d9f">
    Welcome to our final project in Computer Science 👋 
    This web app shows the expoloratory data analysis
    we conducted on over 1GB of Reddit submission data scraped using the Reddit API</p>
    """, unsafe_allow_html=True,
)

st.subheader("| Keyword Search")
st.write(
    """<p style="color:#9c9d9f">
    Select a keyword and the visualization you would like to view:
    </p>
    """, unsafe_allow_html=True,
)
keyword = st.selectbox(
    label = "Select Keyword",
    options = ["Trump", "Biden", "covid", "affirmative action", "loans", "abortion", "Supreme Court", "Ukraine", "Russia"]
    )

st.caption(f'You selected: {keyword}')

if keyword == 'Trump':
    db_cursor.execute("FLUSH TABLES;")
    db_cursor.execute("SELECT * FROM party_sentiment_counts LIMIT 5;")
    rows = db_cursor.fetchall()
    df = pd.DataFrame(rows)
    df.columns = ['positive count', 'negative count', 'keyword']
    #st.dataframe(df)
    st.bar_chart(df, )



st.subheader("| Github")
st.write(
    '<p style="color:#9c9d9f">Visit <a href="https://github.com/kendrewchris/Reddit-Political-Sentiment-Analysis-Web-App">GitHub</a></p><br>',
    unsafe_allow_html=True,
)



