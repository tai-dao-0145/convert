import pandas as pd

# Đọc file excel vào DataFrame
data_frame = pd.read_excel('dataExcel/data_cv.xlsx')
# Khởi tạo một list rỗng để lưu giá trị cho cột mới
values_for_new_column = []
i = 1
for value in data_frame['Word']:
    values_for_new_column.append(i)
    if value == ".":
        i = i + 1
# Thêm cột mới với tên là 'Ten_cot_moi' và giá trị được lưu trong list 'values_for_new_column'
data_frame['Sentence #'] = values_for_new_column

# Lưu DataFrame đã được thêm cột mới vào file Excel
data_frame.to_excel('dataExcel/new_data.xlsx', index=False)