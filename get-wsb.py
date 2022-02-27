import requests
from datetime import datetime

current_time = datetime.now()
timestamp = current_time.strftime("%Y-%m-%d-T%H:%M:%S")
fp='./RedditWSB/'

url = "https://reddit.com/r/wallstreetbets/.json"
headers = {'user-agent': 'vscode-restclient'}

response = requests.get(url, headers=headers)

with open(fp + timestamp +'.json', 'w') as file:
    file.write(response.text)