#

require './NLP-100-05.rb'

x_str = "paraparaparadise"
y_str = "paragraph"

x = NLP100::make_n_gram(x_str, 2)
y = NLP100::make_n_gram(y_str, 2)

puts x
puts y

puts x + y
puts x - y
puts x & y
puts x.include?('se')
puts y.include?('se')
