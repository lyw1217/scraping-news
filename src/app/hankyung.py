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
        
        td_list = soup.find_all('td', {'class' : 'stb-text-box'})
        txt_list = [td.get_text() for td in td_list]
        
        for t in txt_list[:] :
            if '이 뉴스레터를 카카오톡으로 공유하세요!' in t :
                txt_list.remove(t)
                break
            
        return response.status_code, '\r\n'.join(txt_list)

    else :
        return response.status_code, 'Err. Failed to get the Issue Today.'