package main

import (
	"io"
	"log"
	"os"
)

func main() {
	fName := "links.txt"
	links := getLinks(fName)
}

func getLinks() []string {
	file, err := io.Open(fName)
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}
	links := make(links []string, 32*1024)
	io.Copy(links, file)
	return links
}