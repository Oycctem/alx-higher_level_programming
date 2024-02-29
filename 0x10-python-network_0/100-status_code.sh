#!/bin/bash
# A bash script that sends a request to a URL as an arg then displays the status code
curl -s -o /dev/null -w "%{http_code}" $1
