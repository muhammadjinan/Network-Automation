import requests
import json
response = requests.get('https://jsonplaceholder.typicode.com/users')
todos = json.loads(response.text)
# print(todos)
with open('firstJSON.json', 'w')as F:
    json.dump(todos, F, indent=1)
    # for item in todos:
    #     print(item)
    for item in todos:
        if item['username'] == 'Delphine':
            print(item)
            print(f'Phone number of \'{item['username']}\' is: \'{item['phone']}\'')
