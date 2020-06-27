# -*- coding: utf-8 -*-

import requests

file = requests.get("http://www.google.com")
print(file.content)
file.close()

