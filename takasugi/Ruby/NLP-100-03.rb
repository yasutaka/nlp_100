#

org_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

puts org_str.split(/[\s,.]/).select{|s| s.size > 0}.map(&:size)

puts org_str.split(/[,. ]/).map(&:size).delete_if{|x| x == 0}

