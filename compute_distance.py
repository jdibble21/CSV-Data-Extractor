# Choose 4 attributes from 100 rows, compute distance and normalize between row values

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
data = pd.read_csv("hw3_compute_distance.csv")
data['victory_status'] = np.where(data.victory_status == "outoftime",0,data.victory_status)
data['victory_status'] = np.where(data.victory_status == "resign",1,data.victory_status)
data['victory_status'] = np.where(data.victory_status == "mate",2,data.victory_status)
data['victory_status'] = np.where(data.victory_status == "draw",3,data.victory_status)

# Separate the records into 3 different dataframes and normalize
df1 = data[['victory_status','white_rating']]
df1Result = df1.div(df1.sum(axis=1), axis=0)

df2 = data[['white_rating','black_rating']]
df2Result = df2.div(df2.sum(axis=1), axis=0)

df3 = data[['turns','victory_status']]
df3Result = df3.div(df3.sum(axis=1), axis=0)

print("=== NORMALIZATION OF VICTORY STATUS AND WHITE RATING ===\n")
print(df1Result)
print("\n=== NORMALIZATION OF WHITE RATING AND BLACK RATING ===\n")
print(df2Result)
print("\n=== NORMALIZATION OF TURNS AND VICTORY STATUS ===\n")
print(df3Result)

