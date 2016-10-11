import urllib.request
import json
response = urllib.request.urlopen('http://www.reddit.com/r/all/top/.json').read()
jsonResponse = json.loads(response.decode('utf-8'))
print (jsonResponse)
json_data = json.loads(jsonResponse.text)