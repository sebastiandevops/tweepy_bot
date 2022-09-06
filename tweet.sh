#!/usr/bin/env bash
cd /home/sebastian/estudio/tweepy_bot
git pull origin main
python3 my_bot
git add .
git commit -m "History update"
git push origin main
