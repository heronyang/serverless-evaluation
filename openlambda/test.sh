#!/bin/bash
CONTROL_DIR=~/open-lambda
for i in {1..50}
do
	echo "Testing $i"
	cd $CONTROL_DIR
	./restart.sh
	cd -
	echo "Sleeping before test $i"
	sleep 10
	timeout 80 sh ./dstat.sh ./dstat-log/log-$i
done
