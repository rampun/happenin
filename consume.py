# consuming API in terminal
import requests

response = requests.get('http://127.0.0.1:8000/events')
print(response.json())