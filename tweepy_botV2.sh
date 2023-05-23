#!/usr/bin/env bash
# Secuence
echo $(curl --silent https://www.historynet.com/today-in-history/ | htmlq div | html2text) | tr -s ' ' | sed '/./G' > data.txt
sed -r 's/(.)([0-9]{4}\s)/\1\n\2/g' data.txt > processed.txt
grep -E '[0-9]{4}\s' processed.txt > processed2.txt
cat processed2.txt | egrep -o '^[^.]+' > processed3.txt
grep -v -e '\[' -e '\]' -e '(' -e 'Lottery' -e 'See more' processed3.txt | grep -vE '^.{,50}$' > processed4.txt
sed -E 's/([0-9]{4})([^s])/\1,\2/g' processed4.txt > today_in_history.txt
sed -i 's/$/./' today_in_history.txt
