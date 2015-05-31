#!/bin/bash

query=$1

if [ "$query" == "" ]; then
  query="all"
fi

if [ "$query" == "all" ]; then
  queries=../../benchmark/queries/dbase/tpch-sql/*
  for query in $queries
  do
    java -cp perf.jar:/opt/vertica/java/lib/vertica-jdbc.jar perf.Performance tpch $query
    mv latency_results_regex ${query}.result
  done
else
  java -cp perf.jar:/opt/vertica/java/lib/vertica-jdbc.jar perf.Performance tpch ../../benchmark/queries/dbase/tpch-sql/$query
  mv latency_results_regex ${query}.result
fi
