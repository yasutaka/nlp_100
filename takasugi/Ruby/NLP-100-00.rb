#

check_str = "stressed"
out_str = ""
(0..check_str.length - 1).each{|i| out_str += check_str[check_str.length - 1 - i]}

puts out_str

# OR
puts check_str.reverse

