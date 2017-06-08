print("iii")
var str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

println(str)

var o = str split("[ |,|.]")

var ob = o.toBuffer

var oob = ob.filterNot(e => e=="")
var ooob = oob.map(e => e.length)

//oob.foreach(e => println(e.length))



