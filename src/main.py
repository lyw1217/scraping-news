from app import *
from datetime import datetime
from threading import Thread
import time

def maekyung() :
    f_send = False
    '''
    channels = get_channel_list()
    print(type(channels))

    for channel in channels.body['channels'] :
        print(channel)
        if channels['name'] == CHANNEL_NAME :
            id = channel['id']
            break        

    print(id)
    '''
    while True :
        d_month  = datetime.now().month
        d_day    = datetime.now().day
        d_hour   = datetime.now().hour
        
        # 8시 정각에 메시지 전송
        if d_hour == 8 and f_send == False :
            status, maekyung = get_maekyung_msg(d_month, d_day)
            if status == 200 :
                dbout('\r\n' + maekyung)
                f_send = True
            else :
                dbout(f"Status : {status}\r\nMessage : {maekyung}")
                f_send = True
        elif d_hour == 9 :
            f_send = False

        status, maekyung = get_maekyung_msg(d_month, d_day)
        if status == 200 :
            dbout('\r\n' + maekyung)
            f_send = True
        time.sleep(60)

def crawling_news() :
    th1 = Thread(target=maekyung)
    #th2 = Thread(target=slack_socket)

    th1.start()
    #th2.start()
    th1.join()
    #th2.join()

if __name__ == '__main__' :
    crawling_news()