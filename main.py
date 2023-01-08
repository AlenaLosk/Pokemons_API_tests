import requests
import json

token = '2a6a79730d7817f07c35090ca4548164'
# получили коллекцию покемонов у тренера 1652 и запоминаем id наиболее позднесозданного
response_get_all_pokemons = requests.get('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token},
                                         params={'trainer_id': 1652, 'status': 1})
response_json = json.dumps(response_get_all_pokemons.json(), indent=4, ensure_ascii=False)
print(response_json)
id_for_kill = response_get_all_pokemons.json()[4]['id']

# наиболее позднесозданного покемона у тренера 1652 уничтожает
response_kill_pokemon = requests.post('https://pokemonbattle.me:5000/pokemons/kill', headers={'trainer_token': token},
                                      json={"pokemon_id": id_for_kill})
response_json = json.dumps(response_kill_pokemon.json(), indent=4, ensure_ascii=False)
print(response_json)

# создаем нового покемона
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    'name': 'РусланТест', 'photo': 'https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png'})
response_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
print(response_json)
id_for_add_pokeball = response.json()['id']

# редактируем нового покемона
response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    'pokemon_id': id_for_add_pokeball,
    'name': 'РусланТест2',
    'photo': ''
})
response_json = json.dumps(response_put.json(), indent=4, ensure_ascii=False)
print(response_json)

# добавляем нового покемона в покетбол
response_pokeball = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball',
                                  headers={'trainer_token': token}, json={'pokemon_id': id_for_add_pokeball})

response_json3 = json.dumps(response_pokeball.json(), indent=4, ensure_ascii=False)
print(response_json3)
