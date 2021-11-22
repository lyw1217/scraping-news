#!/bin/bash

DIR_PATH="/home/leeyw/Documents/github/scraping-news"
LOG_PATH="${DIR_PATH}/log"
LOG_NAME="nohup.log"
VENV_PATH="${DIR_PATH}/venv/bin"
EXE_PY="${DIR_PATH}/src/main.py"
CMD="SCRAPER"
# sudo check
if [ $(id -u) -ne 0 ]; then exec sudo bash "$0" "$@"; exit; fi

echo ""
echo "--------------------------------------"
echo "          [ SCRAPER MONITOR ]         "
echo "--------------------------------------"
echo ""

echo "> 현재 구동중인 애플리케이션 pid 확인"

CURRENT_PID=$(pgrep -f ${CMD})

echo "현재 구동중인 어플리케이션 pid: $CURRENT_PID"

if [ -z "$CURRENT_PID" ]; then
    echo "> 현재 구동중인 애플리케이션이 없음"
	echo ""
else
	echo "> 정상 실행중..!"
	echo "> 모니터링 종료"
	exit 0
fi

exec ${DIR_PATH}/start
exit 0
