#pip install pyyaml
import json

import yaml
from yaml.loader import SafeLoader

# Open the file and load the file
with open('sample.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)
    print(json.dumps(data,indent=4))