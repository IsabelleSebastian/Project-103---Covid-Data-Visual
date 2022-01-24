import pandas as pd
import plotly.express as px

df = pd.read_csv("Covid Data.csv")
scatter = px.scatter(df, x = "date", y = "cases", color = "country")
scatter.show()