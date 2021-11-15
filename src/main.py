from app import *
from threading import Thread

def get_morning_news() :
    root_logger.critical("< NEWS > get_morning_new Thread Started ... ")

    while True :
        d_month  = datetime.now().month
        d_day    = datetime.now().day
        d_hour   = datetime.now().hour
        
        # 정해진 시간에 뉴스 전송
        for key, flag in f_send.items() :
            child_logger.debug("< NEWS > running... ")
            if d_hour == SEND_HOUR and flag == True :
                # 매일경제
                if key == 'maekyung' :
                    status, maekyung = get_maekyung_msg(d_month, d_day)
                    if status == 200 :
                        dbout('\r\n' + maekyung)
                        parent_logger.info("< NEWS > Success get_maekyung_msg()... ")
                    else :
                        dbout(f'\r\nStatus : {status}\nMessage : {maekyung}\n')
                        root_logger.warning(f'Status : {status}\nMessage : {maekyung}')
                    f_send[key] = False

                # 한국경제
                elif key == 'hankyung' :
                    status, hankyung = get_hankyung_issue_today()
                    if status == 200 :
                        dbout('\r\n' + hankyung)
                        parent_logger.info("< NEWS > Success get_hankyung_issue_today()... ")
                    else :
                        dbout(f'\r\nStatus : {status}\nMessage : {hankyung}\n')
                        root_logger.warning(f'Status : {status}\nMessage : {hankyung}')
                    f_send[key] = False

                else :
                    dbout('Err. Wrong Key.')
                    root_logger.warning('< NEWS > Err. Wrong Key.')
                time.sleep(1)
            elif d_hour != SEND_HOUR :
                f_send[key] = True

        time.sleep(60)

def crawling_news() :
    th1 = Thread(target=get_morning_news)

    th1.start()
    th1.join()

if __name__ == '__main__' :
    root_logger.critical("============================================")
    root_logger.critical("")
    root_logger.critical("       < S C R A P E R >    S T A R T       ")
    root_logger.critical("                            written by ywlee")
    root_logger.critical("============================================")
    crawling_news()