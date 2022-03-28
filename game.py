import sys
import time
from player import Player
from pandas import read_csv
from pokemon import Pokemon
from grass_type_pokemon import GrassTypePokemon
from fire_type_pokemon import FireTypePokemon
from water_type_pokemon import WaterTypePokemon


class Game:
    def __init__(self, pokemon_list_path):
        self._available_pokemon = self._load_pokemon_list(pokemon_list_path)

    def _load_pokemon_list(self, pokemon_list_path):
        pokemon_list = read_csv(pokemon_list_path)
        available_pokemon = []
        for row in pokemon_list.iterrows():
            if row[1]['types'] == 'Fire':
                pokemon = FireTypePokemon(row[1]['names'], row[1]['attack values'], row[1]['speed'], row[1]['health'])
            elif row[1]['types'] == 'Water':
                pokemon = WaterTypePokemon(row[1]['names'], row[1]['attack values'], row[1]['speed'], row[1]['health'])
            elif row[1]['types'] == 'Grass':
                pokemon = GrassTypePokemon(row[1]['names'], row[1]['attack values'], row[1]['speed'], row[1]['health'])
            else:
                pokemon = Pokemon(row[1]['names'], row[1]['attack values'], row[1]['speed'], row[1]['health'])
            available_pokemon.append(pokemon)

        return available_pokemon

    def run(self):
        player_1 = self._create_player('Player 1')
        player_2 = self._create_player('Player 2')

        print('\n\n')
        self._display_pokemon_options()
        pokemon_choice = int(input(self.delay_print(f'\n{player_1.name} choose your pokemon: ')))
        player_1.add_pokemon(self._available_pokemon[pokemon_choice-1])

        print('\n\n')
        self._display_pokemon_options()
        pokemon_choice = int(input(self.delay_print(f'\n{player_2.name} choose your pokemon: ')))
        player_2.add_pokemon(self._available_pokemon[pokemon_choice-1])
        
        print('\n')
        self._battle(player_1, player_2)

    def _create_player(self, player):
        name = input(self.delay_print(f'\n{player} enter your name: '))
        return Player(str(name))

    def _display_pokemon_options(self):
        for i, pokemon in enumerate(self._available_pokemon):
            print(i + 1, pokemon.name, f'[ATK: {pokemon.attack_value}|',
                f'SPEED: {pokemon.speed_value}|', f'HEALTH: {pokemon.health}]', end='\n')

    def delay_print(self, s, t=0.07):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(t)
        return ''

    def _battle(self, player_1, player_2):
        self.delay_print(f'\nOkay we have:\n {player_1.name} with {player_1.pokemon.name} \n\tVS\n '
                    f'{player_2.name} with {player_2.pokemon.name}')   

        while player_1.pokemon.is_alive() and player_2.pokemon.is_alive():
            self._show_round_details(player_1, player_2) 

            print(f"\n************* {player_1.name}s Turn *************")
            player_1.pokemon.attack(player_2.pokemon)
            if not(player_2.pokemon.is_alive()):
                print(f"\n{player_2.pokemon.name} fainted ..")
                break

            print(f"\n\n\n************* {player_2.name}s Turn *************")
            player_2.pokemon.attack(player_1.pokemon)
            if not(player_1.pokemon.is_alive()):
                print(f"\n{player_1.pokemon.name} fainted ..")
                break           

    def _show_round_details(self, player_1, player_2):
        print('\n' + '__'*40)
        h1 = player_1.pokemon.health * u"\u2588" 
        h2 = player_2.pokemon.health * u"\u2588"
        self.delay_print(f'\n{player_1.pokemon.name} \n{player_1.pokemon.health} HEALTH: {h1}\n', 0.01)
        self.delay_print(f'\n{player_2.pokemon.name} \n{player_2.pokemon.health} HEALTH: {h2}', 0.01)
        print('\n' + '__'*40)
        