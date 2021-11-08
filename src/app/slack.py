import os
from slacker import Slacker
from datetime import datetime
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
SECRETS_PATH = os.path.join(ROOT_DIR, '.config_secret/keys.json')

secrets = json.loads(open(SECRETS_PATH).read())

for key, value in secrets.items() :
    # slack_key 가져오기
    if key == 'SLACK_KEY' :
        slack = Slacker(value)

def dbout(message, *args):
    """인자로 받은 문자열을 파이썬 셸과 슬랙으로 동시에 출력한다."""
    tmp_msg = message
    for text in args:
        tmp_msg += str(text)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S] ') + tmp_msg
    print(strbuf)
    slack.chat.post_message('#python-trading-bot', strbuf)