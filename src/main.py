from app import *
from threading import Thread

''' Load Configuration '''
if SYS_PLATFORM == 'Linux' or SYS_PLATFORM == 'Drawin':
    CONFIG_PATH = os.path.join(ROOT_DIR, 'config/config.json')
elif SYS_PLATFORM == 'Windows' :
    CONFIG_PATH = os.path.join(ROOT_DIR, 'config\config.json')

with open(CONFIG_PATH) as json_file :
    configs = json.load(json_file)
    f_send = {}

    SEND_HOUR = int(configs['SEND_HOUR'])            
    for n in configs['news'] :
        if n['name'] == 'maekyung' :
            f_send['maekyung']  = n['send_flag']
        elif n['name'] == 'hankyung' :
            f_send['hankyung']  = n['send_flag']
''''''

def get_morning_news() :

    while True :
        d_month  = datetime.now().month
        d_day    = datetime.now().day
        d_hour   = datetime.now().hour
        
        # 9시 정각에 뉴스 전송
        for key, flag in f_send.items() :
            if d_hour == SEND_HOUR and flag == False :
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
            elif d_hour != SEND_HOUR :
                f_send[key] = False

        time.sleep(60)

def crawling_news() :
    th1 = Thread(target=get_morning_news)

    th1.start()
    th1.join()

if __name__ == '__main__' :
    crawling_news()