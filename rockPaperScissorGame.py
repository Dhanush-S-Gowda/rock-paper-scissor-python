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
user_score = 0
comp_score = 0
while True:
    user_choice = input("Enter Rock(R), Paper(P), Scissors(S) \nEnter 'E' to exit\n -->: ")
    if user_choice == 'E':
        break
    rock = '''  
        ______
    ---'  ____)  
        (_____)  
        (_____)  
        (_____)
    ---.__(___)  
    '''

    paper = '''  
        _______
    ---' ______)____
            ________)  
            ________)  
            ________)
    ---.____________)  
    '''

    scissors = '''  
        _______
    ---'   ____)____  
              ______)  
          __________)  
         (____)
    ---.__(___)  
    '''
    print("You choose")
    if user_choice == 'R':
        print("Rock")
        print(rock)
    elif user_choice == 'P':
        print("Paper")
        print(paper)
    elif user_choice == 'S':
        print("Scissors")
        print(scissors)
    else:
        print("-------->    Wrong input     <---------\n")
        continue
    random_choice = random.randint(1, 3)
    print("Computer choose")
    if random_choice == 1:
        computer_choice = 'R'
        print("Rock")
        print(rock)
    elif random_choice == 2:
        computer_choice = 'P'
        print("Paper")
        print(paper)
    else:
        computer_choice = 'S'
        print("Scissors")
        print(scissors)

    if(user_choice == computer_choice):
        print("Draw")
    elif((user_choice == 'R' and computer_choice == 'S') or (user_choice == 'S' and computer_choice == 'P') or (user_choice == 'P' and computer_choice == 'R')):
        print("You won!")
        user_score += 1
    else:
        print("Computer won!")
        comp_score +=1
    print(f"Your Score: {user_score}, computer Score: {comp_score}\n****************************************************************\n")
if(user_score>comp_score):
    print("You have won")
elif(user_score<comp_score):
    print("You have lost")
else:
    print("Its a draw!")
