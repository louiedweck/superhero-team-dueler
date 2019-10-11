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


if __name__ == "__main__":
        # ability = Ability("Debugging Ability", 20)
        # print(ability.name)
        # print(ability.attack())
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
