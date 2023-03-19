import pandas as pd

df1 = pd.DataFrame({
    'one': [2, 1, 6, 3],
    'two': [3, 1, 4, 2],
    'three': [9, 2, 1, 3]
})

print(df1)
df1 = df1.sort_values(by='two')
print(df1)
