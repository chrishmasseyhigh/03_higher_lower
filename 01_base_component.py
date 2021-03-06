import random
from unittest import result
#Functions go here
#checks the amount of rounds and activate infine mode if user enters enter
def check_rounds(question):
    while True:
        #ask for round amount
        
        response = input(question)

        #error
        round_error = "Please enter an intiger that is more than zero"
        if response !="":
            try:
                response = int(response)

                if response <1:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue
        
        return response

#Yes or no checker
def yes_no(question):
    yes_ok = ["no","n","nope"]
    no_ok = ["yes","y","yep"]

    valid= False 
    while not valid:
            response = input(question).lower()
            #if they say yes, output 'program continues'
            if response in no_ok:
                response= "yes"
                return response
            #if they say no, output 'displays instructions'
            elif response in yes_ok:
                response= "no"
                return response
            #else, output'Please enter yes or no'
            else:
                print()
                print("Please enter yes or no")
                print()

played_before = yes_no("have you played before? ")
if played_before =="no":
    print("instructions")
print()
print("program continues")
print()

rounds_wanted = check_rounds("How many rounds?  Press <enter> for infinite mode: ")
mode=""
if rounds_wanted == "":
    mode = "infinite"
    rounds_wanted = 10

rounds_wanted +=1

# play it
rounds_played = 1
while rounds_played < rounds_wanted:
    print()
    print("-----Round {}-----".format(rounds_played))

    if mode == "infinite":
        rounds_wanted += 1
    
    rounds_played += 1
    user =random.randint(1,20)
    comp_choice =random.randint(1,20)
    print()

    if user < comp_choice:
        result ="lower"
    elif user == comp_choice:
        result = "you got it"
    elif user > comp_choice:
        result = "higher"
    print()
    print("You chose {}, the computor chose {}."
               "\nResult: {}".format(user,comp_choice,result))

    exit = input("xxx to quit... ")

    if exit == "xxx":
        break
    