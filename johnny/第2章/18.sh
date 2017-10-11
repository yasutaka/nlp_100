FILE="./hightemp.txt.un-tabbed.txt"
echo `sort -k3,3 $FILE > sorted_third_column.txt`
echo "done..."
