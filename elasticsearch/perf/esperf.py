#!/usr/bin/python

from datetime import datetime
from elasticsearch import Elasticsearch
import sys, getopt, json

es = Elasticsearch()

def us(td):
  return (td.days * 24 * 60 * 60 + td.seconds) * 1000 * 1000 + td.microseconds

def bench_query_latency(queryfile, index, doc_type, repeat):
  qout = open('latency_results_regex', 'w')
  with open(queryfile) as ifp:
    qid = 0
    for line in ifp:
      query = line.strip()
      print "Query: (%s)" % query
      for i in range(0, repeat):
        count = 0
        start = datetime.now()
        res = es.search(index=index, body={"query": {"regexp": { "text" : query}}}, fields = [], size=4807388, query_cache=False)
        for hit in res['hits']['hits']:
	  count += 1
        end = datetime.now()
        diff = end - start
        print "Query %d iteration %d completed; took %d microseconds for %d documents." % (qid, i, us(diff), count)
        qout.write("%d\t%d\t%d\t%d\n" % (qid, i, count, us(diff)))
      qid += 1
  qout.close()
  print "Finished benchmarking."

def main(argv):
  queryfile = ''
  index = 'test'
  doc_type = 'test'
  repeat = 10
  try:
    opts, args = getopt.getopt(argv,"hq:i:t:r:",["qfile=","index=","type=","repeat="])
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
    elif opt in ("-r", "--repeat"):
      repeat = int(arg)
  if queryfile == '':
  	print "Error: Must specify query-file!"
  	sys.exit(2)
  bench_query_latency(queryfile, index, doc_type, repeat)

if __name__ == "__main__":
   main(sys.argv[1:])
