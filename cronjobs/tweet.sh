#!/usr/bin/env bash
timestamp=$(date +"%D %T")
dir="$HOME/estudio/tweepy_bot/"
cd "$dir" || exit
git pull origin main
python3 "$dir"/bot_v1_runner.py
git add .
git commit -m "History update: $timestamp"
git push origin main