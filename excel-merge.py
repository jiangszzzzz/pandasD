# 按照姓名合并表格

import pandas as pd

data1 = pd.read_excel('./data/workspace/总分排序.xlsx')
data2 = pd.read_excel('./data/workspace/报名信息.xlsx')

writer_score = pd.ExcelWriter('./data/workspace/score.xlsx')
data1['name'] = data1['姓名'].apply(lambda x: x.replace(' ', '').strip())
data1.to_excel(writer_score, sheet_name='score', index=False)
writer_score.close()

writer_info = pd.ExcelWriter('./data/workspace/info.xlsx')
data2['name'] = data2['姓名'].apply(lambda x: x.replace(' ', '').strip())
data2.to_excel(writer_info, sheet_name='info', index=False)
writer_info.close()

writer_merge = pd.ExcelWriter('./data/workspace/merge.xlsx')
data3 = pd.merge(data1, data2, left_on='name', right_on='name', how='right')
data3.to_excel(writer_merge, sheet_name='Merge1', index=False)
data3 = pd.merge(data2, data1, left_on='name', right_on='name', how='right')
data3.to_excel(writer_merge, sheet_name='Merge2', index=False)
writer_merge.close()

