#High-Low Game
from random import randint

#function to compare computer number and user number
def compare(user_num, computer_num):
    if user_num<computer_num:
        return "lower"
    else:
        return "higher"

print("Welcome to High-Low Game!")
print("----------------------------------")
NUM_ROUNDS :int=5
user_num:int
user_score:int=0
computer_num:int
computer_score:int

for i in range(NUM_ROUNDS):
    print(f"Round {i+1}")
    user_num= randint(1,100)
    computer_num= randint(1,100)
    print(f"Your Number is {user_num}")
    user_input=input("Do you think your number is higher or lower than the computer's?:")
    result=compare(user_num, computer_num)
    if user_input==result.lower():
        print(f"You were right! The computer's number was {computer_num}")
        user_score+=1
    else:
        print(f"Aww, that's incorrect. The computer number was {computer_num}")
    print(f"Your score is now {user_score}")

print("Thanks for playing!")