from app.maekyung import *
from app.slack import *
from datetime import datetime
    
def crawling_news() :
    d_month = datetime.now().month
    d_day = datetime.now().day

    status, maekyung = get_maekyung_msg(d_month, d_day)
    if status == 200 :
        #print(maekyung)
        dbout('\r\n' + maekyung)
    else :
        print(status, maekyung)

if __name__ == '__main__' :
    crawling_news()