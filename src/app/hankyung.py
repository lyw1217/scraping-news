# 한경 뉴스레터 Issue Today Preview
# URL : https://mobile.hankyung.com/apps/newsletter.view?topic=morning&gnb=
# Preview를 조회하면 당일의 Issue Today를 조회할 수 있다.

import requests
from bs4 import BeautifulSoup

def get_hankyung_issue_today() :
    """ 오늘의 Issue Today Preview 조회 """

    # 1. Issue Today Preview 조회
    list_url = 'https://mobile.hankyung.com/apps/newsletter.view?topic=morning&gnb='
    response = requests.get(list_url, headers={'User-Agent': 'Mozilla/5.0'}) # header : 안티 크롤링 회피
    if response.status_code == 200 :
        html = response.content.decode('euc-kr', 'replace')
        soup = BeautifulSoup(html, 'html.parser')
        
        print(soup.get_text())
        # 각 block을 get_text() 후 파싱
    else :
        return response.status_code, 'Err. Failed to get the Issue Today.'
