#!/usr/bin/python

from datetime import datetime
from elasticsearch import Elasticsearch
import sys, getopt, json

es = Elasticsearch()

def bench_query_latency(queryfile, index, doc_type):
  qout = open('latency_results_regex', 'w')
  with open(queryfile) as ifp:
    qid = 0
    for query in ifp:
      for i in range(0, 10):
        start = datetime.now()
        es.search(index=index, body={"query": {"regexp": { "text" : query}}})
        end = datetime.now()
        diff = end - start
        print "Query %d iteration %d completed; took %d microseconds" % (qid, i, diff.microseconds)
        qout.write("%d\t%d\t%d\n" % (qid, i, diff.microseconds))
      qid += 1
  qout.close()
  print "Finished benchmarking."

def main(argv):
  queryfile = ''
  index = 'test'
  doc_type = 'test'
  try:
    opts, args = getopt.getopt(argv,"hq:i:t:",["qfile=","index=","type="])
  except getopt.GetoptError:
    print 'esperf.py -q <query-file> -i <index> -t <type>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'esperf.py -q <query-file> -i <index> -t <type>'
      sys.exit()
    elif opt in ("-q", "--qfile"):
      queryfile = arg
    elif opt in ("-i", "--index"):
      index = arg
    elif opt in ("-t", "--type"):
      doc_type = arg
  if queryfile == '':
  	print "Error: Must specify query-file!"
  	sys.exit(2)
  bench_query_latency(queryfile, index, doc_type)

if __name__ == "__main__":
   main(sys.argv[1:])
