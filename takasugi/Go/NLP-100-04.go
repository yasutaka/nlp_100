package main

import "fmt"
import "strings"
func main(){
	str := "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
	fmt.Println(str)
	o := strings.Split(str, " ")
	fmt.Println(o)
	fmt.Println(len(o))
	ary := []int{}
	for i := 0; i < len(o); i++ {
		last_char := o[i][len(o[i]) - 1]
		fmt.Println(last_char)
		if last_char == ',' {
			fmt.Println(o[i])
			o[i] = strings.Replace(o[i], ",", "", 1)
			fmt.Println(o[i])
		}
		if last_char == '.' {
			fmt.Println(o[i])
			o[i] = strings.Replace(o[i], ".", "", 1)
			fmt.Println(o[i])
		}
		ary = append(ary, len(o[i]))
	}

	fmt.Println(o)
	fmt.Println(ary)
}
