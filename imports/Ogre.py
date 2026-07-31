from imports.Enemy import Enemy
import random

class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Ogre',health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("Ogre is slamming hands all around")

    def spread_disease(self):
        print("I am spreading infection")

    def special_attack(self):
        if random.random() < 0.2:
            self._attack_damage += 4
            print("Ogre gets angry and increases attack by 4!")
