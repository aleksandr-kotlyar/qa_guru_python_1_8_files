import os.path

import requests
from requests import Response

r: Response = requests.get('https://selenium.dev/images/selenium_logo_square_green.png')

f = open('selenium.png', 'wb')
f.write(r.content)
f.close()

print(os.path.getsize('selenium.png'))