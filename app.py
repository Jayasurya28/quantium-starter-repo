import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px

# Load the processed sales data
df = pd.read_csv('processed_sales_data.csv')

# Convert date to datetime for proper sorting
df['date'] = pd.to_datetime(df['date'])

# Sort by date
df = df.sort_values(by='date')

# Group by date to get daily total sales
daily_sales = df.groupby('date').sum(numeric_only=True).reset_index()

# Create a line chart
fig = px.line(
    daily_sales,
    x='date',
    y='sales',
    title='Daily Pink Morsel Sales Over Time',
    labels={'sales': 'Total Sales ($)', 'date': 'Date'}
)

# Highlight price change date
fig.add_shape(
    type="line",
    x0=pd.to_datetime('2021-01-15'),
    x1=pd.to_datetime('2021-01-15'),
    y0=0,
    y1=1,
    yref="paper",
    line=dict(
        color="red",
        width=2,
        dash="dash",
    )
)

fig.add_annotation(
    x=pd.to_datetime('2021-01-15'),
    y=1,
    yref="paper",
    text="Price Increase",
    showarrow=False,
    yshift=10
)

# Build Dash app
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Visualiser"

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
