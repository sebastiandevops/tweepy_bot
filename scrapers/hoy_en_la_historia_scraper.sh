#!/usr/bin/env bash
# Secuence
hoy_en_la_historia="https://www.hoyenlahistoria.com/efemerides.php"
ap_news="https://apnews.com/hub/today-in-history"
on_this_day_url="https://www.onthisday.com/"
britannica_url="https://www.britannica.com/on-this-day"
echo $(curl --silent $hoy_en_la_historia | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > datos.txt
sed -r 's/(.)([0-9]{4}\s)/\1\n\2/g' datos.txt > output.txt
sed -E 's/([^A-Z])\.([^,])/\1.\n\2/g' output.txt > output2.txt
grep -E '[0-9]{4}\s' output2.txt > output3.txt
grep -v -e 'See All' -e 'SHOW' -e 'Efemérides' output3.txt | grep -vE '^.{,120}$' > output4.txt
sed -E 's/([0-9]{4}) /\1, /g' output4.txt > output5.txt
sed 's/, - /, /g' output5.txt > hoy_en_la_historia.txt
rm -rf output* datos*
