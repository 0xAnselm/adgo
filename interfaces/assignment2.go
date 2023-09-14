package main

import (
	"io"
	"log"
	"os"
)

func main() {
	fName := os.Args[1]
	file, err := os.Open(fName)
	if err != nil {
		log.Fatal(err)
	}
	io.Copy(os.Stdout, file)
}
