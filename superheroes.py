import random


class Ability:

    def __init__(self, name, max_damage):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
        '''
        self.name = name
        self.max_damage = max_damage
        # TODO: Instantiate the variables listed in the docstring with then
       # values passed in

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value.
        return random.randint(0, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
        # TODO: Create instance variables for the values passed in.

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block)


class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
         abilities: List
         armors: List
         name: String
         starting_health: Integer
         current_health: Integer
     '''
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)
        # Add ability object to abilities:List

    def attack(self):
        # TODO: This method should run Ability.attack() on every ability
        # in self.abilities and returns the total as an integer.
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        # TODO: Add armor object that is passed in to `self.armors`
        self.armors.append(armor)

    def defend(self, damage_amt):
        # TODO: This method should run the block method on each armor in self.armors
        total_block = 0
        for armors in self.armors:
            total_block += armors.block()
        return total_block

    def take_damage(self, damage):
        # updating health after an attack
        self.current_health -= damage

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        return self.current_health > 0

    def fight(self, opponent):
        # if neith have abilities:
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
        # elif self has no abilities:
        elif len(self.abilities) == 0:
            # kill self
            self.current_health = 0
            opponent.add_kills(1)
            self.add_deaths(1)
            print(opponent.name + " defeated", self.name + '!')
        # elif other has no abilities:
        elif len(opponent.abilities) == 0:
            # kill other
            opponent.current_health <= 0
            opponent.add_deaths(1)
            self.add_kill(1)
            print(self.name + " defeated", opponent.name + '!')
        # else:
        else:
            # while one hero is still alive:
            while self.is_alive() and opponent.is_alive():
                # self attacks other
                opponent.take_damage(self.attack())
                if not opponent.is_alive():
                    self.add_kill(1)
                    opponent.add_deaths(1)
                    print(self.name + " defeated", opponent.name + '!')
                    return
                # other attacks self
                self.take_damage(opponent.attack())
                print(opponent.name + " defeated", self.name + '!')

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths


class Weapon(Ability):
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)

    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)


class Team(object):
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            return 0
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def attack(self, other_team):
        while self.heroes and other_team.heroes:
            hero_1 = random.choice(self.heroes)
            hero_2 = random.choice(other_team.heroes)
            if hero_1.is_alive() and hero_2.is_alive():
                hero_1.fight(hero_2)

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            if hero.is_alive() == False:
                hero.current_health = hero.starting_health
    ''' Reset all heroes health to starting_health'''

    def stats(self):
        for hero in self.heroes:
            ratio = hero.kills / hero.deaths
            print(hero.name + "'s K/D is " + ratio)
    '''Print team statistics'''


if __name__ == "__main__":

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 80)
    ability2 = Ability("Super Eyes", 20)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
