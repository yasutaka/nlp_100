echo "Input the number of lines to read from the head:"
read number_of_lines

echo `head -n $number_of_lines cols1_2.txt > head_"$number_of_lines".txt`

