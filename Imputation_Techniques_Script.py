import pandas as pd
import numpy as np

# Sample dataset
data = {'Age': [25, np.nan, 30, np.nan, 45, 35]}
df = pd.DataFrame(data)
print("Original DataFrame with Missing Values:")
print(df)

#Mean Imputation
mean_val = df['Age'].sum(skipna=True) / df['Age'].count()
mean_imputed_values = []
for age in df['Age']:
    if np.isnan(age):        # if age is NaN
        mean_imputed_values.append(mean_val)
    else:                    # if age is a valid number
        mean_imputed_values.append(age)
df['Age_mean_imputed'] = mean_imputed_values # Assign the new list as a column

# Median Imputation
sorted_vals = sorted(df['Age'].dropna())
n = len(sorted_vals)
if n % 2 == 0:
    median_val = (sorted_vals[n//2 - 1] + sorted_vals[n//2]) / 2
else:
    median_val = sorted_vals[n//2]
df['Age_median_imputed'] = df['Age'].apply(lambda x: median_val if np.isnan(x) else x)

# Mode Imputation
non_missing = df['Age'].dropna() # removes all the NaN values and store the output in non_missing

values, counts = np.unique(non_missing, return_counts=True) # stores the uniques values in 'values' variable. return_counts = True counts the number of times an element was repeated and these counts are stored in the 'counts' variable

mode_val = values[np.argmax(counts)] # finds the index of the value which has occured most frequently and stores that in another variable i.e mode_val

imputed_values = []
for val in df['Age']:
    if np.isnan(val):
        imputed_values.append(mode_val)
    else:
        imputed_values.append(val)
df['Age_mode_imputed'] = imputed_values
print(df)

print("\nDataFrame after Manual Imputation:")
print(df)
