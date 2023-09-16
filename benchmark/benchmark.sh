#!/bin/bash
set -e

mkdir temp
cd temp

for i in {1..1000}
do
    cp "../benchmark-program-1.c" "benchmark-program-1-${i}.c"
done

for i in {1..1000}
do
    for _ in {1..1000}
    do
        int_get=$RANDOM
        echo "${int_get}\n$(int_get + 123)\n" >> "benchmark-program-1-${i}.cases"
    done
done

TIMEFORMAT=%0R time $2 > /dev/null

cd ../ && rm -rf temp/
