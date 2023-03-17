import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ['API_KEY']

def getPlanet(planet):
    """Return given planet information"""
    planet = planet.capitalize()
    url = 'https://api.api-ninjas.com/v1/planets?name={}'.format(planet)
    response = requests.get(url, headers={'X-Api-Key': API_KEY})
    return response.text

# print(getPlanet('Earth'))                                