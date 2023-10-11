package main

import (
	"fmt"
	"math"
	"net/http"
	"strconv"
	"time"
)

type myFloat struct {
	f float64
}

func (app *Config) GetTime(w http.ResponseWriter, r *http.Request) {
	c := time.Now()                // current time
	s := time.Date(getStartDate()) // start time
	daysE := deltaT(c, s)
	result := daysE.toString() // result

	result += " Days at adesso SE"

	payload := jsonResponse{
		Error: false,
		Data:  fmt.Sprintf("%s", result),
	}
	app.writeJSON(w, http.StatusAccepted, payload)
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
