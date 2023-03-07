#!/bin/bash

docker rmi apolo

docker build --no-cache -t apolo . --platform linux/amd64

docker tag apolo pulzo/apolo:qa

docker push pulzo/apolo:qa

docker rmi pulzo/apolo:qa