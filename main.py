from game import Game


if __name__=="__main__":
    pokemon_list_path = r'pokemon_list.csv'
    pokemone_game = Game(pokemon_list_path)
    pokemone_game.run()
