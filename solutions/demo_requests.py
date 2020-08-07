


import requests
import json

response = requests.get('https://cat-fact.herokuapp.com/facts')

data = json.loads(response.text)
# print(data['all'][0]['text'])


for row in data['all']:
    print(row['text'])
    print()



