import pandas as pd
import os

if os.path.exists('./抽取结果'):
    pass
else:
    os.mkdir('./抽取结果')

while True:
    try:
        target = input('请输入地市并回车：')
        sum_num = 0
        if target == '':
            continue
        # target = '6.荆州'
        target_dir = './地市/' + target + '.xlsx'
        data = pd.read_excel(target_dir)
        # print(data.shape)
        data = data[data['年龄（周岁）']<46]
        # print(data.shape)
        job_list = []
        DF_joblist = data['岗位类别']

        for job in DF_joblist:
            job_list.append(job)
        job_set = set(job_list)
        # print('该地市有如下岗位:')
        # print(job_set)

        T = './抽取结果/' + '(抽取)' + target + '.xlsx'
        writer = pd.ExcelWriter(T)

        # F = input('请输入抽取比例，并回车完成抽取：')
        F = 0.2
        for i in job_set:
            print('--------------------------------')
            data1 = data[data['岗位类别'] == i]
            if 0< data1.shape[0] < 5:
                sampled_data1 = data1.sample(n = 1)
            else:
                sampled_data1 = data1.sample(frac=float(F))

            if sampled_data1.shape[0] >= 20:
                sampled_data1 = data1.sample(n=20)
            sum_num += sampled_data1.shape[0]
            print(i,'人数：',sampled_data1.shape[0])
            print(sampled_data1)
            sampled_data1.to_excel(writer,sheet_name=i)
        print(target,'总人数：',sum_num)
        print('--------------------------------')
        writer.close()
        input("抽取结束，请按下回车键继续...")
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        break