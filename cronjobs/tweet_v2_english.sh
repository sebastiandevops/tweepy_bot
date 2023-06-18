#!/usr/bin/env bash
url="https://www.britannica.com/on-this-day"
timestamp=$(date +"%D %T")
dir="$HOME/estudio/tweepy_bot/"
cd "$dir" || exit
git pull origin feature/api_v2
bash "$dir"/scrapers/britannica_scraper.sh "$url"
python3 "$dir"/bot_english_runner.py
git add .
git commit -m "bot_english_runner executed: $timestamp"
git push origin feature/api_v2
