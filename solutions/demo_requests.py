


import requests
# import json

# response = requests.get('https://cat-fact.herokuapp.com/facts')

# data = response.json()
# for fact in data['all']:
#     print(fact['text'])
#     print()


# headers = {'Accept': 'text/plain'}
# response = requests.get('https://icanhazdadjoke.com/', headers=headers)
# print(response.text)

# headers = {'Accept': 'application/json'}
# response = requests.get('https://icanhazdadjoke.com/', headers=headers)
# data = response.json()
# print(data['joke'])





term = input('what is the term you\'d like to search for? ').lower()
page = 1
while True:
    params = {'page': page, 'term': term}
    headers = {'Accept': 'application/json'}
    response = requests.get('https://icanhazdadjoke.com/search', headers=headers, params=params)
    print(response.url)
    data = response.json()
    for joke in data['results']:
        print(joke['joke'])
    total_pages = data["total_pages"]
    print(f'Page {page}/{total_pages}')
    next_page = input('would you like to see the next page? ').lower().strip()
    if next_page in ['y', 'yes', 'ok', 'sure']:
        page += 1
    else:
        break

