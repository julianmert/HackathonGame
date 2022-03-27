from game import Game


if __name__=="__main__":
    pokemon_list_path = r'pokemon_list.csv'
    game = Game(pokemon_list_path)
    game.run()
