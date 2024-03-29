#!/usr/bin/env bash
# Secuence
url=$1
britannica_url="https://www.britannica.com/on-this-day"
echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > data.txt
sed -r 's/(.)([0-9]{4}\s)/\1\n\2/g' data.txt > processed.txt
sed -E 's/([^A-Z])\.([^,])/\1.\n\2/g' processed.txt > processed2.txt
grep -E '[0-9]{4}\s' processed2.txt > processed3.txt
grep -v -e 'weds' -e 'All Months' -e 'Search' -e 'Famous Kings' -e 'Divorces' -e 'Birthday' -e 'SHOW' processed3.txt | grep -vE '^.{,60}$' > processed4.txt
sed -E 's/([0-9]{4}) /\1, /g' processed4.txt > today_in_history.txt
# sed -E 's/([0-9]{4})([^s])/\1,\2/g' processed4.txt > today_in_history.txt
