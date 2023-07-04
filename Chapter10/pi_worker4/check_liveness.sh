#!/bin/bash

# Liveness probe for batch process
# The process writes a logfile every time it runs with the current Unix
# timestamp.

# Usage: process_liveness.sh <path_to_file> <freshness_seconds>
# The file must contain only the latest date as a Unix timestamp and no
# newlines

if [ -z "$1" ] || [ -z "$2" ]; then
  echo >&2 'Missing parameters'
  echo >&2 'Usage: process_liveness.sh <path_to_file> <freshness_seconds>'
  echo >&2 '  e.g: process_liveness.sh lastrun.date 300'
  exit 1
fi

if ! rundate=$(<$1); then
  echo >&2 "Failed: unable to read logfile"
  exit 2
fi

curdate=$(date +'%s')

time_difference=$((curdate-rundate))

if [ $time_difference -gt $2 ]
then
  echo >&2 "Liveness failing, timestamp too old."
  exit 1
fi

exit 0
