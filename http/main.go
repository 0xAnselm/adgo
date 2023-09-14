package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

type logWriter struct{}

func (logWriter) Write(bs []byte) (int, error) {
	fmt.Println(string(bs))
	fmt.Println("Wrote", len(bs), "B")
	return len(bs), nil
}

func main() {
	resp, err := http.Get("http://google.com")
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}
	lw := logWriter{}
	fmt.Println("Pagesize:", os.Getpagesize(), "B = ", os.Getpagesize()/1024, "MB")
	io.Copy(lw, resp.Body)
	fmt.Println(lw)
}
