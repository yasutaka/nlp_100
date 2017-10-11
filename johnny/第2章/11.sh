FILE="./hightemp.txt"

echo `sed 's/\t/ /g' "$FILE" > "$FILE.un-tabbed.txt"`
