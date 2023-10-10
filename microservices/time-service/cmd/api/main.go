package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

const webPort = "80"

type Config struct {
}

func handler(w http.ResponseWriter, r *http.Request) {
	c := time.Now()                // current time
	s := time.Date(getStartDate()) // start time
	daysE := deltaT(c, s)
	result := daysE.toString() // result

	result += " Days elapsed"

	fmt.Fprint(w, result)
}

func main() {
	http.HandleFunc("/time", handler)
	log.Fatal(http.ListenAndServe(":80", nil))
}
