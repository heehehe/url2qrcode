#!/usr/bin/env bash

port=$1
if [ -z $port ]; then
    port=8001
fi

python app.py --port $port
