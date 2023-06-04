#!/usr/bin/env bash
# Secuence
url=$1
dir=$HOME/estudio/tweepy_bot/scrapers
echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/data.txt
sed -E 's/([^A-Z])\.([^,])/\1.\n\2/g' "$dir"/data.txt > "$dir"/processed.txt
sed -E 's/([0-9]{4}\s)/\n\1/' "$dir"/processed.txt > "$dir"/processed2.txt
grep -E '[0-9]{4}\s' "$dir"/processed2.txt > "$dir"/processed3.txt
grep -v -e 'See All' -e 'SHOW' -e 'Test your knowledge' -e 'born' "$dir"/processed3.txt | grep -vE '^.{,120}$' > "$dir"/processed4.txt
sed -E 's/([0-9]{4}) /\1, /g' "$dir"/processed4.txt > "$dir"/today_in_history.txt
rm -rf "$dir"/data.txt "$dir"/processed*
