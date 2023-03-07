#!/bin/bash

docker rmi webp-lite

docker build --no-cache -t webp-lite . --platform linux/amd64

docker tag webp-lite pulzo/webp-lite:qa

docker push pulzo/webp-lite:qa

docker rmi pulzo/webp-lite:qa