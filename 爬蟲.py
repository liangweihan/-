import requests
from bs4 import BeautifulSoup
import re
import csv
import os

def scrape_all_laws(new_link, text):  # 修改参数以接收 new_link 和 text
    response = requests.get(new_link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        laws = soup.find_all('div', class_='row')

        file_exists = os.path.isfile(f'{text}.csv')  # 检查以 text 变量为文件名的文件是否存在

        with open(f'{text}.csv', mode='w+', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['Law Number', 'Law Content']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:  # 如果檔案不存在，寫入標題
                writer.writeheader()

            for law in laws:
                law_link = law.find('a')  # 找到包含條文編號和連結的<a>標籤
                if law_link:
                    law_number = law_link.text.strip()
                    law_url = f"https://law.moj.gov.tw/LawClass/{law_link.get('href')}"  # 取得條文連結
                    law_content = scrape_specific_law(law_url)
                    if law_content:
                        writer.writerow({'Law Number': law_number, 'Law Content': law_content})
                    else:
                        writer.writerow({'Law Number': law_number, 'Law Content': '無法獲取條文內容'})
    else:
        print("無法獲取頁面")

def scrape_specific_law(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        law_content = soup.find('div', class_='law-article')
        if law_content:
            return law_content.text.strip()
        else:
            return None
    else:
        return None

# 发送请求获取网页内容
url = 'https://law.moj.gov.tw/Law/LawSearchLaw.aspx?TY=04052012'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 找到所有符合条件的链接并提取最后一串代码和链接后面的文字
links = soup.find_all('a', {'id': 'hlkLawName'})
for link in links:
    href = link.get('href')
    text = link.text  # 获取链接后面的文字
    code = re.search(r'PCode=(\w+)', href)
    if code:
        code = code.group(1)
        new_link = f'https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode={code}'
        print(f"链接：{new_link}, 文字：{text}")
        # 使用 text 变量的值作为文件名来调用函数
        scrape_all_laws(new_link, text)  # 将 new_link 和 text 传递给函数





