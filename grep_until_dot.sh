#!/bin/bash

# Get the input file name
file_name=$1

# Read the input file
lines=$(<"$file_name")

# Create a new output file
new_file_name="output.txt"

# Iterate over the lines in the input file
for line in $lines; do

  # If the line contains a dot not preceded by an uppercase letter and not followed by a comma,
  # then insert a new line after the dot.
  if [[ $line =~ ^[^A-Z]\.(?!,|$) ]]; then
    line="${line%.}\n${line##*.}"
  fi

  # Write the line to the output file
  echo "$line" >>"$new_file_name"

done

# Close the output file
close "$new_file_name"
