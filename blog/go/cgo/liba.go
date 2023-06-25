package main

import (
	"C"
	"fmt"
)

//export Jia
func Jia(x, y C.int) {
	fmt.Printf("Hello: %s\n", "qwe")
}

func main() {
	//
}
