# data_aggregator/data_aggregator.py
import os
import pandas as pd
from fuzzywuzzy import process
import config
from data_lake_storage.data_lake_storage import DataLakeStorage


class DataAggregator:
    def __init__(self, data_lake_storage):
        self.data_lake_storage = data_lake_storage

    def find_best_match(self, query, choices):
        # Fuzzywuzzy's process method to find the best match
        result = process.extractOne(query, choices)

        # Defining a threshold score (adjustable) to consider a match
        threshold = 80

        if result and result[1] >= threshold:
            return result[0]
        else:
            return query

    def map_to_canonical(self, seller, canonical_sellers):
        return canonical_sellers.get(seller, seller)

    def aggregate_spending(self, input_file_path):
        print(config.YELLOW + "\nAggregating and normalizing spending data..." + config.RESET)
        # Reading the CSV file from the Data Lake Storage's data directory
        df = pd.read_csv(input_file_path)

        # Dictionary to map Seller names to canonical names
        canonical_sellers = {}

        # Iterating through unique Seller names in the dataset
        unique_sellers = df['Seller'].unique()
        for seller in unique_sellers:
            # Check if a similar seller name exists in the dictionary
            existing_canonical_seller = self.find_best_match(
                seller, canonical_sellers.keys())

            # If a similar seller name is found, use the existing canonical name
            if existing_canonical_seller in canonical_sellers:
                canonical_sellers[seller] = canonical_sellers[existing_canonical_seller]
            else:
                canonical_sellers[seller] = seller

        # Function to map Seller names to canonical names using the dictionary
        df['CanonicalSeller'] = df['Seller'].apply(
            lambda x: self.map_to_canonical(x, canonical_sellers))

        # Grouping the data by 'CanonicalSeller' and sum the 'CostUSD' for each group
        aggregated_data = df.groupby('CanonicalSeller')[
            'CostUSD'].sum().reset_index()

        # Sorting the aggregated data by 'CanonicalSeller' alphabetically
        aggregated_data = aggregated_data.sort_values(by='CanonicalSeller')

        print("Spending data aggregation and normalization completed.")
        
        # Returning the aggregated data as a DataFrame
        return aggregated_data


def main():
    # Initialize Data Lake storage
    data_lake_storage = DataLakeStorage(config.DATA_LAKE_STORAGE_DIRECTORY)

    # Aggregate spending data
    aggregated_data = DataAggregator(
        data_lake_storage).aggregate_spending(config.INPUT_FILE_PATH)

    # Print the aggregated data
    print("\nAggregated Spending Data:")
    print(aggregated_data)


if __name__ == "__main__":
    main()
