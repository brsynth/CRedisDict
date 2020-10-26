#!/bin/bash

for cmd in clean_env build test convert publish
do
  bash ./conda-${cmd}-indocker.sh
done
