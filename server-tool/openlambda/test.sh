#!/bin/bash
CONTROL_DIR=~/open-lambda
rm -fr dstat-log-1500/*
for ((i=1; i<=150; i+=2));
do
	printf "\n======== Testing $i ========\n"
	cd $CONTROL_DIR
	timeout 15 ./restart.sh
	cd -
	timeout 60 sh ./dstat.sh ./dstat-log-1500/log-$i
done
