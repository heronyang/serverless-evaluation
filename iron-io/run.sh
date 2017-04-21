#!/bin/bash
sudo docker run -d --rm -it --name functions -v ${PWD}/data:/app/data -v /var/run/docker.sock:/var/run/docker.sock -p 80:8080 iron/functions
sleep 20
