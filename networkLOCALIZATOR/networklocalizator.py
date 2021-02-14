import json
from urllib.request import urlopen
from tabulate import tabulate

url = "http://ipinfo.io/json"
response = urlopen(url)
data = json.load(response)

table = [["Dirección IP:", data["ip"]],
		 ["Servidor:", data["org"]],
		 ["Ciudad:", data["city"]],
		 ["Pais:", data["country"]],
		 ["Región:", data["region"]]]

print(tabulate(table))