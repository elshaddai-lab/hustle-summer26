class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    
    #def attack(self):


if __name__ == "__main__":
    ability_1 = Ability("Super Speed", 50)
    print(ability_1.name)
    print(ability_1.max_damage)
