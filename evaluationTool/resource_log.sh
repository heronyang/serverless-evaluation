#!/bin/bash
# NOTE: please let PID to the process you want to monitor
# Usage: ./resource_log.sh <pid>

# clean up previous log
echo "" > log
echo $1
while true
do
    top -bn1 -p $1  >> log
    sleep 1
done
