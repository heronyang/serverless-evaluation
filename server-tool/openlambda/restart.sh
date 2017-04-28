#!/bin/bash

./bin/admin kill -cluster c1
sudo pkill -f ^.*worker-exec.*$
docker unpause $(docker ps -q)
docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
sudo rm -fr ./c1/

./bin/admin new -cluster c1
time sudo ./bin/admin workers -n 1 -cluster c1 -p 80
rm -fr ./c1/registry
cp -rf ./sample-registry ./c1/registry

echo "Sleep just for relaxing"
sleep 20
