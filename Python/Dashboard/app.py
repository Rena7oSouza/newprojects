import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load the previously generated CSV file into a pandas DataFrame
df = pd.read_csv('fake_sales_data.csv')

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Converting 'Date' to datetime

# Initialize the Dash app
app = dash.Dash(__name__)

# Extract the year from the Date column
df['Year'] = df['Date'].dt.year

# Group by the 'Year' and sum the 'Cash Sale' and 'Installment Sale'
df_grouped = df.groupby('Year')[['Cash Sale', 'Installment Sale']].sum().reset_index()

# Create the Dash layout
app.layout = html.Div([

    # Create a row for the first two charts, limiting their height to a fixed value
    html.Div(
        [
            html.H1('Sales Data Dashboard', style={'text-align': 'center'}),
            
            # Line chart for Cash Sales over Time
            html.Div(
                dcc.Graph(
                   className='first-line',
                    id='cash-sales-line-chart',
                    figure=px.line(df_grouped, x='Year', y=['Cash Sale', 'Installment Sale'], title='Cash Sales and Installment Sales by Year')
                        .update_layout(
                            margin=dict(t=30, b=40, l=40, r=30),
                            xaxis=dict(
                                title='Year',  # Add title for x-axis
                                tickmode='array',
                                tickvals=df_grouped['Year'],  # Use years as ticks
                            ),
                            yaxis=dict(
                                title='Sales Value',  # Add title for y-axis
                                tickformat='.2f',  # Format sales values with two decimal places
                            )
                        )
                ),
                style={'width': '50%', 'display': 'inline-block', 'height': '40vh'}
            ),
            
            # Bar chart for Total Sales (Cash Sale + Installment Sale)
            html.Div(
                dcc.Graph(
                    className='first-line',
                    id='total-sales-bar-chart first-line',
                    figure=px.bar(df, x='Date', y=['Cash Sale', 'Installment Sale'], title='Total Sales')
                        .update_layout(
                            margin=dict(t=30, b=40, l=40, r=30),
                        )
                ),
                style={'width': '50%', 'display': 'inline-block', 'height': '40vh'}  # 20% of the viewport height
            ),
        ],
        style={'display': 'flex', 'justify-content': 'space-between', 'height': '40vh'}  # Adjust the container height
    ),
    
    # Pie chart for the distribution of received vs unpaid installments
    dcc.Graph(
        id='received-vs-debit-pie-chart',
        figure=px.pie(df, names='Date', values='Debit', title='Received vs. Unpaid Installments')
            .update_layout(margin=dict(t=30, b=40, l=40, r=30), height=350)
    ),
    
    # Histogram for the distribution of credits granted
    dcc.Graph(
        id='credit-distribution-histogram',
        figure=px.histogram(df, x='Credit', title='Distribution of Credits Granted')
            .update_layout(margin=dict(t=30, b=40, l=40, r=30), height=350)
    ),
    
    # Scatter plot for Entry vs Cash Sale
    dcc.Graph(
        id='entry-vs-cash-sale-scatter',
        figure=px.scatter(df, x='Cash Sale', y='Entry', title='Entry vs Cash Sale')
            .update_layout(margin=dict(t=30, b=40, l=40, r=30), height=350)
    ),
    
    # Box plot for installment sale values
    dcc.Graph(
        id='installment-sale-box-plot',
        figure=px.box(df, y='Installment Sale', title='Box Plot of Installment Sales')
            .update_layout(margin=dict(t=30, b=40, l=40, r=30), height=350)
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
