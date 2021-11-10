from app import *
from threading import Thread

def get_morning_news() :
    f_send = {'maekyung' : False ,
              'hankyung' : False }

    while True :
        d_month  = datetime.now().month
        d_day    = datetime.now().day
        d_hour   = datetime.now().hour
        
        # 9시 정각에 뉴스 전송
        for key, flag in f_send.items() :
            if d_hour == 9 and flag == False :
                # 매일경제
                if key == 'maekyung' :
                    status, maekyung = get_maekyung_msg(d_month, d_day)
                    if status == 200 :
                        dbout('\r\n' + maekyung)
                    else :
                        dbout(f'\r\nStatus : {status}\nMessage : {maekyung}\n')
                    f_send[key] = True

                # 한국경제
                elif key == 'hankyung' :
                    status, hankyung = get_hankyung_issue_today()
                    if status == 200 :
                        dbout('\r\n' + hankyung)
                    else :
                        dbout(f'\r\nStatus : {status}\nMessage : {hankyung}\n')
                    f_send[key] = True

                else :
                    dbout('Err. Wrong Key.')
                time.sleep(1)
            elif d_hour == 10 :
                f_send[key] = False

        time.sleep(60)

def crawling_news() :
    th1 = Thread(target=get_morning_news)

    th1.start()
    th1.join()

if __name__ == '__main__' :
    crawling_news()