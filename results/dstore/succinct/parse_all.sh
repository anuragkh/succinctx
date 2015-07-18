FILES="sr-*"
for f in $FILES
do
    ./parse_latency.sh $f/latency-regex-search $f.bb
done
