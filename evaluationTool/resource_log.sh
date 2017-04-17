#!/bin/bash
# NOTE: please let PID to the process you want to monitor
# Usage: ./resource_log.sh <pid>

# clean up previous log
echo "" > log
while true
do
    htop -p $1 -bn1 >> log
done
