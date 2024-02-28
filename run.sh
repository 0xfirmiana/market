#!/bin/bash

trap terminate SIGINT
terminate(){
#    pkill -SIGINT -P $$
    kill -- -$$
    exit
}

python3 ./backend/market/manage.py runserver & 
cd ./frontend && npm run serve &
wait

