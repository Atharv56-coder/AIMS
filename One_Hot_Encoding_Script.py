import pandas as pd
import numpy as np

# Sample dataset
data = {'City': ['Delhi', 'Mumbai', 'Kolkata', 'Delhi']}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Manual One-Hot Encoding
unique_values = list(df['City'].unique())

for val in unique_values:
    new_col = []   # empty list to store 1s and 0s
    
    for city in df['City']:   # go through each city in the column
        if city == val:
            new_col.append(1)
        else:
            new_col.append(0)
    
    df[val] = new_col   # add the new column to the DataFrame

print(df)

print("\nOne-Hot Encoded DataFrame:")
print(df)
