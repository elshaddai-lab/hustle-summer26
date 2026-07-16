import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def battle(self, opponent):
       my_list = [self.name, opponent.name]
       print(random.choice(my_list))

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.block()
        return total_defense

    def take_damage(self, damage):
        blocked = self.defend()
        damage_taken = max(damage - blocked, 0)
        self.current_health -= damage_taken
        if self.current_health < 0:
            self.current_health = 0
            print(self.current_health)
            return damage_taken

if __name__ == "__main__":
    my_hero = Hero("Spiderman", 150) # 150 is our starting health
    #print(my_hero.name)
    #print(my_hero.current_health)
    #my_opponent = Hero("Captain America", 200)
    #my_hero.battle(my_opponent)
    #my_hero.add_ability(Ability("Web Shooter", 25))
    #my_hero.add_ability(Ability("Spidey Senses", 10))
    #my_hero.attack()
    my_hero.add_armor(Armor("Gloves", 5))
    my_hero.add_armor(Armor("A Really Cool Hat", 10))
    #my_hero.defend()
    my_hero.take_damage(40)
