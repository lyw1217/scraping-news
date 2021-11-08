import os
from slacker import Slacker
from datetime import datetime
import json
import websocket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
SECRETS_PATH = os.path.join(ROOT_DIR, '.config_secret/keys.json')

CHANNEL_NAME = '#python-trading-bot'
#CHANNEL_NAME = '#crawling-news'
secrets = json.loads(open(SECRETS_PATH).read())

for key, value in secrets.items() :
    # slack_key 가져오기
    if key == 'SLACK_KEY' :
        slack = Slacker(value)
    elif key == 'SLACK_APP_TOKEN' :
        slack_sock = Slacker(value)

def dbout(message, *args) :
    """인자로 받은 문자열을 파이썬 셸과 슬랙으로 동시에 출력한다."""
    tmp_msg = message
    for text in args:
        tmp_msg += str(text)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S] ') + tmp_msg
    print(strbuf)
    slack.chat.post_message(CHANNEL_NAME, strbuf)

def get_channel_list() :
    """ slack 채널 리스트를 가져온다. return value : dict """
    channel_list = slack.conversations.list()
    return channel_list

def get_conv_history(id) :
    """ channel에서 id를 이용하여 대화 내용을 읽어온다. return value : list """
    msgs = slack.conversations.history(id)
    return msgs

def slack_socket() :
    res = slack_sock.rtm.connect()
    endpoint = res.body['url']

    ws = websocket.create_connection(endpoint)
    ws.settimeout(60)

    while True :
        try :
            msg = json.loads(ws.recv())
            print(msg)
        except websocket.WebSocketTimeoutException :
            ws.send(json.dumps({'type': 'ping'}))
        except websocket.WebSocketConnectionClosedException :
            print("Connection closed")
            break
        except Exception as e:
            print(e)
            break
    ws.close()