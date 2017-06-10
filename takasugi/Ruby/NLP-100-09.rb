#

def randamize_ary(str)
  str.shuffle!
end

def randamize(word)
  return word if word.length < 5

  ary = word.chars

  head = ary.shift
  tail = ary.pop

  body = randamize_ary(ary)

  out = body.unshift(head)
  out << tail

  out.join
end

puts randamize('123')

puts randamize('a123b')

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

n_sntc = sentence.split(/ /)
out = n_sntc.map{|w| randamize(w)}

puts out.join(' ')
