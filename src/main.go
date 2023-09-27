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
	c := time.Now()                // current time
	s := time.Date(getStartDate()) // start time
	daysE := deltaT(c, s)
	r := daysE.toString() // result
	fmt.Println(r, "Days elapsed")
}

func deltaT(c time.Time, s time.Time) myFloat {
	d := c.Sub(s)       // delta time
	r := d.Hours() / 24 // time in days
	mf := myFloat{math.Floor(r)}
	return mf
}

func (f myFloat) toString() string {
	return strconv.FormatFloat(f.f, 'f', -1, 64)
}

func getStartDate() (int, time.Month, int, int, int, int, int, *time.Location) {
	year := 2023
	month := time.August
	day := 1
	hour := 11
	minute := 30
	sec := 0
	nsec := 0
	loc := time.FixedZone("GMT", 0)
	return year, month, day, hour, minute, sec, nsec, loc
}
