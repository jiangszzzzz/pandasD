import pandas as pd
import os

target_dir = input('请输入要合并excel文件的目录：')
filename = input('请输入要保存excel文件的文件名：')
Sheet_name= input('请输入要保存的Sheet名字：')
files = [
    pd.read_excel(os.path.join(target_dir, file)) for file in os.listdir(target_dir) if file.endswith('.xlsx')
]
# 若Excel表中存在多个Sheet表，需指定需要合并的Sheet表名
# files = [pd.read_excel(os.path.join(target_dir, file), sheet_name='demo') for file in os.listdir(target_dir) if file.endswith('.xlsx')]
# 选择所需要的列，如果是一列，则只需传入一个列名；如果同时选择多列，则传入多个列名即可，多个列名用列表形式封存
# files = [pd.read_excel(os.path.join(target_dir, file), sheet_name='demo')[['date','city']] for file in os.listdir(target_dir) if file.endswith('.xlsx')]
# 如果多个excel文件中的列名一致，则不需此项
writer = pd.ExcelWriter(f'{filename}.xlsx')
pd.concat(files).to_excel(writer, Sheet_name, index=False)
writer.save()