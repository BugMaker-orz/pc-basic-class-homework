#!/usr/bin/env bash
n=$(( RANDOM % 5 ))
if [[ $n -eq 42 || $n -eq 0 ]]; then echo "Something went wrong"; >&2 echo "The error was using magic numbers"; exit 1; fi
echo "Everything went according to plan"
