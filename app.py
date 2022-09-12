import streamlit as st
import os
import sys
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go


pd.set_option("display.precision", 3)
# Set display option for 3 decimal places

st.set_page_config(
    # Setting the icon, text of the web browser tab
    page_title='BR+A Compute Streamlit Example Template', layout='wide',
    page_icon='assets/br+alogo.png'
)


@st.cache
def make_dfs():
    df_h = pd.read_csv('newouts\\hosp_normal.csv')
    df_h = df_h.sort_values('EUI')

    df_o = pd.read_csv('newouts\\office_normal.csv')
    df_o = df_o.sort_values('EUI')

    df_o_ph = pd.read_csv('newouts\\office_phinf.csv')
    df_o_ph = df_o_ph.sort_values('R-Value Area Average (IP)')

    df_h_ph = pd.read_csv('newouts\\hosp_phinf.csv')
    df_h_ph = df_h_ph.sort_values('EUI')
    return df_h, df_o, df_o_ph, df_h_ph


df_h, df_o, df_o_ph, df_h_ph = make_dfs()


#!*fig = px.line(df_h, x='R-Value Area Average (IP)', y='EUI', markers=True)

newfig = go.Figure()
newfig.add_trace(go.Scatter(x=df_h['R-Value Area Average (IP)'], y=df_h['EUI'],
                            mode='lines+markers',
                            name='Hospital Case'))
newfig.add_trace(go.Scatter(x=df_o['R-Value Area Average (IP)'], y=df_o['EUI'],
                            mode='lines+markers',
                            name='Office Case'))
newfig.add_trace(go.Scatter(x=df_o_ph['R-Value Area Average (IP)'], y=df_o_ph['EUI'],
                            mode='lines+markers',
                            name='Office PH infil'))
newfig.add_trace(go.Scatter(x=df_h_ph['R-Value Area Average (IP)'], y=df_h_ph['EUI'],
                            mode='lines+markers',
                            name='Hospital PH infil'))
st.plotly_chart(newfig, use_container_width=True)
