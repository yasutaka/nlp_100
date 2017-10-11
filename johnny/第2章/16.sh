echo "Input the number of lines per file:"
read number_of_lines

echo `split -l $number_of_lines cols1_2.txt file-`

