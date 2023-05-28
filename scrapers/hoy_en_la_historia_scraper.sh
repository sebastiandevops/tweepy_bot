#!/usr/bin/env bash
# Secuence
url=$1
dir="$HOME/estudio/tweepy_bot/scrapers"
rm -rf "$dir"/hoy_en_la_historia.txt
echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/datos.txt
sed -r 's/(.)([0-9]{4}\s)/\1\n\2/g' "$dir"/datos.txt > "$dir"/output.txt
sed -E 's/([^A-Z])\.([^,])/\1.\n\2/g' "$dir"/output.txt > "$dir"/output2.txt
grep -E '[0-9]{4}\s' "$dir"/output2.txt > "$dir"/output3.txt
grep -v -e 'See All' -e 'SHOW' -e 'Efemérides' "$dir"/output3.txt | grep -vE '^.{,120}$' > "$dir"/output4.txt
sed -E 's/([0-9]{4}) /\1, /g' "$dir"/output4.txt > "$dir"/output5.txt
sed 's/, - /, /g' "$dir"/output5.txt > "$dir"/hoy_en_la_historia.txt
rm -rf "$dir"/output* "$dir"/datos*
