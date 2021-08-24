import pandas as pd
import plotly.express as px

var = pd.read_csv("data.csv")
fig = px.scatter(var,x="date",y="cases",color="country")
fig.show()
