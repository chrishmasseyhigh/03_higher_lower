import random

rounds= 20    
while rounds >0:    
    user =random.randint(1,20)
    comp_choice =random.randint(1,20)
    print()
    print(user,comp_choice)
    if user < comp_choice:
        print("lower")
    elif user == comp_choice:
        print("you got it")
    elif user > comp_choice:
        print("higher")
    print()
    rounds -=1