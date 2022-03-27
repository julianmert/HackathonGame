import random
import sys
import time

class Pokemon:
    def __init__(self, name, attack_value, speed_value, health):
        self.name = name
        self.attack_value = attack_value
        self.speed_value = speed_value
        self.health = health

    def attack(self, other_pokemon):
        self.delay_print(f'\n\n{self.name} attacked {other_pokemon.name}')
        if other_pokemon.dodged_attack():
            self.delay_print(f'\n{other_pokemon.name} dodged the attack!')
        else:
            other_pokemon.health -= self.attack_value
            self.delay_print(f'\n{other_pokemon.name} lost {self.attack_value} points of HEALTH!')

    def delay_print(self, s, t=0.07):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(t)
        return ''

    def dodged_attack(self):
        if self.speed_value == 'SuperFast':
            value = random.random()
            return value <= 0.7

        if self.speed_value == 'Fast':
            value = random.random()
            return value <= 0.6

        if self.speed_value == 'Medium':
            value = random.random()
            return value <= 0.4

        if self.speed_value == 'Low':
            value = random.random()
            return value <= 0.2

        if self.speed_value == 'SuperLow':
            value = random.random()
            return value <= 0.1
    
    def is_alive(self):
        return self.health > 0 
