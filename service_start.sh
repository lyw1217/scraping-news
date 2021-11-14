#!/bin/bash

CRAWLING_SVC="crawling.service"
WAIT_TIME=7

# sudo check
if [ $(id -u) -ne 0 ]; then exec sudo bash "$0" "$@"; exit; fi

echo ""
echo "----------------------------------"
echo "          [ CRAWLER RUN ]         "
echo "----------------------------------"
echo ""

sleep 1

cd /home/leeyw/Documents/github/crawling-news

echo "> GIT PULL"
echo ""
git pull

if [ $(systemctl is-active $CRAWLING_SVC ) == "active" ]; then
	echo "> ${CRAWLING_SVC}가 이미 구동중입니다."
	echo "> 종료 하는 중..."
	echo ""
	systemctl stop ${CRAWLING_SVC}

	for cnt in {1..${WAIT_TIME}}
	do
		echo "count : ${cnt}"
		if [ $(systemctl is-active $CRAWLING_SVC) == "unknown" ] || [ $(systemctl is-active $CRAWLING_SVC) == "inactive" ]; then
			echo "> ${CRAWLING_SVC} 종료 완료."
			echo ""
		fi
		sleep 1
	
		if [ ${cnt} == ${WAIT_TIME} ]; then
			echo "> ${CRAWLING_SVC} 종료 실패! 다시 시도하세요."
			echo ""
			exit
		fi
	done
fi

echo ""

echo "> ${CRAWLING_SVC} 시작하는 중..."
echo ""
sudo systemctl start ${CRAWLING_SVC}

for cnt in {1..${WAIT_TIME}}
do
	if [ $(systemctl is-active $CRAWLING_SVC) == "active" ]; then
		echo "> ${CRAWLING_SVC} 구동 성공!"
		echo ""
	fi
	sleep 1
	
	if [ ${cnt} == ${WAIT_TIME} ]; then
		echo "> ${CRAWLING_SVC} 구동 실패! 다시 시도하세요."
		echo ""
		exit
	fi
done

echo ""
echo "----------------------------------"
echo "     [ CRAWLER RUN COMPLETE ]     "
echo "----------------------------------"
echo ""

echo ""
