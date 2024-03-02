import urllib.request
import urllib.parse
import sys
"""sens a POST request to the passed url with the email as a parameter"""

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    html = response.read().decode('utf-8')
    print(html)

