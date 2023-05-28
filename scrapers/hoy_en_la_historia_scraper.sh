#!/usr/bin/env bash
# Secuence
hoy_en_la_historia="https://www.hoyenlahistoria.com/efemerides.php"
ap_news="https://apnews.com/hub/today-in-history"
on_this_day_url="https://www.onthisday.com/"
britannica_url="https://www.britannica.com/on-this-day"
dir=$HOME/estudio/tweepy_bot/scrapers
echo $(curl --silent $hoy_en_la_historia | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/datos.txt
sed -r 's/(.)([0-9]{4}\s)/\1\n\2/g' "$dir"/datos.txt > "$dir"/output.txt
sed -E 's/([^A-Z])\.([^,])/\1.\n\2/g' "$dir"/output.txt > "$dir"/output2.txt
grep -E '[0-9]{4}\s' "$dir"/output2.txt > "$dir"/output3.txt
grep -v -e 'See All' -e 'SHOW' -e 'Efemérides' "$dir"/output3.txt | grep -vE '^.{,120}$' > "$dir"/output4.txt
sed -E 's/([0-9]{4}) /\1, /g' "$dir"/output4.txt > "$dir"/output5.txt
sed 's/, - /, /g' "$dir"/output5.txt > "$dir"/hoy_en_la_historia.txt
rm -rf "$dir"/output* "$dir"/datos*
