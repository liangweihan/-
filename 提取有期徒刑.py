import os
import re
import csv

# 定義函數：根據特定條件提取句子
def extract_sentences_with_penalty(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()  # 讀取文件的每一行內容
        updated_content = []  # 儲存更新後的內容
        for line in content:
            matches = re.findall(r'處[^;]+?有期徒刑', line)  # 使用正則表達式找到匹配的句子
            if matches:
                line = line.rstrip('\n') + ',' + ','.join(matches) + '\n'  # 將找到的句子附加到每行末尾
            updated_content.append(line)  # 將更新後的行添加到列表中
        return updated_content  # 返回更新後的內容

# 定義函數：處理指定資料夾中的所有CSV文件
def process_csv_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):  # 檢查文件是否為CSV文件
            file_path = os.path.join(folder_path, filename)  # 組合文件的完整路徑
            updated_content = extract_sentences_with_penalty(file_path)  # 使用 extract_sentences_with_penalty 函數處理文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(updated_content)  # 將更新後的內容寫回原始CSV文件

# 處理當前資料夾中的所有CSV文件
process_csv_files_in_folder('.')  # 使用「.」表示當前資料夾

