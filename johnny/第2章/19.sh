echo `cut ./output/hightemp.txt.un-tabbed.txt -f 1 -d ' ' | sort | uniq -c | sort -r > output_19.txt`
echo "done..."
