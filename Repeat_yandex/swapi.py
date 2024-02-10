import requests
from pprint import pprint
'''Получение информации от API сервиса swapy.dev'''
response = requests.get('https://swapi.dev/api/people').json()
all_characters = []
for i in response['results']:
    all_characters.append(i)
pprint(all_characters)
LukePlanet = [character['homeworld'] for character in all_characters
              if character['name'] == 'Luke Skywalker'][0]
planetresponse = requests.get(LukePlanet).json()
diameter = int(planetresponse['diameter'])
print(diameter)
