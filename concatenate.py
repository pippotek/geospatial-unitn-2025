import pandas as pd

# Load the two Parquet files
df1 = pd.read_parquet('data/disponibilita-parcheggi-storico.parquet')
df2 = pd.read_parquet('disponibilita-parcheggi-storico.parquet')

# Concatenate and drop duplicate rows
combined_df = pd.concat([df1, df2], ignore_index=True).drop_duplicates()

# Save the result to a new Parquet file
combined_df.to_parquet('disponibilita-parcheggi-storico-combined.parquet', index=False)

print("Parquet files combined and duplicates removed.")
