import json

import requests

url = "https://api.github.com/user"
headers = {}
token="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"
headers['Authorization'] = "Bearer {}".format(token)
response = requests.get(url,headers=headers)
print(response.status_code)
print(response.json())
print(json.dumps(response.json(),indent=6))