#

org_str = "パタトクカシーー"

puts org_str.split('').map.with_index{ |v, idx| v if idx % 2 == 0}.compact.join

