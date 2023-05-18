#!/bin/bash
today_date=$(date +%Y%m%d)
echo $today_date

echo "Run script launched"
/etc/init.d/cron start

app_location="/Users/achintyaranjanchaudhary/Documents/projects/casfinserv"
echo 'running app now'
python3 ${app_location}/boot_script/check_scheduler.py
#python3 ${app_location}/DataService/src/app.py | tee
#while true; do sleep 1000; done
