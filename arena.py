from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''Instantiate properties
        team_one: None
        team_two: None
        '''
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("What is the ability name? ")
        max_damage = input("What is the max damage of the ability? ")

        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt for Weapon information.
        return Weapon with values from user Input
        '''
        name = input("What is the weapon name? ")
        max_damage = input("What is the max damage of the weapon? ")

        return Weapon(name, max_damage)
        pass
    
    def create_armor(self):
        '''Prompt for Armor information.
        return Armor with values from user Input
        '''
        name = input("What is the armor name? ")
        max_damage = input("What is the max damage of the armor? ")

        return Armor(name, max_damage)
        pass

    def create_hero(self):
        '''Prompt for Hero information.
        return Hero with values from user Input
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1]dd ability, [2]add weapon, [3]add armor, or [4]one: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())

        return hero
        
    def build_team_one(self):
        '''Prompt the user to build team one'''
        num_heroes = int(input("How many heroes do you want on team one? "))
        for _ in range(num_heroes):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team two'''
        num_heroes = int(input("How many heroes do you want on team two? "))
        for _ in range(num_heroes):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
        pass

    def team_battle(self):
        '''Battle team_one and team_two together'''
        self.team_one.attack(self.team_two)
        pass

    def show_stats(self):
        '''Print team statistics to terminal'''
        print("\nTeam One:")
        self.team_one.stats()
        print("\nTeam Two:")
        self.team_two.stats()
        
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths == 1:
        print(self.team_one.name + " average K/D was: " + str(team_kills / team_deaths))

        for hero in self.team_one.heroes:
            print("survived from " + self.team_one.name + "; " + hero.name)

        for hero in self.team_two.heroes:
            print("survived from " + self.team_two.name + "; " + hero.name)

        game_is_running = True

        arena = Arena()
        arena.build_team_one()
        arena.build_team_two()
       
       while game_is_running:
            arena.team_battle()
            arena.show_stats()
            play_again = input("Play again? (y/n): ")
            if play_again != "y":
                game_is_running = False
            else:
                game_is_running = True
