import requests
import re


url = "https://fb.com/"
response = requests.get(url)
text = response.text

links = re.findall('"((http|ftp)s?://.*?)"', text)

for link in links:
    print(link)