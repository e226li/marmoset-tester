#!/bin/bash
set -e

mkdir temp
cd temp

for i in {1..10}
do
    cp "../benchmark-program-1.c" "benchmark-program-1-${i}.c"
done

for i in {1..10}
do
    for _ in {1..10000}
    do
        int_get=$RANDOM
        echo -e "${int_get}\n$((int_get + 123))\n" >> "benchmark-program-1-${i}.cases"
    done
done

export DEBIAN_FRONTEND=noninteractive
TIMEFORMAT=%0R /usr/bin/time ${@:1} > /dev/null

cd ../ && rm -rf temp/
