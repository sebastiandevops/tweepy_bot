#!/usr/bin/env bash
url="https://www.britannica.com/on-this-day"
timestamp=$(date +"%D %T")
dir="$HOME/estudio/tweepy_bot"
scraper="$dir"/scraper/britannica_scraper.sh
bot_runner="bot_english_runner.py"
branch="api_v2"

cd "$dir" || exit
git pull origin "$branch"
bash "$scraper" "$url"
python3 "$dir"/"$bot_runner"
git add .
git commit -m "$bot_runner executed: $timestamp"
git push origin "$branch"
