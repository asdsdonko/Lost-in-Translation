#!/bin/bash
mkdir -p data/tokenized

for file in data/input_*.txt; do
  base=$(basename $file)
  cat $file | tr ' ' '\n' > data/tokenized/$base
done