import random

game_list = ['Rock', 'Paper', 'Scissors']
computer = c = 0
command = p = 0
print('Score: Computer ' + str(c) + ' Player ' + str(p))

while True:
    computer_choice = random.choice(game_list)
    command = input('Rock, Paper, Scissors or Quit: ')
    if command == computer_choice:
        print('Tie')
        print('Player: ' + command)
        print('Computer: ' + computer_choice)
    elif command == 'Rock':
        if computer_choice == 'Scissors':
            print('Player won!')
            print('Player: ' + command)
            print('Computer: ' + computer_choice)
            p += 1
        else:
            print('Computer won!')
            print('Player: '    + command)
            print('Computer: ' + computer_choice)
            c += 1

    elif command == 'Paper':
        if computer_choice == 'Rock':
            print('Player won!')
            print('Player: ' + command)
            print('Computer: ' + computer_choice)
            p += 1
        else:
            print('Computer won!')
            print('Player: ' + command)
            print('Computer: ' + computer_choice)
            c += 1

    elif command == 'Scissors':
        if computer_choice == 'Paper':
            print('Player won!')
            print('Player: ' + command)
            print('Computer: ' + computer_choice)
            p += 1
        else:
            print('Computer won!')
            print('Player: ' + command)
            print('Computer: ' + computer_choice)
            c += 1

    elif command == 'Quit':
        break

    else:
        print('Wrong command!!! You piece of shit, play the fucking game!!!')


print('Player: ' + command)
print('Computer: ' + computer_choice)
print("")
print('Score: Computer ' + str(c) + '   Player ' + str(p))
print("")
