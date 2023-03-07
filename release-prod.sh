#!/bin/bash

docker rmi apolo

docker build --no-cache -t apolo . --platform linux/amd64

docker tag apolo pulzo/apolo:latest

docker push pulzo/apolo:latest 

docker rmi pulzo/apolo:latest