from urllib.request import urlopen
import json

url = "link.json"

dataset = urlopen(url)
details = json.loads(dataset.read())



# Sorted dataset based on population

details = sorted(details, key=lambda d: d['population'])
