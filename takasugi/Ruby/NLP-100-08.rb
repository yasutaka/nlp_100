#

def cipher(str)
  ary = str.split('')

  ary.map { |c|
    if c =~ /[a-z]/
      (219-c.ord).chr
    else
      c
    end
    }.join
end

encode = cipher('AbCdEfG1Uu')
decode = cipher(encode)

puts encode
puts decode


