import os
import glob

folder_path = '.'  # 使用相对路径，表示当前目录

# 遍历当前文件夹中的所有 CSV 文件
for file in glob.glob(os.path.join(folder_path, '*.csv')):
    file_name = os.path.basename(file)
    if '編制表' in file_name:  # 检查文件名是否包含特定词语（例如“編制表”）
        os.remove(file)  # 如果包含，删除文件
        print(f"{file_name} 已被删除")