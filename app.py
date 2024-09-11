import os
import psycopg2
import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.shortcuts import render
from flask import Flask, render_template, jsonify, request, send_file
from wordcloud import WordCloud, STOPWORDS

#################################################
# Database Setup
#################################################

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='Project_3_1',
                            user='postgres',
                            password="your Password")
    return conn


#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return render_template('index.html')

## LOCATION COUNT BAR PLOTS ##

### APP ROUTE FOR CONSTRUCTION LOCATION COUNT ###

## WORD COUNT PIE PLOTS ##

### APP ROUTE FOR DATA ANALYST WORD COUNT ###

@app.route('/data_analyst_word_cloud')
def construction_word_cloud():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM data_analyst_word_count;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT word FROM data_analyst_word_count;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Word ": column_values2,
        "Count ": column_values
    })
    text = df["Word "].str.cat(sep=" ")
    wordcloud = WordCloud(width = 600, height = 600,
                    background_color ='white',
                    min_font_size = 10).generate(text)  
    # plot the WordCloud
    fig = plt.figure(figsize=(8, 8), facecolor=None)
    ax = fig.add_subplot(111)
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    # Convert the figure to a PNG image
    filename = "aaa.png"
    file_path = os.path.join("static", filename)
    plt.savefig(file_path, format="png")
    # Return the image as a response
    return render_template("resume_helper_wordcloud.html", image_path=filename)

### APP ROUTE FOR DATA ENGINEER WORD CLOUD ###

@app.route('/data_engineer_word_cloud')
def engineering_word_cloud():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM data_engineer_word_count;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT word FROM data_engineer_word_count;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Word ": column_values2,
        "Count ": column_values
    })
    text = df["Word "].str.cat(sep=" ")
    wordcloud = WordCloud(width = 600, height = 600,
                    background_color ='white',
                    min_font_size = 10, 
                    ).generate(text)  
    # plot the WordCloud
    fig = plt.figure(figsize=(8, 8), facecolor=None)
    ax = fig.add_subplot(111)
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    # Convert the figure to a PNG image
    filename = "aaa.png"
    file_path = os.path.join("static", filename)
    plt.savefig(file_path, format="png")
    # Return the image as a response
    return render_template("resume_helper_wordcloud.html", image_path=filename)


## WORD COUNT PIE PLOTS ##

### APP ROUTE FOR DATA ANALYST WORD COUNT ###

@app.route('/data_analyst_word_count')
def data_analyst_word_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM data_analyst_word_count LIMIT 20;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT word FROM data_analyst_word_count LIMIT 20;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Word ": column_values2,
        "Count ": column_values
    })
    fig = px.pie(df, values="Count ", names="Word ", hole=0.3, height=600, width=600,  title= 'Data Analyst - BuzzWords')
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Data Analyst Key Words"
    description = """
    """
    return render_template('resume_helper_pie.html', graphJSON=graphJSON, header=header,description=description)
    fig.show()

### APP ROUTE FOR DATA ENGINEER  WORD COUNT ###

@app.route('/data_engineer_word_count')
def data_engineer_word_scrapes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT count FROM data_engineer_word_count LIMIT 20;')
    data = cur.fetchall()
    column_values = []
    for row in data: column_values.append(row[0])
    cur.execute('SELECT word FROM data_engineer_word_count LIMIT 20;')
    data2 = cur.fetchall()
    column_values2 = []
    for row in data2: column_values2.append(row[0])
    cur.close()
    conn.close()
    df = pd.DataFrame({
        "Word ": column_values2,
        "Count ": column_values
    })
    fig = px.pie(df, values="Count ", names="Word ", hole=0.3, height=600, width=600,)
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide') # , color="City", barmode="stack"
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Data Engineer Key Words"
    description = """
    """
    return render_template('resume_helper_pie.html', graphJSON=graphJSON, header=header,description=description)

