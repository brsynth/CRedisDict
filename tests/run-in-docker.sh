#!/bin/bash


cd docker
docker-compose run --rm -v $PWD/../src:/home/test -w /home/test --entrypoint="" tool \
  sh -c "python3 main.py"
docker-compose down -v
cd -
