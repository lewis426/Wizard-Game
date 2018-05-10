import random
import time

from creatures import Creature, Wizard, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('------------------------------')
    print('        WIZARD GAME')
    print('------------------------------')
    print()


def game_loop():
    creatures = \
        [SmallAnimal('Toad', 1),
         SmallAnimal('Bat', 3),
         Creature('Wolf', 12),
         Dragon('Dragon', 50, scaliness=20, breathes_fire=True),
         Wizard('Evil Wizard', 500)]
    settings = ['Misty forest', 'Dark lake', 'Rickety bridge', 'Mysterious cave', 'Derelict shack']
    character_name = input('Please input your name: ')
    character = Wizard(character_name, 75)

    print()
    print('The Wizard {0} starts their journey seeking after the evil wizard. '
          '{0} gets the feeling that evil creatures are close.'.format(character_name))
    print('{} is level {}'.format(character_name, character.level))
    print()

    while creatures:

        active_creature = random.choice(creatures)
        active_setting = random.choice(settings)

        print('{} stumbles upon a {}'.format(character_name, active_setting))
        print()
        print('A level {0} {1} appears from the {2}.'
              .format(active_creature.level, active_creature.name, active_setting))
        print()

        action = input('Would you like to [A]ttack, [R]un, [L]ook around or E[x]it game?: ')
        print()
        if action.lower().strip() == 'a':
            if character.attack(active_creature):
                creatures.remove(active_creature)
                character.level = character.level + (active_creature.level * 0.5)
                print('{} has grown to level {}.'.format(character_name, character.level))
                print('-----------------------')
            else:
                print('{} cowers and flees to rest and recover.'.format(character_name))
                time.sleep(10)
                character.level = character.level + (active_creature.level / 3)
                print('{} returns, having grown to level {} from the mistakes of the previous battle.'
                      .format(character_name, character.level))
                print('-----------------------')
        elif action.lower().strip() == 'r':
            print('The Wizard {} fears their powers are not strong enough to match the {} and flees.'
                  .format(character_name, active_creature.name))
            print('-----------------------')
        elif action.lower().strip() == 'l':
            print('{} takes in the {} and sees foes circling.'.format(character_name, active_setting))
            print('The remaining foes: ')
            for c in creatures:
                print('The {} of level {}.'.format(c.name, c.level))
            print('-----------------------')
        elif action.lower().strip() == 'x':
            print('Okay, leaving the game')
            break
        else:
            print('Please enter a valid command.')

        if not creatures:
            print('{} has been triumphant, all the evil creatures have been banished!'.format(character_name))


if __name__ == '__main__':
    main()
