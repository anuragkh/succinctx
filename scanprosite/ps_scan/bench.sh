#!/bin/bash

for qid in `seq -f "%02g" 1 10`; do
  qpath="queries/query$qid"
  for iter in `seq 1 3`; do
    starttime=$(($(date +%s%N)/1000))
    ./scanprosite $qpath
    endtime=$(($(date +%s%N)/1000))
    echo "$iter $(($endtime - $starttime))" >> ${qpath}.benchres
  done
done
