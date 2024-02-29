#!/bin/bash
# A bash script that takes in a URL and displays all the http methods the server will accept
curl -sI $1 | grep "Allow" | cut -d " " -f 2-
