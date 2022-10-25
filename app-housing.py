import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data (1990) by Chenjun Li')
df = pd.read_csv('housing.csv')

median_house_value_filter = st.slider('Median Housing Price:', 0, 500001, 200000)  # min, max, default

# create a multi select
local_type_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a radio button
income_level_filter = st.radio(
    "Choose income level",
    ('Low', 'Median', 'High'))
# filter data by median house price
df = df[df.median_house_value <= median_house_value_filter]

# filter databy location
df = df[df.ocean_proximity.isin(local_type_filter)] 

# filter data by income
st.subheader('See more filters in the sidebar:')
if income_level_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_level_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income <= 4.5)]
elif income_level_filter == 'High':
    df = df[df.median_income > 4.5]

# show on map
st.subheader('See more filters in the sidebar:')
st.map(df)


# show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(20, 10))
df.median_house_value.hist(ax=ax, bins=30)
st.pyplot(fig)