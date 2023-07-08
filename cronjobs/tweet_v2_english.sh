#!/usr/bin/env bash

# url to scrape data
url="https://www.britannica.com/on-this-day"

# paths
dir="$HOME/estudio/tweepy_bot"
scraper="$dir"/scrapers/britannica_scraper.sh
bot_runner="bot_english_runner.py"

# Get timestamp
timestamp=$(date +"%D %T")

# Change directory and handle potential errors
cd "$dir" || {
    echo "Failed to change directory to $dir"
    exit 1
}

# Pull changes from the current branch and check for errors
git pull origin "$(git rev-parse --abbrev-ref HEAD)"
pull_exit_code=$?
if [[ $pull_exit_code -ne 0 ]]; then
    echo "Failed to pull changes from Git. Exit code: $pull_exit_code"
    exit 1
fi

# run scraper and bot
bash "$scraper" "$url"
scraper_exit_code=$(wc -l today_in_history.txt | tr -dc '0-9')
if [[ $scraper_exit_code -ne 0 ]]; then
    echo "Failed to scrape data from url: $scraper_exit_code"
    exit 1
fi

python3 "$dir"/"$bot_runner"

# remote update
git add .
git commit -m "$bot_runner executed: $timestamp"
git push origin "$(git rev-parse --abbrev-ref HEAD)"
