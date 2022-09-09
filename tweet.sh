#!/usr/bin/env bash
timestamp=$(date +"%D %T")
cd /home/sebastian/estudio/tweepy_bot
git pull origin main
python3 my_bot
git add .
git commit -m "History update: $timestamp"
git push origin main
