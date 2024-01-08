import pandas as pd
import streamlit as st
import mysql.connector
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

# Establish connection
db_connection = mysql.connector.connect(user="group6", password="1234")
db_cursor = db_connection.cursor()
db_cursor.execute("USE cs179g;")

db_cursor.execute("FLUSH TABLES;")
db_cursor.execute("SELECT * FROM master_table;")
rows = db_cursor.fetchall()
df = pd.DataFrame(rows)

# Create a DataFrame from the fetched data
df = pd.DataFrame(rows, columns=["keyword", "negative", "positive", "twenty_fifteen", "twenty_sixteen", "twenty_seventeen", \
                                 "twenty_eighteen", "twenty_nineteen", "twenty_twenty", "twenty_twenty_one", "twenty_twenty_two", \
                                 "twenty_twenty_three", "zero", "one_hundred", "five_hundred", "fifteen_hundred", "total"])

st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=78)

st.title("Reddit Political Sentiment Analysis")

st.write(
    """<p style="color:#9c9d9f">
    Welcome to our final project in Computer Science 👋 
    This web app shows the expoloratory data analysis
    we conducted on over 1GB of Reddit submission data scraped using the Reddit API</p>
    """, unsafe_allow_html=True,
)

st.subheader("| Our MySQL Data")
# print out dataframe made from sql table values
st.dataframe(df)

st.subheader("| Keyword Search")
st.write(
    """<p style="color:#9c9d9f">
    Select a keyword and the visualization you would like to view:
    </p>
    """, unsafe_allow_html=True,
)
keyword = st.selectbox(
    label = "Select Keyword",
    options = ["Trump", "Biden", "COVID", "Loans", "Democrat", "Republican", "Ukraine", "Russia", "China", "Congress"]
    )

st.caption(f'You selected: {keyword}')
word_cloud = st.header("Word Cloud")
if keyword == 'Trump':
    db_cursor.execute("SELECT * FROM master_table WHERE keyword = 'trump';")
    rows = db_cursor.fetchall()
    df_trump = pd.DataFrame(rows)
    df_trump = pd.DataFrame(rows, columns=["keyword", "negative", "positive", "twenty_fifteen", "twenty_sixteen", "twenty_seventeen", \
                                 "twenty_eighteen", "twenty_nineteen", "twenty_twenty", "twenty_twenty_one", "twenty_twenty_two", \
                                 "twenty_twenty_three", "zero", "one_hundred", "five_hundred", "fifteen_hundred", "total"])

    st.image("/home/ubuntu/Reddit-Political-Sentiment-Analysis-Web-App/wordcloud_images/wordcloud_trump.png", caption="Generated From Posts Containing Trump")


    # Bar graph for keywords vs positive/negative sentiment
    df_sentiments = pd.DataFrame({
    'Sentiment of Posts Containing Trump': ['Positive', 'Negative'],
    'Posts': [df_trump['positive'].iloc[0], df_trump['negative'].iloc[0]]
    })

    # Set the index to 'Sentiment of Posts Containing Trump' for a custom x-axis label
    df_sentiments.set_index('Sentiment of Posts Containing Trump', inplace=True)

    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments.plot(kind='bar', ax=ax, legend=False)
    
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')

    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)

    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #-----------------------------------------------------------------------------------------------
    # Graph number of posts each year for keyword
    df_sentiments2 = pd.DataFrame({
    'Posts Containing Trump Over Time': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    'Number of Posts': [df_trump['twenty_fifteen'].iloc[0], df_trump['twenty_sixteen'].iloc[0], df_trump['twenty_seventeen'].iloc[0], df_trump['twenty_eighteen'].iloc[0], df_trump['twenty_nineteen'].iloc[0], df_trump['twenty_twenty'].iloc[0],df_trump['twenty_twenty_one'].iloc[0],df_trump['twenty_twenty_two'].iloc[0],df_trump['twenty_twenty_three'].iloc[0]]
    })

    # Set the index to 'Years' for a custom x-axis label
    df_sentiments2.set_index('Posts Containing Trump Over Time', inplace=True)

    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments2.plot(kind='bar', ax=ax, legend=False)
    
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')

    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)

    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #----------------------------------------------------------------------------------------------
    # Percentage of posts for keyword at various upvote ranges
    df_sentiments3 = pd.DataFrame({
    'Posts Containing Trump at Various Upvote Ranges': ['0-99', '100-499', '500-1499', '1500+'],
    'Number of Posts': [df_trump['zero'].iloc[0], df_trump['one_hundred'].iloc[0], df_trump['five_hundred'].iloc[0], df_trump['fifteen_hundred'].iloc[0]]
    })

    # Set the index to 'Posts Containing Trump at Various Upvote Ranges' for a custom x-axis label
    df_sentiments3.set_index('Posts Containing Trump at Various Upvote Ranges', inplace=True)

    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments3.plot(kind='bar', ax=ax, legend=False)
    
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')

    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)

    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
     #----------------------------------------------------------------------------------------------
     #Create and display wordcloud

