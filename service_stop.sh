#!/bin/bash

CRAWLING_SVC="crawling.service"
WAIT_TIME=7

# sudo check
if [ $(id -u) -ne 0 ]; then exec sudo bash "$0" "$@"; exit; fi
echo ""
echo "--------------------------"
echo "     [ CRAWLING STOP ]     "
echo "--------------------------"
echo ""

sleep 0.5

echo ""

if [ $(systemctl is-active $CRAWLING_SVC ) == "active" ]; then
	echo "> ${CRAWLING_SVC}가 이미 구동중입니다."
	echo "> 종료 하는 중..."
	systemctl stop ${CRAWLING_SVC}
	
	for cnt in {1..${WAIT_TIME}}
	do
		if [ $(systemctl is-active $CRAWLING_SVC) == "unknown" ] || [ $(systemctl is-active $CRAWLING_SVC) == "inactive" ]; then
			echo "> ${CRAWLING_SVC} 종료 완료."
		fi
		sleep 1
	
		if [ ${cnt} == ${WAIT_TIME} ]; then
			echo "> ${CRAWLING_SVC} 종료 실패! 다시 시도하세요."
			exit
		fi
	done
else
	echo "> ${CRAWLING_SVC}가 구동중이지 않습니다."
fi

echo ""

