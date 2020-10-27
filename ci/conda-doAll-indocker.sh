#!/bin/bash

#set -e

bash ./docker/scripts/conda-clean_env-indocker.sh

for cmd in clean_env build test convert publish
do
  bash ./docker/scripts/conda-${cmd}-indocker.sh
done
