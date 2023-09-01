import pandas as pd
# 定义写，读excel到data
writer = pd.ExcelWriter('./0725/tmp1.xlsx')
# data = pd.read_excel('./data/测试.xlsx')
data = pd.read_excel('./0725/0725-1.xlsx')

# ------大表 分组排序-------
# 原数据 成绩为‘-’ 影响排序方法，顾替换
# assign增加新的唯一标识列，防止重名
# 按照唯一标识 匿名函数 组内排序

data['成绩'] = data['成绩'].apply(float)
# data['成绩'] = data['成绩'].str.replace("-","0").apply(float)

# data = data[data['成绩']!= 0]
data = data.assign(new_col_name=lambda x: data['组织机构']+data['姓名'])
# groupby 后是在内存，经过方法后实例化为series
# data = data.groupby('new_col_name').apply(lambda x: x.sort_values('成绩', ascending=False))
data = data.groupby('new_col_name').apply(lambda x:x[x.成绩==x.成绩.max()])
# 保留一次最好成绩
data = data.drop_duplicates('new_col_name',keep='first')
# ------大表，按照地市单位拆分为 多个sheet--------
# print(data)
tmp = data['组织机构'].str.split('-->', n=-1, expand=True)  # 组织按照--> 符号形成 list的series

city_list = []  # 定义城市 list
DF_Citylist = tmp[2]  # list 第二项为地市

for city in DF_Citylist: # 遍历
    city_list.append(city)
city_list = set(city_list)  # 遍历后去重
print(city_list)

for ty in city_list:

    if ty == "湖北省局(公司)":
        ty1 = ty.replace("(公司)", "") # 括号影响 contains 模式匹配
        a = data['组织机构'].str.contains(ty1)
        data[a].to_excel(writer, sheet_name=ty) # 分sheet 写入excel
    else:
        a = data['组织机构'].str.contains(ty) # 包含关系+长度相等 双重校验
        b = DF_Citylist.str.len() == len(ty)
        for i in range(len(a)):
            a[i] = a[i] and b[i]
        data1 = data[a]
        print(ty,'/','考试人数:',data1.shape[0],'/','总分：',data1['成绩'].sum(),'/','平均分：', data1['成绩'].sum()/data1.shape[0])
        data[a].to_excel(writer, sheet_name=ty) # 分sheet 写入excel

## 分组排序写
# data.to_excel(writer, sheet_name='分组排序')

writer.close()
