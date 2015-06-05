for i in $(seq -f "%02g" 1 10); do
    awk '{ sum += $2 } END { print sum/NR/1000 }' scanprosite/query$i.benchres >> sp_lat
    awk 'BEGIN { min = 10000000000 } { if($2 < min) { min = $2 } } END { print min/1000 }' scanprosite/query$i.benchres >> sp_min_lat
    awk '{ if($2 > max) { max = $2 } } END { print max/1000 }' scanprosite/query$i.benchres >> sp_max_lat
done

for i in `seq 0 9`; do
    awk "{ if(\$1 == $i) { sum += \$4; count += 1; } } END { print sum/count/1000 }" succinctx/latency_succinct.txt >> succinct_lat
    awk "BEGIN { min = 10000000000 } { if(\$1 == $i && \$4 < min) { min = \$4 } } END { print min/1000 }" succinctx/latency_succinct.txt >> succinct_min_lat
    awk "{ if(\$1 == $i && \$4 > max) { max = \$4 } } END { print max/1000 }" succinctx/latency_succinct.txt >> succinct_max_lat
done

for i in `seq 1 10`; do
    echo "Query#$i" >> names_lat
done

paste sp_lat sp_min_lat > tmp_lat
paste tmp_lat sp_max_lat > sp_final_lat

paste succinct_lat succinct_min_lat > tmp_lat
paste tmp_lat succinct_max_lat > succinct_final_lat

paste sp_final_lat succinct_final_lat > _lat

paste names_lat _lat > latency.txt

rm *_lat

