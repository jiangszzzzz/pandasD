import pandas as pd

df1 = pd.DataFrame({'key':['a','b','c'], 'value1':[1,2,3]})
df2 = pd.DataFrame({'key':['a','b','d'], 'value2':[4,5,6]})
print(df1)
print(df2)
result = pd.merge(df1, df2, on='key').assign(new_col=lambda x: x['value1']+x['value2'])
print(result)