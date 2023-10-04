# reporting_and_visualization/reporting_and_visualization.py
import config
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_table
from datetime import datetime, timedelta
import random
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# Set the path to the data file
data_path = config.INPUT_FILE_PATH

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(data_path)

# Mock data with start and end dates for the date range
start_date = datetime(2023, 7, 1)
end_date = datetime(2023, 9, 30)

# Generating random dates within the specified range for each row
date_column = []
for _ in range(len(df)):
    random_date = start_date + timedelta(
        days=random.randint(0, (end_date - start_date).days)
    )
    date_column.append(random_date)

# Adding the date column to the DataFrame
df["Date"] = date_column

# function to find the best match for a Seller name
def find_best_match(query, choices):
    # fuzzywuzzy's process method to find the best match
    result = process.extractOne(query, choices)

    # Defining a threshold score (adjustable) to consider a match
    threshold = 80

    if result and result[1] >= threshold:
        return result[0]
    else:
        return query


# Dictionary to map Seller names to canonical names
canonical_sellers = {}

# Iterating through unique Seller names in the dataset
unique_sellers = df["Seller"].unique()
for seller in unique_sellers:
    # Check if a similar seller name exists in the dictionary
    existing_canonical_seller = find_best_match(
        seller, canonical_sellers.keys()
    )

    # If a similar seller name is found, use the existing canonical name
    if existing_canonical_seller in canonical_sellers:
        canonical_sellers[seller] = canonical_sellers[
            existing_canonical_seller
        ]
    else:
        canonical_sellers[seller] = seller


# Function to map Seller names to canonical names using the dictionary
def map_to_canonical(seller):
    return canonical_sellers.get(seller, seller)


# Applying the mapping function to the 'Seller' column
df["CanonicalSeller"] = df["Seller"].apply(map_to_canonical)

# Define the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    [
        html.H1("Weekly Report - Vendor Spending Analysis"),
        # Dropdown for selecting visualization
        dcc.Dropdown(
            id="visualization-select",
            options=[
                {
                    "label": "Vendor Spending Distribution",
                    "value": "vendor_distribution",
                },
                {
                    "label": "Weekly Spending Over Time",
                    "value": "weekly_spending_over_time",
                },
            ],
            value="vendor_distribution",
            style={"width": "50%"},
        ),
        # Placeholder for the selected visualization
        dcc.Graph(id="visualization-output"),
        # Table for top 10 vendors by spending
        html.H2("Top 10 Vendors by Spending"),
        dcc.Loading(
            dash_table.DataTable(
                id="top-vendors-table",
                columns=[
                    {"name": col, "id": col}
                    for col in ["Vendor", "TotalSpending"]
                ],
                style_table={"height": "300px", "overflowY": "auto"},
                style_cell={"textAlign": "left"},
            ),
        ),
    ]
)

# Define callback functions for updating the visualization and table


@app.callback(
    [
        Output("visualization-output", "figure"),
        Output("top-vendors-table", "data"),
    ],
    [Input("visualization-select", "value")],
)
def update_visualization(selected_visualization):
    if selected_visualization == "vendor_distribution":
        # Create a histogram of spending by Vendor
        vendor_distribution = (
            df.groupby("CanonicalSeller")["CostUSD"].sum().reset_index()
        )
        fig = px.bar(
            vendor_distribution,
            x="CanonicalSeller",
            y="CostUSD",
            title="Vendor Spending Distribution",
        )

        # Update the top vendors table
        top_vendors = vendor_distribution.sort_values(
            by="CostUSD", ascending=False
        ).head(10)
        top_vendors_table_data = top_vendors.to_dict("records")

    elif selected_visualization == "weekly_spending_over_time":
        df["Date"] = pd.to_datetime(df["Date"])
        weekly_spending_over_time = df.resample("W", on="Date")[
            "CostUSD"
        ].sum()
        fig = px.line(
            weekly_spending_over_time,
            x=weekly_spending_over_time.index,
            y="CostUSD",
            title="Weekly Spending Over Time",
        )

        top_vendors_table_data = []

    return fig, top_vendors_table_data

class ReportingAndVisualization:
    def __init__(self):
        # Initialize the Reporting and Visualization component
        pass

    def generate_report(self, aggregated_data):
        # Simulate generating a summarized report
        print(config.YELLOW + "\nGenerating summarized report..." + config.RESET)
        
        print("Summarized report generated.")

    def generate_visualizations(self, aggregated_data):
        # Simulate generating visualizations
        print(config.GREEN + "\nGenerating visualizations..." + config.RESET)

        run_flag = False

        if run_flag:
            app.run_server(debug=True)
        
        print("Visualizations generated.")

def main():
    # Initialize Reporting and Visualization component
    reporting_and_visualization = ReportingAndVisualization()
    # app.run_server(debug=True)
    

# # Run the app
# if __name__ == "__main__":
#     app.run_server(debug=True)
