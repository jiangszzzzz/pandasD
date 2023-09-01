import pandas as pd

data1 = pd.read_excel('./data/比对测试/测试1.xlsx')
data2 = pd.read_excel('./data/比对测试/测试2.xlsx')

hashmap1 = {}
hashmap2 = {}

print(data1.shape[0])

for i1 in range(data1.shape[0]):
    if str(data1['new_col_name'][i1]) == 'nan':
        continue
    else:
        hashmap1[data1['new_col_name'][i1]] = data1['成绩'][i1]

for i2 in range(data2.shape[0]):
    if str(data2['new_col_name'][i2]) == 'nan':
        continue
    else:
        hashmap2[data2['new_col_name'][i2]] = data2['成绩'][i2]

print(hashmap1)
print(hashmap2)
print('---------------')
print(hashmap1 == hashmap2)
print('---------------')
print(hashmap1.keys() ^ hashmap2.keys())
print('---------------')
differ = set(hashmap1.items()) ^ set(hashmap2.items())
print(differ)

