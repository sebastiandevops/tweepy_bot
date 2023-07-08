#!/usr/bin/env bash
# #!/usr/bin/env bash
# Script to process historical events from a website

# Set the URL argument passed to the script
url=$1

# Define the directory path
dir=$(pwd)

# Remove the existing hoy_en_la_historia.txt file
rm -rf "$dir"/hoy_en_la_historia.txt

# Fetch the content from the given URL, convert it to plain text, remove extra spaces, and save it to data.txt
echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/data.txt

# Insert a new line after the "Efemérides por día" line in data.txt
sed -i '/Efemérides por día/s//\n&/g' "$dir"/data.txt

# Insert a new line after the "Todos los tiposEfeméridesCumpleañosMuertes" line in data.txt
sed -i 's/Todos los tiposEfeméridesCumpleañosMuertes/&\n/g' "$dir"/data.txt

# Filter out unwanted lines from data.txt and save the filtered result to hoy_en_la_historia.txt
grep -v -e 'tiposEfeméridesCumpleañosMuertes' -e 'Efemérides de Hoy' -e 'Hoyenlahistoria.com' "$dir"/data.txt | grep -vE '^.{,80}$' > "$dir"/hoy_en_la_historia.txt

# insert a new line after every dot (.) followed by a space and a 2, 3, or 4-digit sequence number
sed -i 's/\.\s\([0-9]\{2,4\}\)/.\n\1/g' "$dir"/hoy_en_la_historia.txt

# Remove empty lines from data.txt
sed -i '/^\s*$/d' "$dir"/hoy_en_la_historia.txt

# Insert a new line after the last period in data.txt
sed -i '$ s/\./.\n/' "$dir"/hoy_en_la_historia.txt

# Remove lines with less than or equal to 20 characters from hoy_en_la_historia.txt
sed -i '/^.\{0,20\}$/d' "$dir"/hoy_en_la_historia.txt

# inserts a comma after the year
sed -i -E ':a; s/([0-9]{2,4}) /\1, /; t; n; ba' "$dir"/hoy_en_la_historia.txt

# remove all possible spaces at the end of the line
sed -i 's/ *$//' "$dir"/hoy_en_la_historia.txt

# removes any leading white spaces at the beginning of each line in the file.
sed -i 's/^[[:space:]]*//' "$dir"/hoy_en_la_historia.txt

# Remove the temporary output* and datos* files
rm -rf "$dir"/data.txt
