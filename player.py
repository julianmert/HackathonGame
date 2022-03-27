class Player:
    def __init__(self, name):
        self.name = name
        self.pokemon = None

    def add_pokemon(self, pokemon):
        self.pokemon = pokemon
        