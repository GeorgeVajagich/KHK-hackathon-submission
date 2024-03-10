import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv(r"C:\Users\Geord\OneDrive\Desktop\Economics Stuff\Metro Area 2022 5y ACS data.csv",index_col='name')

st. set_page_config(layout="wide")

metro = st.selectbox(
    "Select a Metropolitan Area",
    (df.index))




commuterData=[df.loc[metro]["Car Commuters"],df.loc[metro]["Public Transit Commuters"],df.loc[metro]["Bicycle Commuters"],df.loc[metro]["Walking Commuters"],df.loc[metro]["Other Commuters"],df.loc[metro]["Worked at Home"]]
commuterLabels=["Car Commuters","Public Transit Commuters","Bicycle Commuters","Walking Commuters","Other Commuters","Worked at Home"]
commuterFig= px.pie(df, values=commuterData, names=commuterLabels, color=commuterData)

bornData=[df.loc[metro]["Born in State of Residence"],df.loc[metro]["Born in other US State"],df.loc[metro]["Born in US territories"],df.loc[metro]["Born in other Country"]]
bornLabels=["Born in State of Residence","Born in other US State","Born in US territories","Born in other Country"]
bornFig= px.pie(df, values=bornData, names=bornLabels, color=bornData)

col1, col2 = st.columns(2)

with col1:
    st.title("Median Home Value: "+str(df.loc[metro]["Median Home Value"])+"$")
    st.header("How residents get to work")
    (st.plotly_chart(commuterFig))
with col2:
    st.title("Median Household Income: "+str(df.loc[metro]["Median Household Income"])+"$")
    st.header("Where residents were born")
    st.plotly_chart(bornFig)