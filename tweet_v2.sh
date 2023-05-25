#!/usr/bin/env bash
timestamp=$(date +"%D %T")
file_path="$HOME/estudio/tweepy_bot/today_in_history.txt"
cd /home/sebastian/estudio/tweepy_bot || exit
git pull origin main
if [ -f "$file_path" ]; then
    echo "today_in_history exists. Executing my_bot_end and data cleaner."
    # Place your commands to be executed if the file exists here
    python3 my_bot_end
    rm -rf processed* data.txt today_in_history.txt
else
    echo "today_in_history does not exist. Executing tweepy_botV2 to scrape data and my_bot_start"
    # Place your commands to be executed if the file does not exist here
    ./tweepy_botV2_britannica.sh
    python3 my_bot_start
fi
git add .
git commit -m "History update: $timestamp"
git push origin main
