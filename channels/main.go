package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
	"time"
)

func main() {
	// fName := "links.txt"
	links := []string{
		"http://google.com",
		"http://facebook.com",
		"http://stackoverflow.com",
		"http://golang.org",
		"http://amazon.com",
	}
	c := make(chan string)

	for _, link := range links {
		go checkLink(link, c)
	}

	for l := range c {
		go func(link string) {
			time.Sleep(3 * time.Second)
			checkLink(link, c)
		}(l)
	}
}

func checkLink(l string, c chan string) {
	resp, err := http.Get(l)
	if err != nil {
		log.Fatal(err)
		c <- l
		os.Exit(1)
		return
	}
	fmt.Println("Link:", resp.Status, l)
	c <- l
}

func getLinks(fName string) []string {
	file, err := os.Open(fName)
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}

	fc := make([]byte, 32*1024)
	file.Read(fc)
	fcs := strings.Split(string(fc), "\n")
	return fcs
}
