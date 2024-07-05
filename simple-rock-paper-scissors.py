import random

def game():
    choices_list = ['Rock', 'Paper', 'Scissors']
    count_user, count_computer = 0, 0

    while count_user < 3 and count_computer < 3:
        user_input = input('What do you choose? Rock, Paper or Scissors? Type here: ')
        computer_choice = random.choice(choices_list)
        print(f"Computer chose {computer_choice}")

        if (user_input == 'Rock' and computer_choice == 'Scissors') or \
           (user_input == 'Paper' and computer_choice == 'Rock') or \
           (user_input == 'Scissors' and computer_choice == 'Paper'):
            print('AMAZING YOU WON 1 POINT. THE WINNER OF THE GAME IS WHO REACHES 3 POINTS FIRST.')
            count_user += 1
        elif user_input == computer_choice:
            print("It's a tie. Try again.")
        else:
            print('OH NO COMPUTER WON 1 POINT. THE WINNER OF THE GAME IS WHO REACHES 3 POINTS FIRST.')
            count_computer += 1

        print(f'Your points: {count_user} Computers points: {count_computer}')

    print(f'\t\t+++RESULTS+++ \nYOU: {count_user} Computer: {count_computer}')
    if count_user > count_computer:
        print('CONGRATZ YOU WIN!')
    else:
        print('Unfortunately you lose')

game()