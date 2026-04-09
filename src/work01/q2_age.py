import pandas as pd

df = pd.read_csv('D:/study/数据科学基础/code/data_science/src/work01/files/diabetic_data.csv')

# 计算各年龄组平均值
grouped_age = df.groupby('age')[['time_in_hospital', 'num_medications',
                                 'number_diagnoses', 'number_inpatient']].mean().round(2)

print("=== 第2题表格（年龄分组） ===")
print(grouped_age)