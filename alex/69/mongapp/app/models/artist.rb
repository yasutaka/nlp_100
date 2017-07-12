class Artist
  include Mongoid::Document
  store_in collection: "artist"
  field :name, type: String
  field :area, type: String
  #field :id, type: Int 
  #field :id, type: Integer
end
