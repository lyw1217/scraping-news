# 매경이 전하는 세상의 지식
# 목록 URL : https://www.mk.co.kr/premium/series/20007/
# 본문 URL : https://www.mk.co.kr/premium/life/view/2021/11/31059/

import requests
import time
from bs4 import BeautifulSoup

def get_maekyung_msg(d_month, d_day) :
    """ {d_month}월 {d_day}일에 해당하는 매.세.지 조회 """

    news_dict = {}
    idx = 0

    # 1. 매세지 첫 page 목록 조회
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

        # 2. 날짜에 맞는 글 조회
        for i, news in news_dict.items() :
            if f'{d_month}월 {d_day}일' in news['title'] :
                content_url = news['url']
                time.sleep(0.1)
                response = requests.get(content_url, headers={'User-Agent': 'Mozilla/5.0'})
                
                if response.status_code == 200 :
                    html = response.content.decode('euc-kr', 'replace')
                    soup = BeautifulSoup(html, 'html.parser')
                    content = soup.select_one('#content > div.content_left > div.view_txt')
                    return response.status_code, ('1.' + content.get_text().split('1.')[1])
                else :
                    return response.status_code, 'Err. Failed to get the M.S.G article'
    else :
        return response.status_code, 'Err. Failed to get the M.S.G list.'