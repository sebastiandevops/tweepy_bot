#!/usr/bin/env bash

# url to scrape data
url="https://www.hoyenlahistoria.com/efemerides.php"

# paths
dir="$HOME/estudio/tweepy_bot"
file_path="$dir"/scrapers/hoy_en_la_historia.txt
scraper="$dir"/scrapers/hoy_en_la_historia_scraper.sh

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

# Check if file exists
# if [ -f "$file_path" ]; then
#     echo "hoy_en_la_historia exists. Executing my_bot_end and data cleaner."
#     # Place your commands to be executed if the file exists here
#     python3 "$dir"/bot_end_runner.py
#     rm -rf "$file_path"
#     git add .
#     git commit -m "My_bot_end executed: $timestamp"
#     git push origin "$(git rev-parse --abbrev-ref HEAD)"
# else
#     echo "hoy_en_la_historia does not exist. Executing tweepy_botV2 to scrape data and my_bot_start"
#     # Place your commands to be executed if the file does not exist here
#     bash "$scraper" "$url"
#     python3 "$dir"/bot_start_runner.py
#     scraper_exit_code=$(wc -l hoy_en_la_historia.txt | tr -dc '0-9')
#     if [[ $scraper_exit_code -ne 0 ]]; then
#         echo "Failed to scrape data from url: $scraper_exit_code"
#         exit 1
#     fi
#     git add .
#     git commit -m "My_bot_start executed: $timestamp"
#     git push origin "$(git rev-parse --abbrev-ref HEAD)"
# fi


# Check if file exists
echo "Executing tweepy_botV2 to scrape data, my_bot_end and data cleaner."
bash "$scraper" "$url"
python3 "$dir"/bot_end_runner.py
rm -rf "$file_path"
git add .
git commit -m "My_bot_end executed: $timestamp"
git push origin "$(git rev-parse --abbrev-ref HEAD)"
