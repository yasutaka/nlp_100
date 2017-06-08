#

org_str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

t_idx = [1, 5, 6, 7, 8, 9, 15, 16, 19]
h =  org_str.split(/[,. ]/).map.with_index do |x, idx|
  case idx
  when *t_idx
    [x[0], idx]
  else
    [x[0..1], idx]
  end
end

puts h.to_h

