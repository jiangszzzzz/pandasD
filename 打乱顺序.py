import pandas as pd
import os

# 读取Excel数据

for root, dirs, files in os.walk('./0919打乱/原数据'):
    for f in files:
        Excel_path = os.path.join(root, f)
        Out_path = './0919打乱/输出/' + f

        data = pd.read_excel(Excel_path)

        # 打乱数据
        data = data.sample(frac=1).reset_index(drop=True)

        ## 删除列
        # data.drop("序号", axis=1, inplace=True)

        # 修改序号
        data['序号'] = range(1, len(data) + 1)

        # 导出数据到新的Excel文件

        writer = pd.ExcelWriter(Out_path)
        data.to_excel(writer, index=False)
        writer.close()
