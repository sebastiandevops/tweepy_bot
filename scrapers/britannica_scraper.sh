#!/usr/bin/env bash
# Secuence
url=$1
dir="$HOME"/estudio/tweepy_bot/scrapers
echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/data.txt
sed -i '/Sort fact from fiction/s//\n&/g' data.txt
sed -i '/How much do you know about/s//\n&/g' data.txt
sed -i '/Test your knowledge/s//\n&/g' data.txt
sed -i 's/See All Biographies On This Day/&\n/' data.txt
sed -i -E 's/([^A-Z])\.([^,])/\1.\n\2/g' "$dir"/data.txt
sed -i -E 's/([0-9]{4}\s)/\n\1/' "$dir"/data.txt
grep -E '[0-9]{4}\s' "$dir"/data.txt > "$dir"/processed.txt
grep -v -e 'See All Biographies' -e 'born' "$dir"/processed.txt | grep -vE '^.{,80}$' > "$dir"/today_in_history.txt
sed -i -E 's/([0-9]{4}) /\1, /g' "$dir"/today_in_history.txt
rm -rf "$dir"/data.txt "$dir"/processed*
