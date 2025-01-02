import requests
import json
import sys
import os

# Define the proxy
proxies = {
    "http": "http://103.191.196.76:8080",
    "https": "http://103.191.196.76:8080",
}

url = "https://www.google.com"
response = requests.get(url, proxies=proxies)
print(response.status_code)

response = requests.get('https://httpbin.org/ip', proxies=proxies)
ip_address = response.json()['origin']

print(f"Your IP Address: {ip_address}")