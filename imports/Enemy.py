class Enemy:

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self._type_of_enemy = type_of_enemy # private attribute
        self._health_points = health_points
        self._attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self._type_of_enemy

    def get_health_points(self):
        return self._health_points

    def get_attack_damage(self):
        return self._attack_damage

    def decrease_health_points(self, damage):
        self._health_points -= damage

    def talk(self):
        print(f"I am a {self._type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self._type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self._type_of_enemy} attacks for {self._attack_damage} damage.")

    def special_attack(self):
        print(f"{self._type_of_enemy} has no special attack")
