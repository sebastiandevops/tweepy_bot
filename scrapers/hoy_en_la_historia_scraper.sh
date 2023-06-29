#!/usr/bin/env bash
# Secuence

# Get the URL argument passed to the script
url=$1

# Define the directory path
dir="$HOME"/estudio/tweepy_bot/scrapers

# Remove the existing hoy_en_la_historia.txt file
rm -rf "$dir"/hoy_en_la_historia.txt

# Fetch the content from the given URL, convert it to plain text, remove extra spaces, and save it to data.txt
echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/data.txt

# Insert a new line before either a 2 to 4 digit number followed by a hyphen or a space, followed by a 2 to 4 digit number, followed by "a.C. -" in data.txt
sed -i -E 's/([0-9]{2,4} -| [0-9]{2,4} a\.C\. -)/\n\1/g' "$dir"/data.txt

# Remove empty lines from data.txt
sed -i '/^\s*$/d' "$dir"/data.txt

# Insert a new line after the last period in data.txt
sed -i '$ s/\./.\n/' "$dir"/data.txt

# Filter out lines containing 'See All', 'SHOW', 'Efemérides' from output.txt and remove lines shorter than or equal to 140 characters, save the result to hoy_en_la_historia.txt
grep -v -e 'See All' -e 'SHOW' -e 'Efemérides' "$dir"/data.txt | grep -vE '^.{,140}$' > "$dir"/hoy_en_la_historia.txt

# Replace ' - ' with ', ' in hoy_en_la_historia.txt
sed -i 's/ - /, /g' "$dir"/hoy_en_la_historia.txt

# removes any leading white spaces at the beginning of each line in the file.
sed -i 's/^[[:space:]]*//' "$dir"/hoy_en_la_historia.txt

# remove the content after the last dot (excluding the dot itself), but only if the line does not end with a parenthesis symbol.
sed -i -E 's/(\.[^.]*[^)])\..*/\1./' "$dir"/hoy_en_la_historia.txt

# Remove the temporary output* and datos* files
rm -rf "$dir"/data.txt
