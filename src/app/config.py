import os
import json
import platform
import logging
import logging.config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
SYS_PLATFORM = platform.system()

''' Logging Configuration '''
if SYS_PLATFORM == 'Linux' or SYS_PLATFORM == 'Drawin':
    LOGGING_PATH = os.path.join(ROOT_DIR, 'config/logging.json')
elif SYS_PLATFORM == 'Windows' :
    LOGGING_PATH = os.path.join(ROOT_DIR, 'config\logging.json')
with open(LOGGING_PATH) as json_file :
    log_configs = json.load(json_file)
    logging.config.dictConfig(log_configs)

root_logger = logging.getLogger()
'''
# USAGE
root_logger.debug("디버그")
root_logger.info("정보")
root_logger.error("오류")
'''
parent_logger = logging.getLogger("parent")
'''
# USAGE
parent_logger.debug("디버그")
parent_logger.info("정보")
parent_logger.error("오류")
'''
child_logger = logging.getLogger("parent.child")
'''
# USAGE
child_logger.debug("디버그")
child_logger.info("정보")
child_logger.error("오류")
'''

''' Main Configuration '''
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