#!/bin/bash
CONTROL_DIR=~/open-lambda
rm -fr dstat-log-1500/*
for ((i=1; i<=100; i+=2));
do
	echo "\n\n======== Testing $i ========"
	cd $CONTROL_DIR
	timeout 10 ./restart.sh
	cd -
	timeout 50 sh ./dstat.sh ./dstat-log-1500/log-$i
done
