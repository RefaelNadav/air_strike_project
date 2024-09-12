import requests

url = "http://api.openweathermap.org/geo/1.0/direct?q=teheran&appid=cfea5411793c14999b71203d32b5d922"
# params = {'userId':1}

response = requests.get(url)
print(f"reponse is {response.json()}")


url = "https://google.com"

response = requests.get(url)
print(f"reponse is {response.text}")