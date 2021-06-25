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
st.image('logo.jpg')
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


analysis20 = load2020Data()
analysis = loadWorldData()
analysisIndia = loadIndiaData()


def overview():
    st.header("Project Overview Here")


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

    st.dataframe(analysis20.getDataframe())


def analyseTimeline():
    st.header('Timeline Analyse')
    st.markdown('---')

    selLoc = st.selectbox(
        options=analysis20.getLocations(), label="Select Location")
    st.plotly_chart(plotLine(analysis20.getLocationData(selLoc)))


def analyseIndia():
    st.header("Indian Unemployment Analysis")
    st.markdown('---')

    st.header("Unemployment Rates in different States of India")
    st.image('images/in_states.png', use_column_width=True)

    st.header("Unemployment Rates in different Region of India")
    st.image('images/dir_india.png', use_column_width=True)

    st.header("Average Unemployment Rates in different States of India")
    st.image('images/avg_india.png', use_column_width=True)

    st.header("Unemployment Rates in different States & Region of India")
    st.image('images/pie_india.png', use_column_width=True)

    st.header("Percentage of unemployment Rates after Lockdown")
    st.image('images/%unemployment_in.png', use_column_width=True)

    st.header("Impact of Lockdown in different States of India")
    st.image('images/lock_india.png', use_column_width=True)


def analyseWorld():
    st.header("Global unemployment rate from 2010 to 2020")
    st.image('images/global.png', use_column_width=True)
    st.markdown('---')

    st.header("Top 20 Countries having highest Unemployment Rate")
    st.image('images/top20.png', use_column_width=True)
    st.markdown('---')

    st.header(
        "Unemployment rate in member states of the European Union in January 2021")
    st.image('images/eu.png', use_column_width=True)
    st.markdown('---')

    st.header("Unemployment rate in selected world regions between 2015 and 2020")
    st.image('images/regions.png', use_column_width=True)
    st.markdown('---')

    st.header("Youth unemployment rate in selected world regions in 2015 to 2020")
    st.image('images/youth_regions.png', use_column_width=True)
    st.markdown('---')

    st.header("France: Unemployment rate from 1991 to 2020")
    st.image('images/france.png', use_column_width=True)
    st.markdown('---')

    st.header("Unemployment rate in the United Kingdom (UK) from 1999 to 2020")
    st.image('images/uk.png', use_column_width=True)
    st.markdown('---')

    st.header("South Korea: Unemployment rate from 2016 to 2026")
    st.image('images/southkorea.png', use_column_width=True)
    st.markdown('---')

    st.header("Bangladesh: Unemployment rate from 1999 to 2020")
    st.image('images/Bangladesh.png', use_column_width=True)
    st.markdown('---')

    st.header("Japan: Unemployment rate from 1999 to 2020")
    st.image('images/japan.png', use_column_width=True)


sidebar.header('Choose Your Option')
options = ['Overview', 'View Dataset', 'Analyse India', 'Analyse World']
choice = sidebar.selectbox(options=options, label="Choose Action")

if choice == options[0]:
    overview()
elif choice == options[1]:
    viewDataset()
elif choice == options[2]:
    analyseIndia()
elif choice == options[3]:
    analyseWorld()
