# pandas excel 拆分列

import pandas as pd

# 读入文件
data = pd.read_excel("./data/douban_top250.xls")
# apply 批量处理
data['zh-name'] = data['fullname'].apply(lambda x: x.split(' ')[0])

writer = pd.ExcelWriter('./data/tmp.xlsx')

# 写入
# data.to_excel(writer, sheet_name='原始数据')

# 按照年份筛选
# print(data[data['pubyear'] == 1993])

for i in data['pubyear'].unique():
    data[data['pubyear'] == i].to_excel(writer, sheet_name=str(i))

writer.close()

