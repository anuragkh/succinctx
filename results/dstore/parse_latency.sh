for i in 0 1 2 3 4; do
    awk "{ if(\$1 == $i) { sum += \$4; count += 1; } } END { print sum/count/1000 }" latency_elasticsearch.txt >> es_lat
    awk "BEGIN { min = 10000000000 } { if(\$1 == $i && \$4 < min) { min = \$4 } } END { print min/1000 }" latency_elasticsearch.txt >> es_min_lat
    awk "{ if(\$1 == $i && \$4 > max) { max = \$4 } } END { print max/1000 }" latency_elasticsearch.txt >> es_max_lat
done

for i in 0 1 2 3 4; do
    awk "{ if(\$1 == $i) { sum += \$4; count += 1; } } END { print sum/count/1000 }" latency_mongo.txt >> mongo_lat
    awk "BEGIN { min = 10000000000 } { if(\$1 == $i && \$4 < min) { min = \$4 } } END { print min/1000 }" latency_mongo.txt >> mongo_min_lat
    awk "{ if(\$1 == $i && \$4 > max) { max = \$4 } } END { print max/1000 }" latency_mongo.txt >> mongo_max_lat
done

for i in 0 1 2 3 4; do
    awk "{ if(\$1 == $i) { sum += \$4; count += 1; } } END { print sum/count/1000 }" latency_succinct.txt >> succinct_lat
    awk "BEGIN { min = 10000000000 } { if(\$1 == $i && \$4 < min) { min = \$4 } } END { print min/1000 }" latency_succinct.txt >> succinct_min_lat
    awk "{ if(\$1 == $i && \$4 > max) { max = \$4 } } END { print max/1000 }" latency_succinct.txt >> succinct_max_lat
done

for i in 1 2 3 4 5; do
    echo "Query#$i" >> names_lat
done

paste es_lat es_min_lat > tmp_lat
paste tmp_lat es_max_lat > es_final_lat

paste mongo_lat mongo_min_lat > tmp_lat
paste tmp_lat mongo_max_lat > mongo_final_lat

paste succinct_lat succinct_min_lat > tmp_lat
paste tmp_lat succinct_max_lat > succinct_final_lat

paste es_final_lat mongo_final_lat > tmp_lat
paste tmp_lat succinct_final_lat > _lat

paste names_lat _lat > latency.txt

rm *_lat
