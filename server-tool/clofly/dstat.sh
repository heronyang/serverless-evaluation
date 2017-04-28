#!/bin/bash
if [ -z "$1" ]
then
echo "Please specify the output file"
exit
fi

# run
dstat -T -ta -p -y -m --socket --noheaders --output $1
