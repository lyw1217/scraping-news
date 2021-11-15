#!/bin/bash

SCRAPING_SVN="scraper.service"
WAIT_TIME=7

# sudo check
if [ $(id -u) -ne 0 ]; then exec sudo bash "$0" "$@"; exit; fi

echo ""
echo "-----------------------------------"
echo "          [ SCRAPER RUN ]          "
echo "-----------------------------------"
echo ""

sleep 1

cd /home/leeyw/Documents/github/scraping-news

echo "> GIT PULL"
echo ""
git pull

if [ $(systemctl is-active $SCRAPING_SVN ) == "active" ]; then
	echo "> ${SCRAPING_SVN}가 이미 구동중입니다."
	echo "> 종료 하는 중..."
	echo ""
	systemctl stop ${SCRAPING_SVN}

	for cnt in {1..${WAIT_TIME}}
	do
		echo "count : ${cnt}"
		if [ $(systemctl is-active $SCRAPING_SVN) == "unknown" ] || [ $(systemctl is-active $SCRAPING_SVN) == "inactive" ]; then
			echo "> ${SCRAPING_SVN} 종료 완료."
			echo ""
		fi
		sleep 1
	
		if [ ${cnt} == ${WAIT_TIME} ]; then
			echo "> ${SCRAPING_SVN} 종료 실패! 다시 시도하세요."
			echo ""
			exit
		fi
	done
fi

echo ""

echo "> ${SCRAPING_SVN} 시작하는 중..."
echo ""
sudo systemctl start ${SCRAPING_SVN}

for cnt in {1..${WAIT_TIME}}
do
	if [ $(systemctl is-active $SCRAPING_SVN) == "active" ]; then
		echo "> ${SCRAPING_SVN} 구동 성공!"
		echo ""
	fi
	sleep 1
	
	if [ ${cnt} == ${WAIT_TIME} ]; then
		echo "> ${SCRAPING_SVN} 구동 실패! 다시 시도하세요."
		echo ""
		exit
	fi
done

echo ""
echo "-----------------------------------"
echo "     [ SCRAPING RUN COMPLETE ]     "
echo "-----------------------------------"
echo ""

echo ""
