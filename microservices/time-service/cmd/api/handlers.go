package main

import (
	"fmt"
	"math"
	"net/http"
	"strconv"
	"time"
)

func (app *Config) GetTime(w http.ResponseWriter, r *http.Request) {
	c := time.Now()                                          // current time
	s := time.Date(getStartDate())                           // start time
	result := strconv.FormatFloat(deltaT(c, s), 'g', -1, 64) // result as string

	result += " Days at adesso SE"

	payload := jsonResponse{
		Error: false,
		Data:  fmt.Sprintf("%s", result),
	}
	app.writeJSON(w, http.StatusAccepted, payload)
}

func deltaT(c time.Time, s time.Time) float64 {
	d := c.Sub(s)       // delta time
	r := d.Hours() / 24 // time in days
	return math.Round(r*100) / 100
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
