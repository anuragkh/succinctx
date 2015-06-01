#!/usr/bin/python

from datetime import datetime
from pymongo import MongoClient
import sys, getopt, json

client = MongoClient()

def bench_query_latency(queryfile, db_name, collection_name):
  db = client[db_name]
  collection = db[collection_name]

  qout = open('latency_results_regex', 'w')
  with open(queryfile) as ifp:
    qid = 0
    for query in ifp:
      for i in range(0, 10):
        start = datetime.now()
        # query goes here
        # collection.find({'text': { '$regex' : query }})
        end = datetime.now()
        diff = end - start
        print "Query %d iteration %d completed; took %d microseconds" % (qid, i, diff.microseconds)
        qout.write("%d\t%d\t%d\n" % (qid, i, diff.microseconds))
      qid += 1
  qout.close()
  print "Finished benchmarking."

def main(argv):
  queryfile = ''
  db = 'test'
  collection = 'test'
  try:
    opts, args = getopt.getopt(argv,"hq:d:c:",["qfile=","db=","collection="])
  except getopt.GetoptError:
    print 'mongoperf.py -q <query-file> -d <database> -c <collection>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'mongoperf.py -q <query-file> -d <database> -c <collection>'
      sys.exit()
    elif opt in ("-q", "--qfile"):
      queryfile = arg
    elif opt in ("-d", "--db"):
      index = arg
    elif opt in ("-c", "--collection"):
      doc_type = arg
  if queryfile == '':
  	print "Error: Must specify query-file!"
  	sys.exit(2)
  bench_query_latency(queryfile, db, collection)

if __name__ == "__main__":
   main(sys.argv[1:])
