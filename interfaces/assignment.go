package main

import "fmt"

type triangle struct {
	height float64
	base   float64
}

type square struct {
	sideLength float64
}

type body interface {
	getArea() float64
}

func printArea(b body) {
	fmt.Println(b.getArea())
}

func (t triangle) getArea() float64 {
	return 0.5 * t.base * t.height
}

func (s square) getArea() float64 {
	return s.sideLength * s.sideLength
}

func main() {
	t := triangle{5.3, 4.2}
	s := square{4}

	printArea(t)
	printArea(s)
}
