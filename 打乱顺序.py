import pandas as pd
import os
from styleframe import StyleFrame, Styler, utils
from openpyxl.utils import get_column_letter
from openpyxl import Workbook

# 读取Excel数据

for root, dirs, files in os.walk('./0919打乱/原数据'):
    for f in files:
        Excel_path = os.path.join(root, f)
        Out_path = './0919打乱/输出/' + f
        writer = pd.ExcelWriter(Out_path)
        writer1 = StyleFrame.ExcelWriter(Out_path)

        # 遍历excel 中的所有sheet
        data = pd.read_excel(Excel_path, sheet_name=None)
        sheet_list = list(data)

        for sheet_name in list(data):
            data = pd.read_excel(Excel_path, sheet_name=sheet_name)

            for column, value in data.items():
                print(f"Column: {column}")
                # print(value)

            # 打乱数据
            data = data.sample(frac=1).reset_index(drop=True)

            ## 删除列
            # data.drop("序号", axis=1, inplace=True)

            # 修改序号
            data['序号'] = range(1, len(data) + 1)

            # 导出数据到新的Excel文件
            data.to_excel(writer, sheet_name=sheet_name, index=False)

            sf = StyleFrame(data)
            sf.apply_column_style(cols_to_style=data.columns,
                                  styler_obj=Styler(bg_color=utils.colors.white, bold=False, font=utils.fonts.arial,
                                                    font_size=14), style_header=True)
            sf.apply_headers_style(
                styler_obj=Styler(bg_color=utils.colors.white, bold=True, font_size=14, font_color=utils.colors.black,
                                  number_format=utils.number_formats.general, protection=False))
            sf.to_excel(writer1, sheet_name=sheet_name)

        writer.close()
        writer1.close()
