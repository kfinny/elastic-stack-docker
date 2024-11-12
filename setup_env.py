import random
import string
import re

with open('.env', 'r') as fd:
    data = fd.read()


output = re.sub('changeme', lambda m: ''.join(random.choices(string.ascii_letters + string.digits, k=20)), data)
output = re.sub('(ENCRYPTION_KEY=)(.*)', lambda m: f"{m.group(1)}{''.join(random.choices(string.ascii_lowercase + string.digits, k=64))}", output)

with open('.env', 'w') as fd:
    fd.write(output)
