import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
from database import Report
from visualization import *
from AnalyseData import Analyse

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

st.title('World Unemployment Analysis and Visualization')
sidebar = st.sidebar


# @st.cache(suppress_st_warning=True)
def loadIndiaData():
    return Analyse('datasets/india.csv')


# @st.cache(suppress_st_warning=True)
def loadWorldData():
    return Analyse('datasets/unemployment.csv')


# @st.cache(suppress_st_warning=True)
def load2020Data():
    return Analyse('datasets/unemployment2020.csv')


analysis20 = loadIndiaData()
analysis = loadWorldData()
analysisIndia = loadIndiaData()


def overview():
    st.header("Project Overview Here")
    st.markdown("""
        # This is Heading 1
        ## heading 2
        
    """)
    st.image('logo.jpg')
    st.subheader('ksjhdkj')


def viewDataset():
    st.header('Data Used in Project')
    dataframe = analysis20.getDataframe()

    with st.spinner("Loading Data..."):
        st.dataframe(dataframe)

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown("### No. of Rows :")
        cols[1].markdown(f"# {dataframe.shape[0]}")
        cols[2].markdown("### No. of Columns :")
        cols[3].markdown(f"# {dataframe.shape[1]}")
        st.markdown('---')

        st.header('Summary')
        st.dataframe(dataframe.describe())
        st.markdown('---')

        types = {'object': 'Categorical',
                 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], dataframe.dtypes))
        st.header('Dataset Columns')
        for col, t in zip(dataframe.columns, types):
            st.markdown(f"### {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"# {dataframe[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")


def analyseByCountry():

    st.header('Analysis By Country')
    selMonth = st.selectbox(options=list(analysis20.getDataframe()[
                            'Month'].unique()), label="Select Month to Display")
    chartType = st.selectbox(
        options=['Bar', 'Line'], label='Select Chart Type')

    data = analysis20.getCountrywise(selMonth)
    if chartType == 'Line':
        st.plotly_chart(plotLine(data.index, data.values.flatten()))
    elif chartType == 'Bar':
        st.plotly_chart(plotBar(data.index, data.values.flatten()))


sidebar.header('Choose Your Option')
options = ['Overview', 'View Dataset', 'Analyse Unemployment By Country']
choice = sidebar.selectbox(options=options, label="Choose Action")

if choice == options[0]:
    overview()
if choice == options[1]:
    viewDataset()
elif choice == options[2]:
    analyseByCountry()
