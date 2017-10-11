SORTED=`sort col1.txt > sorted_col1.txt`
echo $SORTED
UNIQUE=`uniq -u sorted_col1.txt > sorted_unique_col1.txt`
echo $UNIQUE
