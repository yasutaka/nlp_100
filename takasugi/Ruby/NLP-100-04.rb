#

check_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

c = check_str.split(/[,. ]/).map{|x| x.size}.delete_if{|x| x == 0}

puts c.to_s
