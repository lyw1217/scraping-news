# 매경이 전하는 세상의 지식
# 목록 URL : https://www.mk.co.kr/premium/series/20007/
# 본문 URL : https://www.mk.co.kr/premium/life/view/2021/11/31059/

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

d_month = datetime.now().month
d_day = datetime.now().day

list_url = 'https://www.mk.co.kr/premium/series/20007/'
response = requests.get(list_url, headers={'User-Agent': 'Mozilla/5.0'}) # header : 안티 크롤링 회피
if response.status_code == 200 :
    html = response.content.decode('euc-kr', 'replace')
    soup = BeautifulSoup(html, 'html.parser')
    #with open('list.html', 'w', encoding='utf-8') as f :
    #    f.write(str(soup))
    
    title = soup.select_one('#content > div.content_left > div.list_area2 > dl:nth-child(1) > dt > a')

    if f'{d_month}월 {d_day}일' in title.get_text() :
        content_url = title['href']
        content_title = title.get_text()
        time.sleep(0.1)
        response = requests.get(content_url, headers={'User-Agent': 'Mozilla/5.0'})
        
        if response.status_code == 200 :
            html = response.content.decode('euc-kr', 'replace')
            soup = BeautifulSoup(html, 'html.parser')
            #with open('content.html', 'w', encoding='utf-8') as f :
            #    f.write(str(soup))
            content = soup.select_one('#content > div.content_left > div.view_txt')
            print('1.' + content.get_text().split('1.')[1])


list_dict = {}
idx = 0