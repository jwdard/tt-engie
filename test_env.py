# Test environment
import requests
test = ["A", "h", "H", "x"]

r = requests.post("http://localhost:5000/convert", json=test, verify=False)
print(r.json())