#!/usr/bin/env bash
timestamp=$(date +"%D %T")
cd /home/sebastian/estudio/tweepy_bot || exit
git pull origin main
python3 my_bot_end
rm -rf processed* data.txt today_in_history.txt
git add .
git commit -m "History update: $timestamp"
git push origin main
