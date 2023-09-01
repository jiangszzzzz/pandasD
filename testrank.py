# 成绩排名

import pandas as pd

data = pd.read_excel('./data/0719省局.xlsx')
# writer = pd.ExcelWriter('./data/tmp_testrank.xlsx')
# writer1 = pd.ExcelWriter('./data/tmp_testrank1.xlsx')
# writer2 = pd.ExcelWriter('./data/tmp_testrank2.xlsx')
# writer3 = pd.ExcelWriter('./data/tmp_testrank3.xlsx')
writer4 = pd.ExcelWriter('./data/tmp_testrank5.xlsx')

# 组织机构列  分列

tmp = data['组织机构'].str.split('-->', n=-1, expand=True)

# 分列 后拼接到预原表后

# res1 = pd.concat([data, tmp], axis=1)  # axis 为 0 是 水平拼接， axis 为 1 是 垂直拼接

# 拼接后写入新excel表

# res1.to_excel(writer, sheet_name='M', index=True)

# data.assign(new_col=lambda x: data['组织机构']+data['姓名']+data['性别']+str(data['年龄']))
# print(data)
# data.to_excel(writer2, sheet_name='M', index=True)


type_list = []
for j in tmp[2]:
    type_list.append(j)
type_list = set(type_list)
print(type_list)
#
for ty in type_list:
    ty1 = ty.replace("(公司)", "")
    print(len(ty1))
    a = data['组织机构'].str.contains(ty1)
    b = tmp[2].str.len() == len(ty1)
    for i in range(len(a)):
        a[i] = a[i] and b[i]
    data[a].to_excel(writer4, sheet_name=ty)
#

# writer.close()
# writer1.close()
# writer2.close()
# writer3.close()
writer4.close()

