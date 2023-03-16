# Starting point
import random

name = input('What is your name?')
print(f'Welcome to the dungeon, {name}!')

print('You find yourself at the entrance of a dark dungeon.')

# Loop until player reaches the end or loses
while True:
    # Ask for direction
    direction = input('Which way do you want to go? (left/right/up/down) ')

    # Player goes left
    if direction == 'left':
        print('You turn left and walk down a long, winding corridor.')

        # Random chance of encounter
        if random.random() < 0.5:
            print('You come across a fierce dragon!')
            action = input('Do you want to fight or run? ')

            if action == 'fight':
                print('You valiantly fight the dragon with all your might...')
                if random.random() < 0.35:
                    print('...and emerge victorious!')
                else:
                    print('...but the dragon is too strong, and you are defeated.')
                    print('Game over!')
                    break  # End game
            elif action == 'run':
                print('You run as fast as you can back the way you came.')
                print('The dragon roars in frustration as you escape.')
            else:
                print('Invalid action, try again.')

        else:
            print('You continue walking, but nothing of interest happens.')

    # Player goes right
    elif direction == 'right':
        print('You turn right and walk down a dark, narrow tunnel.')

        # Random chance of encounter
        if random.random() < 0.3:
            print('You come across a hidden treasure chest!')
            action = input('Do you want to open it? ')

            if action == 'yes':
                print('You open the chest and find a magic sword inside!')
            elif action == 'no':
                print('You decide to leave the chest alone.')
            else:
                print('Invalid action, try again.')
        else:
            print('You continue walking, but nothing of interest happens.')

    # Player goes up
    elif direction == 'up':
        print('You climb up a steep staircase.')

        # Puzzle
        if random.random() < 0.45:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            answer = num1 + num2
            print(f"You see a sign that reads '{num1} + {num2} = ?'")
            guess = int(input('What is your answer? '))

            if guess == answer:
                print('You solved the puzzle and continue on your way.')
            else:
                print('Incorrect answer! A trapdoor opens beneath you and you fall into a pit.')
                print('Game over!')
                break  # End game
        else:
            print('You continue climbing, but nothing of interest happens.')

    # Player goes down
    elif direction == 'down':
        print('You descend a spiral staircase.')

        # Random chance of encounter
        if random.random() < 0.6:
            print('You hear a growling noise and see a pack of wolves ahead.')
            action = input('Do you want to fight or run? ')

            if action == 'fight':
                print('You battle the wolves with your bare hands...')
                if random.random() < 0.5:
                    print('...and emerge victorious!')
                else:
                    print('...but the wolves are too many, and you are overpowered.')
                    print('Game over!')
                    break  # End game
            
