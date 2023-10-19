package main

import (
	"bytes"
	"encoding/json"
	"errors"
	"io"
	"log"
	"net/http"
)

type jsonResponse struct {
	Error   bool   `json:"error"`
	Message string `json:"message"`
	Data    any    `json:"data,omitempty"`
}

func (app *Config) readJSON(w http.ResponseWriter, r *http.Request, data any) error {
	maxBytes := 1048576

	r.Body = http.MaxBytesReader(w, r.Body, int64(maxBytes))

	dec := json.NewDecoder(r.Body)
	err := dec.Decode(data)
	if err != nil {
		return err
	}

	err = dec.Decode(&struct{}{})
	if err != io.EOF {
		return errors.New("body must have only a single JSON value")
	}

	return nil
}

func (app *Config) writeJSON(w http.ResponseWriter, status int, data any, headers ...http.Header) error {
	out, err := json.Marshal(data)
	if err != nil {
		return err
	}

	if len(headers) > 0 {
		for key, value := range headers[0] {
			w.Header()[key] = value
		}
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	_, err = w.Write(out)
	if err != nil {
		return err
	}

	return err
}

func (app *Config) errorJSON(w http.ResponseWriter, err error, status ...int) error {
	statusCode := http.StatusBadRequest

	if len(status) > 0 {
		statusCode = status[0]
	}

	var payload jsonResponse
	payload.Error = true
	payload.Message = err.Error()

	return app.writeJSON(w, statusCode, payload)
}

func (app *Config) printJSON(f any) {
	jsonData, _ := json.MarshalIndent(f, "", "\t")

	var prettyJSON bytes.Buffer
	error := json.Indent(&prettyJSON, jsonData, "", "\t")
	if error != nil {
		log.Println("JSON parse error: ", error)
		return
	}

	log.Println("JSON:", prettyJSON.String())
}

func (app *Config) fruitsGET(w http.ResponseWriter, f FruitsPayload) {
	pythonAPIURL := "http://fruits-service:90/fruits"

	var response *http.Response
	var err error

	log.Println("\tCase: GET")
	log.Println("\tMethod:", f.Method)
	log.Println("\tData:", f.Path)
	// Make a GET request to retrieve the fruit data
	response, err = http.Get(pythonAPIURL)

	if err != nil {
		app.errorJSON(w, err)
		log.Println("Service not reachable")
		return
	}
	defer response.Body.Close()

	// create a variable we'll read response.Body into
	var jsonFromService jsonResponse

	// decode json from the auth service
	err = json.NewDecoder(response.Body).Decode(&jsonFromService)
	if err != nil {
		app.errorJSON(w, err)
		return
	}

	if jsonFromService.Error {
		app.errorJSON(w, err, http.StatusInternalServerError)
		return
	}

	var payload jsonResponse
	payload.Error = false
	payload.Message = jsonFromService.Message
	payload.Data = jsonFromService.Data

	app.writeJSON(w, http.StatusAccepted, payload)
}

func (app *Config) fruitPOST(w http.ResponseWriter, f FruitsPayload) {
	jsonData, _ := json.MarshalIndent(f.Body, "", "\t")

	pythonAPIURL := "http://fruits-service:90/" + f.Path

	log.Println("\tCase: POST")
	log.Println("\tMethod:", f.Method)
	log.Println("\tPath:", f.Path)
	log.Println("\t\tBody:")
	log.Println("\t\t\tBody:", f.Body.Name)
	log.Println("\t\t\tBody:", f.Body.Color)
	log.Println("\t\t\tBody:", f.Body.Weight)
	// Make a GET request to retrieve the fruit data
	request, err := http.NewRequest("POST", pythonAPIURL, bytes.NewBuffer(jsonData))
	if err != nil {
		app.errorJSON(w, err)
		return
	}

	request.Header.Set("Content-Type", "application/json")

	client := &http.Client{}

	response, err := client.Do(request)
	if err != nil {
		app.errorJSON(w, err)
		return
	}
	defer response.Body.Close()

	// create a variable we'll read response.Body into
	var jsonFromService jsonResponse

	// decode json from the auth service
	err = json.NewDecoder(response.Body).Decode(&jsonFromService)
	if err != nil {
		app.errorJSON(w, err)
		return
	}

	if jsonFromService.Error {
		app.errorJSON(w, err, http.StatusInternalServerError)
		return
	}

	var payload jsonResponse
	payload.Error = false
	payload.Message = jsonFromService.Message
	payload.Data = jsonFromService.Data

	app.writeJSON(w, http.StatusAccepted, payload)
}

func (app *Config) fruitDELETE(w http.ResponseWriter, f FruitsPayload) {
	jsonData, _ := json.MarshalIndent(f.Body, "", "\t")

	pythonAPIURL := "http://fruits-service:90/" + f.Path

	log.Println("\tCase: DELETE")
	log.Println("\tMethod:", f.Method)
	log.Println("\tPath:", f.Path)
	// Make a GET request to retrieve the fruit data
	request, err := http.NewRequest("DELETE", pythonAPIURL, bytes.NewBuffer(jsonData))
	if err != nil {
		app.errorJSON(w, err)
		return
	}

	request.Header.Set("Content-Type", "application/json")

	client := &http.Client{}

	response, err := client.Do(request)
	if err != nil {
		app.errorJSON(w, err)
		return
	}
	defer response.Body.Close()

	// create a variable we'll read response.Body into
	var jsonFromService jsonResponse

	// decode json from the auth service
	err = json.NewDecoder(response.Body).Decode(&jsonFromService)
	if err != nil {
		app.errorJSON(w, err)
		return
	}

	if jsonFromService.Error {
		app.errorJSON(w, err, http.StatusInternalServerError)
		return
	}

	var payload jsonResponse
	payload.Error = false
	payload.Message = jsonFromService.Message
	payload.Data = jsonFromService.Data

	app.writeJSON(w, http.StatusAccepted, payload)
}
