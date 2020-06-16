#!/bin/bash


python3 ../src/main.py \
  -rp2paths_compounds in/$size/rp2paths_compounds.csv \
  -rp2_pathways in/$size/rp2_pathways.csv \
  -rp2paths_pathways in/$size/rp2paths_pathways.csv \
  -max_subpaths_filter $max_subpaths \
  -output out/${size}_${max_subpaths} \
  -sm db
