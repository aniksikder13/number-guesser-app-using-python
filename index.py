import  random
low= 1
high= 50

correct_answer = random.randint(low, high)

def repeatGame():
    user_agree = input('If you want to restart, Please type "yes": ').lower()
    if user_agree == 'yes':
        game()
def game():
    chance = 5
    win = False
    for num in range(0, 5):
        user_val = int(input('Please type a number between 1 & 50: '))

        if user_val < low or user_val > high:
            print('You type a invalid number')
            repeatGame()
            break
        if correct_answer == user_val:
            win = True
            break
        elif correct_answer > user_val:
            chance -= 1
            print(f'Correct answer is smaller!\n You have {chance} chances left')
        elif correct_answer < user_val:
            chance -= 1
            print(f'Correct answer is greater!\n You have {chance} chances left')

    if not win:
        print('You Lose!')
        repeatGame()
    else:
        print('You Win!')
        repeatGame()
game()

