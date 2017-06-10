#
require 'pry'

module NLP100
  class << self
    def make_n_gram(obj, n_gram = 1)
      ary = obj
      if obj.is_a? String
        ary = obj.split('')
      end
      
      max = ary.size - n_gram

      if obj.is_a? String
        0.upto(max).map{ |c| ary[c...(n_gram + c)].join }
      else
        0.upto(max).map{ |c| ary[c...(n_gram + c)] }
      end
    end
  end
end

str = "012345678"
binding.pry
puts NLP100.make_n_gram(str, 2)

ary = %w[abc bcd cde def]

puts NLP100::make_n_gram(ary, 2).to_s

p_str = "I am a NLPer"
puts NLP100::make_n_gram(p_str.gsub(' ', ''), 2)
puts NLP100::make_n_gram(p_str.split(' '), 2).to_s

