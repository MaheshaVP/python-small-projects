#Import and connect to the api

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokeman_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed to retrive data {response.status_code}")

pokeman_name = "Typhlosion"
pokemon_info = get_pokeman_info(pokeman_name)

if pokemon_info:
    print(f"Name   : {pokemon_info["name"].capitalize()}")
    print(f"id     : {pokemon_info["id"]}")
    print(f"height : {pokemon_info["height"]}")
    print(f"weight : {pokemon_info["weight"]}")
