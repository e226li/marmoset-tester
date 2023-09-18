#!/bin/bash
set -e

mkdir temp
cd temp

cp "../benchmark-program-2.c" "benchmark-program-2.c"

for _ in {1..100000}
do
    int_get=$RANDOM
    echo -e "${int_get}\n$((int_get))\n" >> "benchmark-program-2.cases"
done

export DEBIAN_FRONTEND=noninteractive
echo "$(($(stat -c '%s' benchmark-program-2.cases) / $(/usr/bin/time -f '%e' ${@:1} > /dev/null)"

cd ../ && rm -rf temp/