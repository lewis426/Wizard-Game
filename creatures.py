import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return 'Creature: {0} of level {1} has appeared.'.format(
            self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self, creature):
        print('The wizard {} approaches the {} for battle.'.format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print('The wizard {0} rolls {1} and the {2} rolls {3}.'
              .format(self.name, my_roll, creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard {} casts a ball of fire and burns the {} to ash.'.format(self.name, creature.name))
            print()
            return True
        else:
            print('The wizard {0} is overpowered by the {1}. {0} is defeated!'.format(self.name, creature.name))
            print()
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.breathes_fire = breathes_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breathes_fire else 1
        scale_modifier = self.scaliness / 10
        return base_roll * fire_modifier * scale_modifier
