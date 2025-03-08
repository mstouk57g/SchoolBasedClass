import pandas as pd

# 读取第一个文件
file1 = "2023级高二校本成绩.xlsx"
df1 = pd.read_excel(file1)

# 读取第二个文件
file2 = "高一高二非高考科目期中、期末成绩登记表.xlsx"
df2 = pd.read_excel(file2)

# 将第一个文件中的姓名和成绩存储为字典
name_to_score = dict(zip(df1.iloc[:, 1], df1.iloc[:, 2]))  # 第2列是姓名，第3列是成绩

# 更新第二个文件中的成绩
for index, row in df2.iterrows():
    name = row[1]  # 第2列是姓名
    if name in name_to_score:
        df2.at[index, df2.columns[3]] = name_to_score[name]  # 第4列是成绩

# 保存更新后的第二个文件
output_file = "高一高二非高考科目期中、期末成绩登记表.xlsx"
df2.to_excel(output_file, index=False)

print(f"更新完成！结果已保存到 {output_file}")
