module NLPCommon
  class MecabNode
    def initialize(str=nil)
      parse(str) unless str.nil?
    end
    def parse(str)
      str.gsub!(/\s/, ',')
      tmp = str.split(',')

      @surface = tmp[0]
      @pos = tmp[1]
      @pos1 = tmp[2]
      @base = tmp[7]
    end

    def to_hash
      {surface: @surface, pos: @pos, pos1: @pos1, base: @base}
    end
  end
end
