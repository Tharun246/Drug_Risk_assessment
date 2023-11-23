import pandas as pd

# Read the CSV files
df1 = pd.read_csv('data/drugsComTest_raw.csv')
df2 = pd.read_csv('data/drugsComTrain_raw.csv')

# Concatenate the dataframes vertically
combined_df = pd.concat([df1, df2])

# Write the combined dataframe to a new CSV file
combined_df.to_csv('combined.csv', index=False)
