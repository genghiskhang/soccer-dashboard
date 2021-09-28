#Pandas, Plotly, and NumPy modules
import pandas as pd
import numpy as np
import plotly.express as px

#Modules imported to retrieve data from Google Sheets
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

xVals = np.random.randn(20).tolist()
yVals = np.random.randn(20).tolist()

fig = px.scatter(x=xVals, y=yVals, width=1)
fig.show()