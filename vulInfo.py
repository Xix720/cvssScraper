from concurrent.futures.thread import ThreadPoolExecutor
import re

import requests
from bs4 import BeautifulSoup


class CvssBoxScraper:
    def __init__(self, url):
        self.url = url

    def get_cvss_score_10(self):
        scores = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/91.0.4472.124 Safari/537.36'
        }
        print("正在发送请求")

        def fetch_url(url):
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                print(url + " :请求成功，正在解析响应")
                soup = BeautifulSoup(response.text, 'html.parser')
                cveId = soup.find('h2', class_=lambda value: value and value.startswith('mt-4'))
                cvss_box = soup.find('div', class_=lambda value: value and value.startswith('cvssbox score'))
                vulInfo = str(cveId.text.strip())+": "+str(cvss_box.text.strip())

                if cveId and cvss_box:
                    scores.append(vulInfo)
                else:
                    print("未找到指定的元素")
            else:
                print(f"请求失败，状态码: {response.status_code}")

        with ThreadPoolExecutor() as executor:
            executor.map(fetch_url, self.url)

        return scores
