#!/usr/bin/env bash
timestamp=$(date +"%D %T")
cd /home/sebastian/estudio/tweepy_bot || exit
git pull origin main
python3 bot_v1_runner.py
git add .
git commit -m "History update: $timestamp"
git push origin main
