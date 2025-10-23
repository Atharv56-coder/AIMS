import pandas as pd

# Sample dataset
data = {'Education' : ['High School', 'Undergraduate', 'Postgraduate', 'High School', 'Postgraduate']}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Manual Ordinal Encoding

# Finding out the unique values from Education column using the unique() function and storing them in a list
unique_values = list(df['Education'].unique())

#Creating an empty dictionary to store the encoded data
encoding_dict = {}
index = 0
for degree in unique_values:
    encoding_dict[degree] = index
    index += 1

# Create a new column with name Education_encoded and map the values assigned to undergraduate, postgraduate and high school in this column
df['Education_encoded'] = df['Education'].map(encoding_dict)

print("\nEncoded DataFrame:\n")
print(df)
print("\nEncoding dictionary:", encoding_dict)