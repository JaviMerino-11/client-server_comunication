import requests

i = 1

while i < 11:
    url = "https://rickandmortyapi.com/api/character/{}".format(i)
    response = requests.get(url)
    data = response.json()
    nombre = data['name']
    print('El personaje {} se llama: {}'.format(i, nombre))
    i += 1
