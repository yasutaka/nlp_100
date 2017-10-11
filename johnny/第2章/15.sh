echo "Input the number of lines to read from the tail:"
read number_of_lines

echo `tail -n $number_of_lines cols1_2.txt > tail_"$number_of_lines".txt`

