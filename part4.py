# Imports -- you may add others but do not need to
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets




plotly.tools.set_credentials_file(username='oliverwang', api_key='ki77h8anNbeY5bNIPuxL')

data=pd.read_csv("noun_data.csv")
print(data)

data = [
    go.Bar(
        x=data['Noun'], # assign x as the dataframe column 'x'
        y=data['Number']
    )
]

py.plot(data, filename='part4_viz_image')