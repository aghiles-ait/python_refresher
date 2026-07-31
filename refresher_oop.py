from imports import Enemy
from imports.Zombie import Zombie
from imports.Ogre import Ogre

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()
    while e1.get_health_points() > 0 and e2.get_health_points() > 0:
        print('----------')

        e1.special_attack()
        e2.special_attack()

        e2.attack()
        e1.decrease_health_points(e2.get_attack_damage())

        e1.attack()
        e2.decrease_health_points(e1.get_attack_damage())

        print(f'{e1.get_type_of_enemy()}: {e1.get_health_points()} HP left')
        print(f'{e2.get_type_of_enemy()}: {e2.get_health_points()} HP left')
    
    print('----------')
    print('RESULT:')
    if e1.get_health_points() > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    else: 
        print(f'{e2.get_type_of_enemy()} wins!')


if __name__ == "__main__":

    zombie = Zombie(health_points=10, attack_damage=1)
    ogre = Ogre(health_points=20, attack_damage=3)
    
    battle(zombie, ogre)

