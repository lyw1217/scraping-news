#!/bin/bash

SCRAPING_SVN="scraping.service"
WAIT_TIME=7

# sudo check
if [ $(id -u) -ne 0 ]; then exec sudo bash "$0" "$@"; exit; fi
echo ""
echo "--------------------------"
echo "     [ SCRAPING STOP ]     "
echo "--------------------------"
echo ""

sleep 0.5

echo ""

if [ $(systemctl is-active $SCRAPING_SVN ) == "active" ]; then
	echo "> ${SCRAPING_SVN}가 이미 구동중입니다."
	echo "> 종료 하는 중..."
	systemctl stop ${SCRAPING_SVN}
	
	for cnt in {1..${WAIT_TIME}}
	do
		if [ $(systemctl is-active $SCRAPING_SVN) == "unknown" ] || [ $(systemctl is-active $SCRAPING_SVN) == "inactive" ]; then
			echo "> ${SCRAPING_SVN} 종료 완료."
		fi
		sleep 1
	
		if [ ${cnt} == ${WAIT_TIME} ]; then
			echo "> ${SCRAPING_SVN} 종료 실패! 다시 시도하세요."
			exit
		fi
	done
else
	echo "> ${SCRAPING_SVN}가 구동중이지 않습니다."
fi

echo ""

