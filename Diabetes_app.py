#%%writefile app.py
import streamlit as st
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
from prophet import Prophet
import pycountry

# Load datasets
fertility_data  = pd.read_csv(r'C:\Users\User\Desktop\Fertility.csv')
death_data  = pd.read_csv(r'C:\Users\User\Desktop\Death.csv')
life_expectancy_data  = pd.read_csv(r'C:\Users\User\Desktop\Life Expectancy.csv')


# Sidebar for dataset selection
dataset = st.sidebar.selectbox("Select Dataset", ("Death Data", "Fertility Data", "Life Expectancy Data"))

st.title('Healthcare Analytics Dashboard')

def eda_death_data(data):
    st.header("Death Data")
    st.write("Summary Statistics")
    st.write(data.describe())

    st.write("Missing Values")
    st.write(data.isnull().sum())

    metrics = data['metric'].unique()
    for metric in metrics:
        st.subheader(f"EDA for {metric}")
        metric_data = data[data['metric'] == metric]

        fig, ax = plt.subplots()
        sns.histplot(metric_data['val'], kde=True, ax=ax)
        ax.set_title(f'Distribution of {metric}')
        st.pyplot(fig)

        fig, ax = plt.subplots()
        sns.boxplot(x='location', y='val', data=metric_data, ax=ax)
        ax.set_title(f'{metric} by Region')
        plt.xticks(rotation=90)
        st.pyplot(fig)

def eda_fertility_data(data):
    st.header("Fertility Data")
    st.write("Summary Statistics")
    st.write(data.describe())

    st.write("Missing Values")
    st.write(data.isnull().sum())

    fig, ax = plt.subplots()
    sns.histplot(data['val'], kde=True, ax=ax)
    ax.set_title('Distribution of Fertility Rate')
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.boxplot(x='location', y='val', data=data, ax=ax)
    ax.set_title('Fertility Rate by Region')
    plt.xticks(rotation=90)
    st.pyplot(fig)

def eda_life_expectancy_data(data):
    st.header("Life Expectancy Data")
    st.write("Summary Statistics")
    st.write(data.describe())

    st.write("Missing Values")
    st.write(data.isnull().sum())

    fig, ax = plt.subplots()
    sns.histplot(data['val'], kde=True, ax=ax)
    ax.set_title('Distribution of Life Expectancy')
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.boxplot(x='location', y='val', data=data, ax=ax)
    ax.set_title('Life Expectancy by Region')
    plt.xticks(rotation=90)
    st.pyplot(fig)

# Display EDA based on selected dataset
if dataset == "Death Data":
    eda_death_data(death_data)
elif dataset == "Fertility Data":
    eda_fertility_data(fertility_data)
else:
    eda_life_expectancy_data(life_expectancy_data)
