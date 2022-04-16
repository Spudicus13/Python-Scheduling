import requests 
import json
import csv
import nicehash
import os



env_var = 'nicehash_API_KEY'
 
env_var_value = 'f788b8c9-9717-4e29-bb94-6e785379cac5dca3a020-ae0d-4474-9ce7-b1d0eb954c1f'

os.environ[env_var] = env_var_value
 
print(f'{env_var}={os.environ[env_var]} environment variable has been set.')
