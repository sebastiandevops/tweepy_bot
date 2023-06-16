#!/usr/bin/env bash
url="https://www.britannica.com/on-this-day"
timestamp=$(date +"%D %T")
cd "$HOME"/estudio/tweepy_bot || exit
git pull origin feature/api_v2
./scrapers/britannica_scraper.sh "$url"
python3 bot_english_runner.py
git add .
git commit -m "bot_english_runner executed: $timestamp"
git push origin feature/api_v2
