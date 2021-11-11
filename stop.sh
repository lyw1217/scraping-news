#!/bin/bash

DIR_PATH="/home/leeyw/문서/github/crawling-news"
LOG_PATH="${DIR_PATH}/log"
LOG_NAME="nohup.log"
VENV_PATH="${DIR_PATH}/venv/bin"
EXE_PY="${DIR_PATH}/src/main.py"
CMD="CRAWLER"
WAIT_TIME=7

# sudo check
if [ $(id -u) -ne 0 ]; then exec sudo bash "$0" "$@"; exit; fi

echo ""
echo "----------------------------------"
echo "         [ CRAWLER STOP ]         "
echo "----------------------------------"
echo ""

sleep 0.5

echo "> 현재 구동중인 애플리케이션 pid 확인"
echo ""
sleep 0.5

CURRENT_PID=$(pgrep -f ${CMD})

echo "현재 구동중인 어플리케이션 pid: $CURRENT_PID"
sleep 0.5
if [ -z "$CURRENT_PID" ]; then
    echo "> 현재 구동중인 애플리케이션이 없으므로 종료하지 않습니다."
else
    echo "> kill -15 $CURRENT_PID"
    kill -15 $CURRENT_PID
	sleep 0.5
	
	for cnt in {1..${WAIT_TIME}}
	do
		CURRENT_PID=$(pgrep -f ${CMD})
		if [ -z "$CURRENT_PID" ]; then
			echo "> 어플리케이션 종료 성공!"
			echo ""
			break
		fi
		sleep 0.5
		
		if [ ${cnt} == ${WAIT_TIME} ]; then
			echo "> 어플리케이션 종료 실패.. 다시 시도하세요"
			echo ""
			exit 1
		fi
	done
fi

echo ""
echo "----------------------------------"
echo "    [ CRAWLER STOP COMPLETE ]     "
echo "----------------------------------"
echo ""

echo ""
exit 0
