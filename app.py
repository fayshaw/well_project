import streamlit as st
import pandas as pd
import altair as at
import database
import well_plot
import sqlalchemy

st.title("Abandoned Wells")
st.text("An interactive map of abandoned wells that can be used for geothermal energy")

depth = st.sidebar.number_input('Depth (m)', min_value=0, value=500)
gradient = st.sidebar.number_input('Gradient (°C / m)', min_value=0.0, value=0.1, format='%0.3f')

data = database.get_wells(depth, gradient)
well_df = pd.DataFrame(data).dropna()

well_chart = well_plot.make_chart(well_df)
st.altair_chart(well_chart)