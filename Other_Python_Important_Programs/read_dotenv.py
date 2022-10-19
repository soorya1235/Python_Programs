import os

from dotenv import load_dotenv,dotenv_values

#This will load the .env files in to enviroment variables
load_dotenv()
print(os.environ['user'])
print(os.environ['password'])

#How to read the value of .evn in to  variables
config = dotenv_values('.env')
print(config)

