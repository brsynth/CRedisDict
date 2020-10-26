#!/bin/bash

source ../extras/.env

for cmd in $@
do
  PACKAGE=$PACKAGE \
  HOMEDIR=$HOMEDIR \
  docker-compose \
      -f conda/docker/docker-compose.yml \
      --env-file conda/docker/.env \
      build $cmd

  PACKAGE=$PACKAGE \
  HOMEDIR=$HOMEDIR \
  docker-compose \
      -f conda/docker/docker-compose.yml \
      --env-file conda/docker/.env \
    run --rm \
    $cmd
done


# PACKAGE=$PACKAGE \
# HOMEDIR=$HOMEDIR \
# docker-compose \
#     -f conda/docker/docker-compose.yml \
#     --env-file conda/docker/.env \
#   run --rm \
#   test
