#!/bin/bash
# A bash script that sends a request to a URL as an arg then displays the status code
curl -so /dev/null -w "%{http_code}" $1
