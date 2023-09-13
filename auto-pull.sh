#!/bin/bash

cd "${0%/*}"
git pull

cd -
python3 run-tests.sh