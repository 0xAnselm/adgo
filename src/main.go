package main

import (
	"fmt"
	"math"
	"strconv"
	"time"
)

type myFloat struct {
	f float64
}

func main() {
	daysE := deltaT()
	s := daysE.toString()
	fmt.Println(s, "Days elapsed")
}

func deltaT() myFloat {
	c := time.Now() // current time
	year := 2023
	month := time.August
	day := 1
	hour := 11
	minute := 30
	sec := 0
	nsec := 0
	loc := time.FixedZone("GMT", 0)
	s := time.Date(year, month, day, hour, minute, sec, nsec, loc) // start time

	d := c.Sub(s)       // delta time
	r := d.Hours() / 24 // time in days
	mf := myFloat{math.Floor(r)}
	return mf
}

func (f myFloat) toString() string {
	return strconv.FormatFloat(f.f, 'f', -1, 64)
}