elif keyword == 'Biden':
    db_cursor.execute("SELECT * FROM master_table WHERE keyword = 'biden';")
    rows = db_cursor.fetchall()
    df_biden = pd.DataFrame(rows)
    df_biden = pd.DataFrame(rows, columns=["keyword", "negative", "positive", "twenty_fifteen", "twenty_sixteen", "twenty_seventeen", \
                                 "twenty_eighteen", "twenty_nineteen", "twenty_twenty", "twenty_twenty_one", "twenty_twenty_two", \
                                 "twenty_twenty_three", "zero", "one_hundred", "five_hundred", "fifteen_hundred", "total"])

    st.image("/home/ubuntu/Reddit-Political-Sentiment-Analysis-Web-App/wordcloud_images/wordcloud_biden.png", caption="Generated From Posts Containing Biden")


    # Bar graph for keywords vs positive/negative sentiment
    df_sentiments = pd.DataFrame({
    'Sentiment of Posts Containing Biden': [
'Positive', 'Negative'],
    'Posts': [df_biden['positive'].iloc[0], df_biden['negative'].iloc[0]]})


    # Set the index to 'Sentiment of Posts Containing Biden' for a custom x-axis label
    df_sentiments.set_index('Sentiment of Posts Containing Biden', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #-----------------------------------------------------------------------------------------------
    # Graph number of posts each year for keyword
    df_sentiments2 = pd.DataFrame({
    'Posts Containing Biden Over Time': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    'Number of Posts': [df_biden['twenty_fifteen'].iloc[0], df_biden['twenty_sixteen'].iloc[0], df_biden['twenty_seventeen'].iloc[0], df_biden['twenty_eighteen'].iloc[0], df_biden['twenty_nineteen'].iloc[0], df_biden['twenty_twenty'].iloc[0],df_biden['twenty_twenty_one'].iloc[0],df_biden['twenty_twenty_two'].iloc[0],df_biden['twenty_twenty_three'].iloc[0]]
    })


    # Set the index to 'Years' for a custom x-axis label
    df_sentiments2.set_index('Posts Containing Biden Over Time', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments2.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #----------------------------------------------------------------------------------------------
    # Percentage of posts for keyword at various upvote ranges
    df_sentiments3 = pd.DataFrame({
    'Posts Containing Biden at Various Upvote Ranges': ['0-99', '100-499', '500-1499', '1500+'],
    'Number of Posts': [df_biden['zero'].iloc[0], df_biden['one_hundred'].iloc[0], df_biden['five_hundred'].iloc[0], df_biden['fifteen_hundred'].iloc[0]]
    })


    # Set the index to 'Posts Containing Biden at Various Upvote Ranges' for a custom x-axis label
    df_sentiments3.set_index('Posts Containing Biden at Various Upvote Ranges', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments3.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)


elif keyword == 'Loans':
    db_cursor.execute("SELECT * FROM master_table WHERE keyword = 'loans';")
    rows = db_cursor.fetchall()
    df_loans = pd.DataFrame(rows)
    

    st.image("/home/ubuntu/Reddit-Political-Sentiment-Analysis-Web-App/wordcloud_images/wordcloud_loans.png", caption="Generated From Posts Containing Loans")

    df_loans = pd.DataFrame(rows, columns=["keyword", "negative", "positive", "twenty_fifteen", "twenty_sixteen", "twenty_seventeen", \
                                 "twenty_eighteen", "twenty_nineteen", "twenty_twenty", "twenty_twenty_one", "twenty_twenty_two", \
                                 "twenty_twenty_three", "zero", "one_hundred", "five_hundred", "fifteen_hundred", "total"])

    # Bar graph for keywords vs positive/negative sentiment
    df_sentiments = pd.DataFrame({
    'Sentiment of Posts Containing Loans': [
'Positive', 'Negative'],
    'Posts': [df_loans['positive'].iloc[0], df_loans['negative'].iloc[0]]})


    # Set the index to 'Sentiment of Posts Containing Loans' for a custom x-axis label
    df_sentiments.set_index('Sentiment of Posts Containing Loans', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #-----------------------------------------------------------------------------------------------
    # Graph number of posts each year for keyword
    df_sentiments2 = pd.DataFrame({
    'Posts Containing Loans Over Time': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    'Number of Posts': [df_loans['twenty_fifteen'].iloc[0], df_loans['twenty_sixteen'].iloc[0], \
                        df_loans['twenty_seventeen'].iloc[0], df_loans['twenty_eighteen'].iloc[0], \
                        df_loans['twenty_nineteen'].iloc[0], df_loans['twenty_twenty'].iloc[0], \
                        df_loans['twenty_twenty_one'].iloc[0],df_loans['twenty_twenty_two'].iloc[0], df_loans['twenty_twenty_three'].iloc[0]]
    })


    # Set the index to 'Years' for a custom x-axis label
    df_sentiments2.set_index('Posts Containing Loans Over Time', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments2.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #----------------------------------------------------------------------------------------------
    # Percentage of posts for keyword at various upvote ranges
    df_sentiments3 = pd.DataFrame({
    'Posts Containing Loans at Various Upvote Ranges': ['0-99', '100-499', '500-1499', '1500+'],
    'Number of Posts': [df_loans['zero'].iloc[0], df_loans['one_hundred'].iloc[0], \
                        df_loans['five_hundred'].iloc[0], df_loans['fifteen_hundred'].iloc[0]]
    })


    # Set the index to 'Posts Containing Loans at Various Upvote Ranges' for a custom x-axis label
    df_sentiments3.set_index('Posts Containing Loans at Various Upvote Ranges', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments3.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)


elif keyword == 'COVID':
    db_cursor.execute("SELECT * FROM master_table WHERE keyword = 'covid';")
    rows = db_cursor.fetchall()
    df_covid = pd.DataFrame(rows)
    
    df_covid = pd.DataFrame(rows, columns=["keyword", "negative", "positive", "twenty_fifteen", "twenty_sixteen", "twenty_seventeen", \
                                 "twenty_eighteen", "twenty_nineteen", "twenty_twenty", "twenty_twenty_one", "twenty_twenty_two", \
                                 "twenty_twenty_three", "zero", "one_hundred", "five_hundred", "fifteen_hundred", "total"])

    st.image("/home/ubuntu/Reddit-Political-Sentiment-Analysis-Web-App/wordcloud_images/wordcloud_covid.png", caption="Generated From Posts Containing COVID")

    # Display the filtered DataFrame using Streamlit
    # Bar graph for keywords vs positive/negative sentiment
    df_sentiments = pd.DataFrame({
    'Sentiment of Posts Containing Covid': ['Positive', 'Negative'],
    'Posts': [df_covid['positive'].iloc[0], df_covid['negative'].iloc[0]]
    })


    # Set the index to 'Sentiment of Posts Containing Covid' for a custom x-axis label
    df_sentiments.set_index('Sentiment of Posts Containing Covid', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #-----------------------------------------------------------------------------------------------
    # Graph number of posts each year for keyword
    df_sentiments2 = pd.DataFrame({
    'Posts Containing Covid Over Time': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    'Number of Posts': [df_covid['twenty_fifteen'].iloc[0], df_covid['twenty_sixteen'].iloc[0], df_covid['twenty_seventeen'].iloc[0], \
                        df_covid['twenty_eighteen'].iloc[0], df_covid['twenty_nineteen'].iloc[0], df_covid['twenty_twenty'].iloc[0], \
                        df_covid['twenty_twenty_one'].iloc[0],df_covid['twenty_twenty_two'].iloc[0],df_covid['twenty_twenty_three'].iloc[0]]
    })


    # Set the index to 'Years' for a custom x-axis label
    df_sentiments2.set_index('Posts Containing Covid Over Time', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments2.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #----------------------------------------------------------------------------------------------
    # Percentage of posts for keyword at various upvote ranges
    df_sentiments3 = pd.DataFrame({
    'Posts Containing Covid at Various Upvote Ranges': ['0-99', '100-499', '500-1499', '1500+'],
    'Number of Posts': [df_covid['zero'].iloc[0], df_covid['one_hundred'].iloc[0], df_covid['five_hundred'].iloc[0], df_covid['fifteen_hundred'].iloc[0]]
    })


    # Set the index to 'Posts Containing Covid at Various Upvote Ranges' for a custom x-axis label
    df_sentiments3.set_index('Posts Containing Covid at Various Upvote Ranges', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments3.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)


elif keyword == 'Congress':
    db_cursor.execute("SELECT * FROM master_table WHERE keyword = 'congress';")
    rows = db_cursor.fetchall()
    df_congress = pd.DataFrame(rows)
    df_congress = pd.DataFrame(rows, columns=["keyword", "negative", "positive", "twenty_fifteen", "twenty_sixteen", "twenty_seventeen", \
                                 "twenty_eighteen", "twenty_nineteen", "twenty_twenty", "twenty_twenty_one", "twenty_twenty_two", \
                                 "twenty_twenty_three", "zero", "one_hundred", "five_hundred", "fifteen_hundred", "total"])

    st.image("/home/ubuntu/Reddit-Political-Sentiment-Analysis-Web-App/wordcloud_images/wordcloud_congress.png", caption="Generated From Posts Containing Congress")

    # Bar graph for keywords vs positive/negative sentiment
    df_sentiments = pd.DataFrame({
    'Sentiment of Posts Containing Congress': ['Positive', 'Negative'],
    'Posts': [df_congress['positive'].iloc[0], df_congress['negative'].iloc[0]]
    })


    # Set the index to 'Sentiment of Posts Containing Congress' for a custom x-axis label
    df_sentiments.set_index('Sentiment of Posts Containing Congress', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #-----------------------------------------------------------------------------------------------
    # Graph number of posts each year for keyword
    df_sentiments2 = pd.DataFrame({
    'Posts Containing Congress Over Time': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    'Number of Posts': [df_congress['twenty_fifteen'].iloc[0], df_congress['twenty_sixteen'].iloc[0], df_congress['twenty_seventeen'].iloc[0], \
                        df_congress['twenty_eighteen'].iloc[0], df_congress['twenty_nineteen'].iloc[0], df_congress['twenty_twenty'].iloc[0], \
                        df_congress['twenty_twenty_one'].iloc[0],df_congress['twenty_twenty_two'].iloc[0],df_congress['twenty_twenty_three'].iloc[0]]
    })


    # Set the index to 'Years' for a custom x-axis label
    df_sentiments2.set_index('Posts Containing Congress Over Time', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments2.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #----------------------------------------------------------------------------------------------
    # Percentage of posts for keyword at various upvote ranges
    df_sentiments3 = pd.DataFrame({
    'Posts Containing Congress at Various Upvote Ranges': ['0-99', '100-499', '500-1499', '1500+'],
    'Number of Posts': [df_congress['zero'].iloc[0], df_congress['one_hundred'].iloc[0], df_congress['five_hundred'].iloc[0], df_congress['fifteen_hundred'].iloc[0]]
    })


    # Set the index to 'Posts Containing Congress at Various Upvote Ranges' for a custom x-axis label
    df_sentiments3.set_index('Posts Containing Congress at Various Upvote Ranges', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments3.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)

elif keyword == 'Russia':
    db_cursor.execute("SELECT * FROM master_table WHERE keyword = 'russia';")
    rows = db_cursor.fetchall()
    df_russia = pd.DataFrame(rows)
    df_russia = pd.DataFrame(rows, columns=["keyword", "negative", "positive", "twenty_fifteen", "twenty_sixteen", "twenty_seventeen", \
                                 "twenty_eighteen", "twenty_nineteen", "twenty_twenty", "twenty_twenty_one", "twenty_twenty_two", \
                                 "twenty_twenty_three", "zero", "one_hundred", "five_hundred", "fifteen_hundred", "total"])

    st.image("/home/ubuntu/Reddit-Political-Sentiment-Analysis-Web-App/wordcloud_images/wordcloud_russia.png", caption="Generated From Posts Containing Russia")

    # Bar graph for keywords vs positive/negative sentiment
    df_sentiments = pd.DataFrame({
    'Sentiment of Posts Containing Russia': ['Positive', 'Negative'],
    'Posts': [df_russia['positive'].iloc[0], df_russia['negative'].iloc[0]]
    })


    # Set the index to 'Sentiment of Posts Containing Russia' for a custom x-axis label
    df_sentiments.set_index('Sentiment of Posts Containing Russia', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #-----------------------------------------------------------------------------------------------
    # Graph number of posts each year for keyword
    df_sentiments2 = pd.DataFrame({
    'Posts Containing Russia Over Time': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    'Number of Posts': [df_russia['twenty_fifteen'].iloc[0], df_russia['twenty_sixteen'].iloc[0], df_russia['twenty_seventeen'].iloc[0], \
                        df_russia['twenty_eighteen'].iloc[0], df_russia['twenty_nineteen'].iloc[0], df_russia['twenty_twenty'].iloc[0], \
                        df_russia['twenty_twenty_one'].iloc[0],df_russia['twenty_twenty_two'].iloc[0],df_russia['twenty_twenty_three'].iloc[0]]
    })


    # Set the index to 'Years' for a custom x-axis label
    df_sentiments2.set_index('Posts Containing Russia Over Time', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments2.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #----------------------------------------------------------------------------------------------
    # Percentage of posts for keyword at various upvote ranges
    df_sentiments3 = pd.DataFrame({
    'Posts Containing Russia at Various Upvote Ranges': ['0-99', '100-499', '500-1499', '1500+'],
    'Number of Posts': [df_russia['zero'].iloc[0], df_russia['one_hundred'].iloc[0], df_russia['five_hundred'].iloc[0], df_russia['fifteen_hundred'].iloc[0]]
})


    # Set the index to 'Posts Containing Russia at Various Upvote Ranges' for a custom x-axis label
    df_sentiments3.set_index('Posts Containing Russia at Various Upvote Ranges', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments3.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)


elif keyword == 'Ukraine':
    db_cursor.execute("SELECT * FROM master_table WHERE keyword = 'ukraine';")
    rows = db_cursor.fetchall()
    df_ukraine = pd.DataFrame(rows)
    df_ukraine = pd.DataFrame(rows, columns=["keyword", "negative", "positive", "twenty_fifteen", "twenty_sixteen", "twenty_seventeen", \
                                 "twenty_eighteen", "twenty_nineteen", "twenty_twenty", "twenty_twenty_one", "twenty_twenty_two", \
                                 "twenty_twenty_three", "zero", "one_hundred", "five_hundred", "fifteen_hundred", "total"])

    st.image("/home/ubuntu/Reddit-Political-Sentiment-Analysis-Web-App/wordcloud_images/wordcloud_ukraine.png", caption="Generated From Posts Containing Ukraine")

    # Bar graph for keywords vs positive/negative sentiment
    df_sentiments = pd.DataFrame({
    'Sentiment of Posts Containing Ukraine': ['Positive', 'Negative'],
    'Posts': [df_ukraine['positive'].iloc[0], df_ukraine['negative'].iloc[0]]
    })


    # Set the index to 'Sentiment of Posts Containing Ukraine' for a custom x-axis label
    df_sentiments.set_index('Sentiment of Posts Containing Ukraine', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #-----------------------------------------------------------------------------------------------
    # Graph number of posts each year for keyword
    df_sentiments2 = pd.DataFrame({
    'Posts Containing Ukraine Over Time': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    'Number of Posts': [df_ukraine['twenty_fifteen'].iloc[0], df_ukraine['twenty_sixteen'].iloc[0], df_ukraine['twenty_seventeen'].iloc[0], \
                        df_ukraine['twenty_eighteen'].iloc[0], df_ukraine['twenty_nineteen'].iloc[0], df_ukraine['twenty_twenty'].iloc[0], \
                        df_ukraine['twenty_twenty_one'].iloc[0],df_ukraine['twenty_twenty_two'].iloc[0],df_ukraine['twenty_twenty_three'].iloc[0]]
    })


    # Set the index to 'Years' for a custom x-axis label
    df_sentiments2.set_index('Posts Containing Ukraine Over Time', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments2.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #----------------------------------------------------------------------------------------------
    # Percentage of posts for keyword at various upvote ranges
    df_sentiments3 = pd.DataFrame({
    'Posts Containing Ukraine at Various Upvote Ranges': ['0-99', '100-499', '500-1499', '1500+'],
    'Number of Posts': [df_ukraine['zero'].iloc[0], df_ukraine['one_hundred'].iloc[0], df_ukraine['five_hundred'].iloc[0], df_ukraine['fifteen_hundred'].iloc[0]]
    })


    # Set the index to 'Posts Containing Ukraine at Various Upvote Ranges' for a custom x-axis label
    df_sentiments3.set_index('Posts Containing Ukraine at Various Upvote Ranges', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments3.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)


elif keyword == 'China':
    db_cursor.execute("SELECT * FROM master_table WHERE keyword = 'china';")
    rows = db_cursor.fetchall()
    df_china = pd.DataFrame(rows)
    df_china = pd.DataFrame(rows, columns=["keyword", "negative", "positive", "twenty_fifteen", "twenty_sixteen", "twenty_seventeen", \
                                 "twenty_eighteen", "twenty_nineteen", "twenty_twenty", "twenty_twenty_one", "twenty_twenty_two", \
                                 "twenty_twenty_three", "zero", "one_hundred", "five_hundred", "fifteen_hundred", "total"])

    st.image("/home/ubuntu/Reddit-Political-Sentiment-Analysis-Web-App/wordcloud_images/wordcloud_china.png", caption="Generated From Posts Containing China")

    # Bar graph for keywords vs positive/negative sentiment
    df_sentiments = pd.DataFrame({
    'Sentiment of Posts Containing China': ['Positive', 'Negative'],
    'Posts': [df_china['positive'].iloc[0], df_china['negative'].iloc[0]]
    })


    # Set the index to 'Sentiment of Posts Containing China' for a custom x-axis label
    df_sentiments.set_index('Sentiment of Posts Containing China', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #-----------------------------------------------------------------------------------------------
    # Graph number of posts each year for keyword
    df_sentiments2 = pd.DataFrame({
    'Posts Containing China Over Time': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    'Number of Posts': [df_china['twenty_fifteen'].iloc[0], df_china['twenty_sixteen'].iloc[0], df_china['twenty_seventeen'].iloc[0], \
                        df_china['twenty_eighteen'].iloc[0], df_china['twenty_nineteen'].iloc[0], df_china['twenty_twenty'].iloc[0], \
                        df_china['twenty_twenty_one'].iloc[0],df_china['twenty_twenty_two'].iloc[0],df_china['twenty_twenty_three'].iloc[0]]
    })


    # Set the index to 'Years' for a custom x-axis label
    df_sentiments2.set_index('Posts Containing China Over Time', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments2.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #----------------------------------------------------------------------------------------------
    # Percentage of posts for keyword at various upvote ranges
    df_sentiments3 = pd.DataFrame({
    'Posts Containing China at Various Upvote Ranges': ['0-99', '100-499', '500-1499', '1500+'],
    'Number of Posts': [df_china['zero'].iloc[0], df_china['one_hundred'].iloc[0], df_china['five_hundred'].iloc[0], df_china['fifteen_hundred'].iloc[0]]
    })


    # Set the index to 'Posts Containing China at Various Upvote Ranges' for a custom x-axis label
    df_sentiments3.set_index('Posts Containing China at Various Upvote Ranges', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments3.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)


elif keyword == 'Democrat':
    db_cursor.execute("SELECT * FROM master_table WHERE keyword = 'democrat';")
    rows = db_cursor.fetchall()
    df_democrat = pd.DataFrame(rows)
    df_democrat = pd.DataFrame(rows, columns=["keyword", "negative", "positive", "twenty_fifteen", "twenty_sixteen", "twenty_seventeen", \
                                 "twenty_eighteen", "twenty_nineteen", "twenty_twenty", "twenty_twenty_one", "twenty_twenty_two", \
                                 "twenty_twenty_three", "zero", "one_hundred", "five_hundred", "fifteen_hundred", "total"])

    st.image("/home/ubuntu/Reddit-Political-Sentiment-Analysis-Web-App/wordcloud_images/wordcloud_democrat.png", caption="Generated From Posts Containing Democrat")

    # Bar graph for keywords vs positive/negative sentiment
    df_sentiments = pd.DataFrame({
    'Sentiment of Posts Containing Democrat': ['Positive', 'Negative'],
    'Posts': [df_democrat['positive'].iloc[0], df_democrat['negative'].iloc[0]]
    })


    # Set the index to 'Sentiment of Posts Containing Democrat' for a custom x-axis label
    df_sentiments.set_index('Sentiment of Posts Containing Democrat', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #-----------------------------------------------------------------------------------------------
    # Graph number of posts each year for keyword
    df_sentiments2 = pd.DataFrame({
    'Posts Containing Democrat Over Time': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    'Number of Posts': [df_democrat['twenty_fifteen'].iloc[0], df_democrat['twenty_sixteen'].iloc[0], df_democrat['twenty_seventeen'].iloc[0], \
                        df_democrat['twenty_eighteen'].iloc[0], df_democrat['twenty_nineteen'].iloc[0], df_democrat['twenty_twenty'].iloc[0], \
                        df_democrat['twenty_twenty_one'].iloc[0],df_democrat['twenty_twenty_two'].iloc[0],df_democrat['twenty_twenty_three'].iloc[0]]
    })


    # Set the index to 'Years' for a custom x-axis label
    df_sentiments2.set_index('Posts Containing Democrat Over Time', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments2.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #----------------------------------------------------------------------------------------------
    # Percentage of posts for keyword at various upvote ranges
    df_sentiments3 = pd.DataFrame({
    'Posts Containing Democrat at Various Upvote Ranges': ['0-99', '100-499', '500-1499', '1500+'],
    'Number of Posts': [df_democrat['zero'].iloc[0], df_democrat['one_hundred'].iloc[0], df_democrat['five_hundred'].iloc[0], df_democrat['fifteen_hundred'].iloc[0]]
    })


    # Set the index to 'Posts Containing Democrat at Various Upvote Ranges' for a custom x-axis label
    df_sentiments3.set_index('Posts Containing Democrat at Various Upvote Ranges', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments3.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)


elif keyword == 'Republican':
    db_cursor.execute("SELECT * FROM master_table WHERE keyword = 'republican';")
    rows = db_cursor.fetchall()
    df_republican = pd.DataFrame(rows)
    df_republican = pd.DataFrame(rows, columns=["keyword", "negative", "positive", "twenty_fifteen", "twenty_sixteen", "twenty_seventeen", \
                                 "twenty_eighteen", "twenty_nineteen", "twenty_twenty", "twenty_twenty_one", "twenty_twenty_two", \
                                 "twenty_twenty_three", "zero", "one_hundred", "five_hundred", "fifteen_hundred", "total"])

    st.image("/home/ubuntu/Reddit-Political-Sentiment-Analysis-Web-App/wordcloud_images/wordcloud_republican.png", caption="Generated From Posts Containing Republican")
    
    # Bar graph for keywords vs positive/negative sentiment
    df_sentiments = pd.DataFrame({
    'Sentiment of Posts Containing Republican': ['Positive', 'Negative'],
    'Posts': [df_republican['positive'].iloc[0], df_republican['negative'].iloc[0]]
    })


    # Set the index to 'Sentiment of Posts Containing Republican' for a custom x-axis label
    df_sentiments.set_index('Sentiment of Posts Containing Republican', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #-----------------------------------------------------------------------------------------------
    # Graph number of posts each year for keyword
    df_sentiments2 = pd.DataFrame({
    'Posts Containing Republican Over Time': ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    'Number of Posts': [df_republican['twenty_fifteen'].iloc[0], df_republican['twenty_sixteen'].iloc[0], df_republican['twenty_seventeen'].iloc[0], \
                        df_republican['twenty_eighteen'].iloc[0], df_republican['twenty_nineteen'].iloc[0], df_republican['twenty_twenty'].iloc[0], \
                        df_republican['twenty_twenty_one'].iloc[0],df_republican['twenty_twenty_two'].iloc[0],df_republican['twenty_twenty_three'].iloc[0]]
    })


    # Set the index to 'Years' for a custom x-axis label
    df_sentiments2.set_index('Posts Containing Republican Over Time', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments2.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)
    #----------------------------------------------------------------------------------------------
    # Percentage of posts for keyword at various upvote ranges
    df_sentiments3 = pd.DataFrame({
    'Posts Containing Republican at Various Upvote Ranges': ['0-99', '100-499', '500-1499', '1500+'],
    'Number of Posts': [df_republican['zero'].iloc[0], df_republican['one_hundred'].iloc[0], df_republican['five_hundred'].iloc[0], df_republican['fifteen_hundred'].iloc[0]]
    })


    # Set the index to 'Posts Containing Republican at Various Upvote Ranges' for a custom x-axis label
    df_sentiments3.set_index('Posts Containing Republican at Various Upvote Ranges', inplace=True)


    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    df_sentiments3.plot(kind='bar', ax=ax, legend=False)
   
    # Add y-axis label or title
    ax.set_ylabel('Number of Posts')


    # Rotate x-axis labels to be horizontal
    plt.xticks(rotation=0)


    # Display the Matplotlib figure in Streamlit
    st.pyplot(fig)

