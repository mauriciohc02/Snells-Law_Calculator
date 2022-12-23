#!/bin/bash

xhost +local:* &>> output.txt &&
docker-compose up &>> output.txt |
docker compose up &>> output.txt &&
docker-compose down &>> output.txt |
docker compose down &>> output.txt &&
xhost -local:* &>> output.txt

rm output.txt
