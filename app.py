import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
from database import Report
from visualization import plot, plotBar, plotLine
from AnalyseData import Analyse

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

st.title('Global Warming and Climate Change Analysis')
sidebar = st.sidebar

def viewForm():

    title = st.text_input("Report Title")
    desc = st.text_area('Report Description')
    btn = st.button("Submit")

    if btn:
        report1 = Report(title = title, desc = desc, data = "")
        sess.add(report1)
        sess.commit()
        st.success('Report Saved')

def analyseByCountry():

    analysis20 = Analyse('datasets/unemployment2020.csv')
    selMonth = st.selectbox(options = list(analysis20.getDataset()['Month'].unique()), label="Select Month to Display")

    # st.dataframe(analysis20.getDataset())

    # selMonth = 'January'
    data = analysis20.getCountrywise(selMonth)
    st.plotly_chart(plotLine(data.index, data.values.flatten()))


def viewReport():
    reports = sess.query(Report).all()
    titlesList = [ report.title for report in reports ]
    selReport = st.selectbox(options = titlesList, label="Select Report")
    
    reportToView = sess.query(Report).filter_by(title = selReport).first()

    markdown = f"""
        ## {reportToView.title}
        ### {reportToView.desc}
        
    """

    st.markdown(markdown)

sidebar.header('Choose Your Option')
options = [ 'View Database', 'Analyse Unemployment By Country', 'View Report' ]
choice = sidebar.selectbox( options = options, label="Choose Action" )

if choice == options[1]:
    analyseByCountry()
elif choice == options[2]:
    analyse()