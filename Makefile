.PHONY: up down build

up:
docker-compose up -d --build

down:
docker-compose down

build:
docker-compose build
