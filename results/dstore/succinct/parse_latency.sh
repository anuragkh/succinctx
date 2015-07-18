for i in 0 1 2 3 4; do
    awk "{ if(\$1 == $i) { sum += \$4; count += 1; } } END { print sum/count/1000 }" $1 >> succinct_lat
    awk "BEGIN { min = 10000000000 } { if(\$1 == $i && \$4 < min) { min = \$4 } } END { print min/1000 }" $1 >> succinct_min_lat
    awk "{ if(\$1 == $i && \$4 > max) { max = \$4 } } END { print max/1000 }" $1 >> succinct_max_lat
done

for i in 1 2 3 4 5; do
    echo "Query#$i" >> names_lat
done

paste succinct_lat succinct_min_lat > tmp_lat
paste tmp_lat succinct_max_lat > succinct_final_lat

paste names_lat succinct_final_lat > $2

rm *_lat
