import warnings
import pandas as pd
import os
warnings.filterwarnings('ignore')

# for root, dirs, files in os.walk('./data/0719/党建第二轮成绩统计'):
for root, dirs, files in os.walk('./data/按sheet拆分表格0719地市'):
    for f in files:
        Rfile = os.path.join(root,f)
        data = pd.read_excel(Rfile)

        num = 0
        Score = 0
        num_0 = 0
        num1 = 0
        for i in data['成绩']:
            num = num + 1
            Score += i
            if i == 0:
                num_0 += 1
            if 0<i<60:
                num1 += 1
        avg = Score/num
        print(f.split('.')[0],':','答题人数:', num, '总分:', Score, '平均分:', avg,'0分人数:', num_0,'0-60分人数:',num1)



# 遍历
# def walkFile(file):
#     for root, dirs, files in os.walk(file):
#
#         # root 表示当前正在访问的文件夹路径
#         # dirs 表示该文件夹下的子目录名list
#         # files 表示该文件夹下的文件list
#
#         # 遍历文件
#         for f in files:
#             print(os.path.join(root, f))
#
#         # 遍历所有的文件夹
#         for d in dirs:
#             print(os.path.join(root, d))