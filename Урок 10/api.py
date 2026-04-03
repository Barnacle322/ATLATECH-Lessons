import requests

response = requests.get("https://api.github.com/users/Barnacle322")
print(response.status_code)
# 2xx - OK
# 4xx - User Error
# 5xx - Server Error
print(response.json()["name"])
