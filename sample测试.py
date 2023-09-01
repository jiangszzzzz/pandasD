import os
import pandas as pd
import os

if os.path.exists('./抽取结果'):
    pass
else:
    os.mkdir('./抽取结果')

# 测试
for root,dirs,files in os.walk('./地市'):
    for target in files:
        sum_num = 0
        target_dir = os.path.join(root, target)
        data = pd.read_excel(target_dir)
        data = data[data['年龄（周岁）'].apply(float) < 46]

        job_list = []
        DF_joblist = data['岗位类别']

        for job in DF_joblist:
            job_list.append(job)
        job_set = set(job_list)

        T = './抽取结果/' + '(抽取)' + target
        writer = pd.ExcelWriter(T)

        F = 0.2
        for i in job_set:
            # print('--------------------------------')
            data1 = data[data['岗位类别'] == i]
            if 0 < data1.shape[0] < 5:
                sampled_data1 = data1.sample(n=1)
            else:
                sampled_data1 = data1.sample(frac=float(F))
            if sampled_data1.shape[0] >= 20:
                sampled_data1 = data1.sample(n = 20)
            # print(i, '人数：', sampled_data1.shape[0])
            sum_num += sampled_data1.shape[0]

            # print(sampled_data1)
            sampled_data1.to_excel(writer, sheet_name=i)
        # print('--------------------------------')
        print(target, sum_num)
        writer.close()


