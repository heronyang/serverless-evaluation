#!/bin/bash
CONTROL_DIR=~/
rm -fr dstat-log-1500/*
for ((i=1; i<=150; i+=2));
do
	printf "\n======== Testing $i ========\n"
	# run
	cd $CONTROL_DIR
	timeout 15 ./run.sh
	cd -
	# measure
	timeout 60 sh ./dstat.sh ./dstat-log-1500/log-$i
done
