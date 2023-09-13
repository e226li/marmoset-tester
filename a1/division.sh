#!/bin/bash
<cases xargs -l bash -c 'echo -n "($0, $1) $2 " && echo -e "\e[$((31 + ($(echo $0 $1 | ~/a.out) == $2)))m$(echo $0 $1 | ~/a.out)\e[0m"'
