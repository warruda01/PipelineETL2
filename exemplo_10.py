
#Outro exemplo:

import requests
url2 = "https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0"
response2 = requests.get(url2)
print(response2.json())