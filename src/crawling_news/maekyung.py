# 매경이 전하는 세상의 지식
# 목록 URL : https://www.mk.co.kr/premium/series/20007/
# 본문 URL : https://www.mk.co.kr/premium/life/view/2021/11/31059/

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

d_month = datetime.now().month
d_day = datetime.now().day

news_dict = {}
idx = 0

list_url = 'https://www.mk.co.kr/premium/series/20007/'
response = requests.get(list_url, headers={'User-Agent': 'Mozilla/5.0'}) # header : 안티 크롤링 회피
if response.status_code == 200 :
    html = response.content.decode('euc-kr', 'replace')
    soup = BeautifulSoup(html, 'html.parser')
    
    dt_list = soup.find_all('dt', {'class' : 'tit'})
    a_list = [dt.find('a') for dt in dt_list]

    for n in a_list :
        news_dict[idx] = { 'title' : n.get_text(), 
                           'url'   : n.get('href')
                        }
        idx += 1

    for i, news in news_dict.items() :
        if f'{d_month}월 {d_day}일' in news['title'] :
            content_url = news['url']
            content_title = news['title']
            time.sleep(0.1)
            response = requests.get(content_url, headers={'User-Agent': 'Mozilla/5.0'})
            
            if response.status_code == 200 :
                html = response.content.decode('euc-kr', 'replace')
                soup = BeautifulSoup(html, 'html.parser')
                content = soup.select_one('#content > div.content_left > div.view_txt')
                print('1.' + content.get_text().split('1.')[1])
            else :
                print(response.status_code)    
            break
else :
    print(response.status_code)

