# built in libraries

# third party libraries
import pandas as pd


# Importing json file to dataframe
card_df = pd.read_json('mtg_card_data.json')


# Summary of first 20 rows of data.
card_df.head(20)


# Looking at the column names
card_df.columns


# Getting the total cards of the top 25 artists
card_df["artist"].value_counts().head(25)
