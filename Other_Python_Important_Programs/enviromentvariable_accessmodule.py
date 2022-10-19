from decouple import config

API_USERNAME = config("username")
API_PASSWORD = config("password")

print("API Username is",API_USERNAME)
print("API Password is",API_PASSWORD)
