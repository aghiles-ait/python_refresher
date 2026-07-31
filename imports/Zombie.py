from imports.Enemy import Enemy
import random

class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Zombie',health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("*Grumbling...")

    def spread_disease(self):
        print("I am spreading infection")

    def special_attack(self):
        if random.random() < 0.5:
            self._health_points += 2
            print("Zombie regenrated 2 HP!")
