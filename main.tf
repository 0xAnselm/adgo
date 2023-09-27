terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "go-compiler" {
  name         = "go"
  keep_locally = true
}

resource "docker_container" "go-compiler" {
  image = docker_image.go-compiler.name
  name  = "myGoContainer"
  #   ports {
  #     internal = 80
  #     external = 8000
  #   }
  attach = true
}
