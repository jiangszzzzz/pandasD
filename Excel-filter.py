import pandas as pd

data = pd.read_excel('./data/workspace/merge.xlsx')

ty_list1 = []
for i in data['岗位名称']:
    ty_list1.append(i)
ty_list1 = set(ty_list1)

ty_list2 = []
for i in data['地点']:
    ty_list2.append(i)
ty_list2 = set(ty_list2)

writer1 = pd.ExcelWriter('./data/workspace/按照岗位排名.xlsx')
for j1 in ty_list1:
    data[data['岗位名称'] == j1].to_excel(writer1, sheet_name=str(j1), index=False)
writer1.close()

writer2 = pd.ExcelWriter('./data/workspace/按照地点分类.xlsx')
for j2 in ty_list2:
    data[data['地点'] == j2].to_excel(writer2, sheet_name=str(j2), index=False)
writer2.close()
