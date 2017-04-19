#!/bin/bash
# NOTE: please let PID to the process you want to monitor
# Usage: ./resource_log.sh <pid>

# clean up previous log

if [ -z "$1" ]
then
echo "No log name extension supplied"
exit
fi

MEM_LOG="memory$1.log"
CPU_LOG="cpu$1.log"

echo "" > ${MEM_LOG}
echo "" > ${CPU_LOG}

while true
do
    date >> ${MEM_LOG}
    free >> ${MEM_LOG}
    uptime >> ${CPU_LOG}
    sleep 1
done
