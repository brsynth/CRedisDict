#!/bin/bash


cd ../docker
docker-compose up -d db
docker-compose run --rm -v $PWD/../test:/home/test -w /home/test --entrypoint="" module \
  sh -c "./run.sh"
cd -
