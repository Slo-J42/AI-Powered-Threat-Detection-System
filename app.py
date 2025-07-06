import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.detect_anomalies import detect_anomalies
import streamlit as st

st.set_page_config(page_title='AI Threat Detection', layout='wide')
st.title('🛡️ AI-Powered Threat Detection Dashboard')
with st.spinner('Detecting anomalies...'):
    df = detect_anomalies()
st.success('Detection complete')
st.subheader('All Logs')
st.dataframe(df)
st.subheader('Anomalies')
st.dataframe(df[df['anomaly'] == -1])