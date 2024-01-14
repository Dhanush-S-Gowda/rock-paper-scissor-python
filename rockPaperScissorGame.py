import random
welcome = '''
 __          __  _                           
 \ \        / / | |                          
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
    \  /\  /  __/ | (_| (_) | | | | | |  __/ 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___| 
                            
'''
print(welcome)
score = 0
while True:
    user_choice = input("Enter Rock(R), Paper(P), Scissors(S) \nEnter 'E' to exit\n -->: ")
    if user_choice == 'E':
        break
    rock = '''  
        _______
    ---'   ____)  
        (_____)  
        (_____)  
        (____)
    ---.__(___)  
    '''

    paper = '''  
        _______
    ---'   ____)____  
            ______)  
            _______)  
            _______)
    ---.__________)  
    '''

    scissors = '''  
        _______
    ---'   ____)____  
            ______)  
        __________)  
        (____)
    ---.__(___)  
    '''
    print("You choose\n")
    if user_choice == 'R':
        print(rock)
    elif user_choice == 'P':
        print(paper)
    elif user_choice == 'S':
        print(scissors)
    else:
        print("-------->    Wrong input     <---------\n")
        continue
    random_choice = random.randint(1, 3)
    print("Computer choose\n")
    if random_choice == 1:
        computer_choice = 'R'
        print(rock)
    elif random_choice == 2:
        computer_choice = 'P'
        print(paper)
    else:
        computer_choice = 'S'
        print(scissors)

    if(user_choice == computer_choice):
        print("Draw")
    elif((user_choice == 'R' and computer_choice == 'S') or (user_choice == 'S' and computer_choice == 'P') or (user_choice == 'P' and computer_choice == 'R')):
        print("You won!")
        score += 1
    else:
        print("Computer won!")
    print(f"Your Score: {score}\n****************************************************************\n")
