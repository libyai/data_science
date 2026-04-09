import pandas as pd

# 1. 读取数据
df = pd.read_csv('D:/study/数据科学基础/code/data_science/src/work01/files/diabetic_data.csv')

# 2. age 转成数值中点（方便求平均）
age_mapping = {
    '[0-10)': 5,   '[10-20)': 15,  '[20-30)': 25,  '[30-40)': 35,
    '[40-50)': 45, '[50-60)': 55,  '[60-70)': 65,  '[70-80)': 75,
    '[80-90)': 85, '[90-100)': 95
}
df['age_numeric'] = df['age'].map(age_mapping)

# 3. 选特征做平均值表格（包含你想要的全部）
features = ['time_in_hospital', 'num_medications', 'number_inpatient',
            'num_lab_procedures', 'number_diagnoses', 'age_numeric']

grouped = df.groupby('readmitted')[features].mean().round(2)

# 重命名列（韩文，便于直接复制到报告）
grouped.columns = ['平均入院天数', '平均吃药数量', '平均过去入院次数',
                   '平均检查数量', '平均诊断数量', '平均年龄(中点)']

print("\n=== 第1题推荐表格（直接复制到Word） ===")
print(grouped)