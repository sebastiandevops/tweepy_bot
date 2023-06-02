#!/usr/bin/env bash
timestamp=$(date +"%D %T")
url="https://www.britannica.com/on-this-day"
dir="$HOME/estudio/tweepy_bot/scrapers"
file_path="$dir/today_in_history.txt"
cd "$HOME"/estudio/tweepy_bot || exit
git pull origin main
if [ -f "$file_path" ]; then
    echo "today_in_history exists. Executing my_bot_end and data cleaner."
    # Place your commands to be executed if the file exists here
    python3 bot_end_runner.py
    rm -rf "$dir"/processed* "$dir"/data.txt "$dir"/today_in_history.txt
    git add .
    git commit -m "My_bot_end executed: $timestamp"
    git push origin main
else
    echo "today_in_history does not exist. Executing tweepy_botV2 to scrape data and my_bot_start"
    # Place your commands to be executed if the file does not exist here
    ./scrapers/britannica_scraper.sh "$url"
    python3 bot_start_runner.py
    git add .
    git commit -m "My_bot_start executed: $timestamp"
    git push origin main
fi
