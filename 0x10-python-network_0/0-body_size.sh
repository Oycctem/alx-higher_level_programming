#!/bin/bash
# A bash script that takes in a URL and sends a request then displays the size of the body
curl -s "$1" | wc -c
