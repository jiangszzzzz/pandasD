# pandas excel 拆分列

import pandas as pd

# 读入文件
data = pd.read_excel("./data/douban_top250.xls")
# apply 批量处理
# data['zh-name'] = data['fullname'].apply(lambda x: x.split(' ')[0])

writer = pd.ExcelWriter('./data/tmp.xlsx')

# 写入
# data.to_excel(writer, sheet_name='原始数据')

# 按照年份筛选
# print(data[data['pubyear'] == 1993])

# for i in data['pubyear'].unique():
#     data[data['pubyear'] == i].to_excel(writer, sheet_name=str(i))

# 按照类型筛选
# data[data['genre'].str.contains('科幻')]

# type_list = set(z for j in data['genre'] for z in j.split(','))

type_list = []
for j in data['genre']:
    for z in j.split(','):
        type_list.append(z)
type_list = set(type_list)
for ty in type_list:
    data[data['genre'].str.contains(ty)].to_excel(writer, sheet_name=ty)

writer.close()

