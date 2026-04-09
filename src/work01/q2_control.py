import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

df = pd.read_csv('D:/study/数据科学基础/code/data_science/src/work01/files/diabetic_data.csv')

grouped_a1c = df.groupby('A1Cresult')[['time_in_hospital', 'num_medications',
                                        'number_diagnoses', 'number_inpatient']].mean().round(2)

print("=== 第2题表格（A1Cresult分组） ===")
print(grouped_a1c)