import os
import csv

folder_path = '.'  # 使用相對路徑，表示當前目錄

# 遍歷當前資料夾中的所有 CSV 檔案
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)

        # 讀取 CSV 檔案內容
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        # 刪除包含「,無法獲取條文內容」的列
        cleaned_rows = [row for row in rows if 'Law Number' not in row]

        # 寫入更新後的 CSV 檔案
        with open(file_path, mode='w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(cleaned_rows)

        print(f"已刪除 {file_name} 中包含「,無法獲取條文內容」的列")
