# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv("formatted_output.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Marshmallow Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales"},
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Marshmallow Sales Visualiser", style={"textAlign": "center"}),

    dcc.Graph(id="line-chart", figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
