#!/usr/bin/env bash
# Secuence
url=$1
dir="$HOME/estudio/tweepy_bot/scrapers"
rm -rf "$dir"/hoy_en_la_historia.txt
echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/datos.txt

# ([0-9]{3,4} -) is the pattern that matches either a 3-digit or 4-digit sequence followed by a space and a dash. The captured group is then inserted into the replacement string \n\1 to add a newline before the matched pattern.
sed -E 's/([0-9]{3,4} -)/\n\1/g' "$dir"/datos.txt > "$dir"/output.txt

# /^\s*$/ is a regular expression pattern that matches empty lines. The ^ represents the start of a line, \s* matches zero or more whitespace characters, and $ represents the end of a line.
# /d is the sed command to delete the matched lines.
sed -i '/^\s*$/d' "$dir"/output.txt

# $ matches the last line of the file.
# s/\./.\n/ finds the first occurrence of a dot (\.) on the last line and replaces it with the dot followed by a newline (.\n)
sed -i '$ s/\./.\n/' "$dir"/output.txt

grep -v -e 'See All' -e 'SHOW' -e 'Efemérides' "$dir"/output.txt | grep -vE '^.{,140}$' > "$dir"/output2.txt

#  substitution command that searches for the pattern "space-dash-space" (-) and replaces it with a comma and a space (, )
sed 's/ - /, /g' "$dir"/output2.txt > "$dir"/hoy_en_la_historia.txt

# Workspace cleanup
rm -rf "$dir"/output* "$dir"/datos*
