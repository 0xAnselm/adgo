package main

import (
	"fmt"
	"strconv"
)

type person struct {
	firstName string
	lastName  string
	contact   contactinfo
}

type contactinfo struct {
	em      eMail
	zipCode int
}

type eMail struct {
	prefix string
	at     string
	suffix string
}

func (p person) toString() string {
	return "Person:\n\t" + p.firstName + " " + p.lastName + "\n\t" + p.contact.toString()
}

func (c contactinfo) toString() string {
	return "Contactinfo:\n\t" + c.em.toString() + "\n\t\tzipCode: " + strconv.Itoa(c.zipCode)
}

func (p person) printPerson() {
	fmt.Println(p.toString())
}

func (e eMail) toString() string {
	return "\teMail: " + e.prefix + e.at + e.suffix
}

func (p *person) updateName(newFirstName string) {
	p.firstName = newFirstName
}

func main() {
	p1 := person{
		firstName: "Alex",
		lastName:  "Alexson",
		contact: contactinfo{
			em: eMail{
				prefix: "a",
				at:     "@",
				suffix: "b",
			},
			zipCode: 1234,
		},
	}
	p1.printPerson()
	fmt.Printf("%+v\n", p1)
	p1.updateName("Torsten")
	p1.printPerson()
}
