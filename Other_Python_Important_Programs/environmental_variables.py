import os

# Get environment variables
USER = os.getenv('API_USER')
onedrive = os.environ['OneDrive']
java = os.environ['JAVA_HOME']

print("The One Drive Path is",onedrive)
print("The Java Path is",java)

#Set Environment Variables

os.environ['A1'] = "ABC"
os.environ['B1'] = "CCC"


# Set environment variables
os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')

print(USER)
print(PASSWORD)

import os

# Iterate loop to read and print all environment variables
print("The keys and values of all environment variables:")
for key in os.environ:
    print(key, '=>', os.environ[key])
