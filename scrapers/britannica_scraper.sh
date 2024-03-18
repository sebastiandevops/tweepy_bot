# #!/usr/bin/env bash
# # Secuence
# # Get the URL argument passed to the script
# url=$1
#
# # Define the directory path
# dir="$HOME"/projects/tweepy_bot/scrapers
#
# # Fetch the content from the given URL, convert it to plain text, remove extra spaces, and save it to data.txt
# echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/data.txt
#
# # Insert a new line before the text "Sort fact from fiction" in data.txt
# sed -i '/Sort fact from fiction/s//\n&/g' "$dir"/data.txt
#
# # Insert a new line before the text "How much do you know about" in data.txt
# sed -i '/How much do you know about/s//\n&/g' "$dir"/data.txt
#
# # Insert a new line before the text "Test your knowledge" in data.txt
# sed -i '/Test your knowledge/s//\n&/g' "$dir"/data.txt
#
# # Insert a new line after the text "See All Biographies On This Day" in data.txt
# sed -i 's/See All Biographies On This Day/&\n/' "$dir"/data.txt
#
# # Insert a new line after the text "SHOW ANOTHER EVENT" in data.txt
# sed -i 's/SHOW ANOTHER EVENT/&\n/' "$dir"/data.txt
#
# # Insert a new line after periods followed by a lowercase letter and a non-comma character
# sed -i -E 's/([^A-Z])\.([^,])/\1.\n\2/g' "$dir"/data.txt
#
# # Insert a new line before a 4-digit number followed by a space
# sed -i -E 's/([0-9]{4}\s)/\n\1/' "$dir"/data.txt
#
# # Extract lines containing a 4-digit number followed by a space and save them to processed.txt
# grep -E '[0-9]{4}\s' "$dir"/data.txt > "$dir"/processed.txt
#
# # Filter out lines containing "See All Biographies" or "born" from processed.txt, and remove lines shorter than or equal to 80 characters
# grep -v -e 'See All Biographies' -e 'born' "$dir"/processed.txt | grep -vE '^.{,80}$' > "$dir"/today_in_history.txt
#
# # Add a comma after the 4-digit year in today_in_history.txt
# sed -i -E 's/([0-9]{4}) /\1, /g' "$dir"/today_in_history.txt
#
# # Remove the temporary data.txt file and all files starting with "processed" in the directory
# rm -rf "$dir"/data.txt "$dir"/processed*
#
#!/bin/bash
# Sequence
# Get the URL argument passed to the script
url=$1

# Define the directory path
dir="$HOME/projects/tweepy_bot/scrapers"

# Fetch the content from the given URL, convert it to plain text, remove extra spaces, and save it to data.txt
echo $(curl --silent "$url" | htmlq --text | html2text) | tr -s ' ' | sed '/./G' > "$dir"/data.txt

# Insert a new line before the text "Sort fact from fiction" in data.txt
sed -i '' '/Sort fact from fiction/s//\
&/g' "$dir"/data.txt

# Insert a new line before the text "How much do you know about" in data.txt
sed -i '' '/How much do you know about/s//\
&/g' "$dir"/data.txt

# Insert a new line before the text "Test your knowledge" in data.txt
sed -i '' '/Test your knowledge/s//\
&/g' "$dir"/data.txt

# Insert a new line after the text "See All Biographies On This Day" in data.txt
sed -i '' 's/See All Biographies On This Day/&\
/' "$dir"/data.txt

# # Insert a new line after the text "On this day" in data.txt
# sed -i '' 's/On this day in /&\
# /' "$dir"/data.txt

# Insert a new line after the text "SHOW ANOTHER EVENT" in data.txt
sed -i '' 's/SHOW ANOTHER EVENT/&\
/' "$dir"/data.txt

# Insert a new line after periods followed by a lowercase letter and a non-comma character
sed -i '' -E 's/([^A-Z])\.([^,])/\1.\n\2/g' "$dir"/data.txt

# Insert a new line before a 4-digit number followed by a space
sed -i '' -E 's/([[:space:]]|^)[0-9]{4}[[:space:]]/\n&/' "$dir"/data.txt

# Extract lines containing a 4-digit number followed by a space and save them to processed.txt
grep -E '[0-9]{4}\s' "$dir"/data.txt > "$dir"/processed.txt

# Filter out lines containing "See All Biographies" or "born" from processed.txt, and remove lines shorter than or equal to 80 characters
grep -v -e 'See All Biographies' -e 'Born' -e 'Take our quiz' "$dir"/processed.txt | grep -vE '^.{,80}$' > "$dir"/today_in_history.txt

# Add a comma after the 4-digit year in today_in_history.txt
sed -i '' -E 's/([0-9]{4}) /\1, /g' "$dir"/today_in_history.txt

# Remove the temporary data.txt file and all files starting with "processed" in the directory
rm -rf "$dir"/data.txt "$dir"/processed*
