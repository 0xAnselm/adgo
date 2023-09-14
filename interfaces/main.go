package main

import "fmt"

type englishBot struct{}
type spanishBot struct{}

type bot interface {
	getGreeting() string
}

func main() {
	var eb englishBot
	var sb spanishBot

	printGreeting(eb)
	printGreeting(sb)
}

func printGreeting(b bot) {
	fmt.Println(b.getGreeting())
}
func (englishBot) getGreeting() string {
	return "Hello mate, how are you?"
}

func (spanishBot) getGreeting() string {
	return "Hola, ¿Que Tal?"
}
