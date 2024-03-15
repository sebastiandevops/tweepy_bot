#!/usr/bin/env bash

timestamp=$(date +"%D %T")
dir="$HOME/projects/tweepy_bot/"
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

python3 "$dir"/bot_v1_runner.py

git add .
git commit -m "History updated: $timestamp"
git push origin "$(git rev-parse --abbrev-ref HEAD)"
