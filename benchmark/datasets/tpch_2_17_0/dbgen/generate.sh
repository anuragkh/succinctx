#!/bin/bash

sf=$1
if [ "$sf" == "" ]; then
  sf="1"
fi

echo "Generating data with sf=$sf"

./dbgen -T O -s $sf
./dbgen -T P -s $sf
./dbgen -T s -s $sf

mkdir -p data
mv *.tbl data/
