import requests

while 1 > 0:
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        user = response.json()['results'][0]
        age = int(user['dob']['date'][:4])
        if age in (1990, 1991, 1999, 1997, 2007):
            name = user['name']['first']
            print(name, age)