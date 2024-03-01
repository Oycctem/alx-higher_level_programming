#!/bin/bash
# A bash script that makes a rquest to 0.0.0.0:5000/catch_me that make the server respond with "You got me"
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
