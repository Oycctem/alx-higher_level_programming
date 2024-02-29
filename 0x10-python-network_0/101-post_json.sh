#!/bin/bash
# A bash script that sends a JSON POST request to a URL then displays the body response
curl -s -H "Content-Type: application/json" -d "@$2" $1
