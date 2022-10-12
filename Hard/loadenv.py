from dotenv import load_dotenv,dotenv_values
import os

load_dotenv(".env")
print(os.environ)

b = dotenv_values(".env")
print(b)
