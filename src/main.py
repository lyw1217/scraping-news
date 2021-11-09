from os import stat
from app import *
from threading import Thread

def get_morning_news() :
    f_send = False

    while True :
        d_month  = datetime.now().month
        d_day    = datetime.now().day
        d_hour   = datetime.now().hour
        
        # 9시 정각에 매.세.지 전송
        if d_hour == 9 and f_send == False :
            status, maekyung = get_maekyung_msg(d_month, d_day)
            if status == 200 :
                dbout('\r\n' + maekyung)
            else :
                dbout(f'\r\nStatus : {status}\nMessage : {maekyung}\n')
            f_send = True
        elif d_hour == 10 :
            f_send = False

        time.sleep(60)

def crawling_news() :
    th1 = Thread(target=get_morning_news)
    #th2 = Thread(target=slack_socket)

    th1.start()
    #th2.start()
    th1.join()
    #th2.join()

if __name__ == '__main__' :
    crawling_news()