from pokemon import Pokemon


class WaterTypePokemon(Pokemon):
    def __init__(self, name, attack_value, speed_value, health):
        super().__init__(name, attack_value, speed_value, health)
        self.types = 'Water'

    def attack(self, other_pokemon):
        self.delay_print(f'\n\n{self.name} used Hydro Pump! against {other_pokemon.name}!')
        if other_pokemon.dodged_attack():
            self.delay_print(f'\n{other_pokemon.name} dodged the attack!')
        else:
            other_pokemon.health -= self.attack_value
            self.delay_print(f'\n{other_pokemon.name} lost {self.attack_value} points of HEALTH!')