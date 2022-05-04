# reddit-data

Data originally collected using Microsoft Flow and IFTTT then transition to python scripts.

Use the following script as a template for `get-`url.py

## get-wsb.py

```py
import requests
from datetime import datetime

# fp is the root filepath
# and intialize timestamp variable
# fp='./RedditExcel/' for /r/Excel posts
fp='./RedditWSB/'
current_time = datetime.now()
timestamp = current_time.strftime("%Y-%m-%d-T%H:%M:%S")

# set up the request and receive the response
# https://reddit.com/r/excel/.json for /r/Excel
url = "https://reddit.com/r/wallstreetbets/.json"
headers = {'user-agent': 'vscode-restclient'}
response = requests.get(url, headers=headers)

# write to file @ ./RedditWSB/{timestamp}.json
with open(fp + timestamp +'.json', 'w') as file:
    file.write(response.text)
```
