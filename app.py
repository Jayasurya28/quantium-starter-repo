import pandas as pd
import datetime
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# Load data
df = pd.read_csv("processed_sales_data.csv", parse_dates=["date"])

# Initialize Dash app
app = Dash(__name__)
app.title = "Pink Morsel Sales Dashboard"

# Define app layout
app.layout = html.Div(
    children=[
        html.H1("Pink Morsel Sales Visualiser", style={
            'textAlign': 'center',
            'color': '#800080',
            'marginBottom': '30px'
        }),

        html.Div([
            html.Label("Select a Region:", style={
                'fontWeight': 'bold',
                'marginRight': '15px',
                'color': '#333'
            }),
            dcc.RadioItems(
                id='region-selector',
                options=[
                    {'label': 'All', 'value': 'all'},
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'}
                ],
                value='all',
                labelStyle={'display': 'inline-block', 'marginRight': '10px'}
            )
        ], style={'textAlign': 'center', 'marginBottom': '20px'}),

        dcc.Graph(id='sales-line-chart')
    ],
    style={'fontFamily': 'Arial', 'padding': '20px', 'backgroundColor': '#f0f8ff'}
)

# Callback to update chart based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-selector', 'value')]
)
def update_chart(selected_region):
    # Filter data
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # Group by date
    daily_sales = filtered_df.groupby("date", as_index=False)["sales"].sum()

    # Create figure
    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales Over Time - {selected_region.capitalize()} Region" if selected_region != 'all' else "Pink Morsel Sales Over Time - All Regions",
        labels={"date": "Date", "sales": "Total Sales ($)"}
    )

    # Add vertical line for price change
    fig.add_vline(
        x=datetime.datetime(2021, 1, 15),
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top left"
    )

    fig.update_layout(
        plot_bgcolor="#fffafa",
        paper_bgcolor="#fffafa",
        font_color="#333",
        title_font_size=20,
        title_x=0.5
    )

    return fig

# Run app
if __name__ == '__main__':
    app.run(debug=True)
