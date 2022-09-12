from urllib.request import urlopen
import json

url = "https://cdn.jsdelivr.net/gh/apilayer/restcountries@3dc0fb110cd97bce9ddf27b3e8e1f7fbe115dc3c/src/main/resources/countriesV2.json"

dataset = urlopen(url)
details = json.loads(dataset.read())



# Sorted dataset based on population

details = sorted(details, key=lambda d: d['population'])
