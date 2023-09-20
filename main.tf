terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "go-compiler" {
  name         = "go:1"
  keep_locally = true
}

resource "docker_container" "go-compiler" {
  image = docker_image.go-compiler.name
  name  = "tutorial"
  #   ports {
  #     internal = 80
  #     external = 8000
  #   }
}
