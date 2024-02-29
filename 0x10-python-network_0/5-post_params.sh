#!/bin/bash
# A bash script that takes in a URL then send a POST request to it
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
