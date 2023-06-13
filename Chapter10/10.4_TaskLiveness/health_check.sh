#!/bin/bash

# Liveness probe for batch process
# The process writes a logfile every time it runs with the current Unix
# timestamp.

# Usage: process_liveness.sh <path_to_file>
# The file must contain only the latest date as a Unix timestamp and no
# newlines

if ! rundate=$(<$1); then
  echo >&2 failed
  echo "no logfile"
  exit 1
fi

curdate=$(date +'%s')

diff=$((curdate-rundate))

if [ $diff -gt 300 ]
then
  echo "too old"
  exit 100
fi

exit 0
