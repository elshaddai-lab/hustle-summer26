







import random

from hero import Hero


class Team:
    def __init__(self, name):
        ''' Instance properties:
        name: String -> the team's name
        heros: List -> the Hero objects on the team
        '''
        self.name = name
        self.heroes = [] #start empty; we add heros one at a time

    # --Managing the roster ------------------------
        
    def add_hero(self, hero):
        ''' Add a Hero object to this team. '''
        self.heros.append(hero)

    def remove_hero(self, name):
        ''' Remove a hero from this team by NAME.

        We walk through the list looking for a hero whose name matches. If we find one, we remove it. If no hero with that name is found, we print a friendly note.
        '''

        for hero in self.heroes:
            if hero.name == name:
                self.heros.remove(hero)
                return # done -- leave the method
        print("There is no hero named " + name + " on this team.")

        def view_all_heros(self):
            ''' Print the name of every hero on this team."
            for hero in self.heroes:
                print(hero.name)

        # -- Team statistics ------------------------

        def team_kills(self):
            '''Add up the kills of every hero on the team.'''
            total = 0
            for hero in self.heroes:
                total += hero.kills
                return total

         def team_deaths(self):
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
        living_opponents = [h for h in other_team.heros if h.is_alive()]

        # Keep fighting while BOTH teams still have someone standing.
        while len(living_heros) > 0 and len(living_opponents) > 0:
            # random.choice() picks one random item from a list.
            hero = random.choice(living_heros)
            opponent = random.choice(living_opponents)

            # Two heros duel using the Hero.battle() method we already wrote.
            hero.battle(opponent)

            #After the duel, rebuild the "still alive" lists so dead hers
            # drop out and can't be picked again.
            living_heros = [h for h in self.heros if h.is_alive()]
            living_opponents = [h for h in other_team.heros if h.is_alive()]

    def revive_heros(self, health = 100):
        ''' Bring every hero on the team back to full health.

        Handy for playing another round without rebuilding all the teams.
        '''
        for hero in self.heros:
            hero.current_health = health


# ------------------------------------------------------
# Quick test area (only runs when you do python3 team.py)
# ------------------------------------------------------
if __name__ == "__main__":
    team = Team("X-Men")
    team.add_hero(Hero("Storm"))
    team.add_hero(Hero("Wolverine"))
    team.view_all_heros()        # -> Storm, then Wolverine
    team.remove_hero("Storm")
    team.view_all_heros()        # -> Now, just Wolverine