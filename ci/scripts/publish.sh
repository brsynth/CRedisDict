#!/bin/bash

source .env
source ../extras/.env

anaconda \
    upload \
    --user brsynth \
    --label main \
    ${CONDA_BLD_PATH}/*/${PACKAGE}-*.tar.bz2
