import os ;import sys ;import subprocess
import random
from tkinter import E
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
#checks the amount of rounds and activate infine mode if user enters enter
def check_rounds_2(question):
    while True:
        #ask for round amount
        
        response = input(question)

        #error
        round_error = "Please enter an intiger that is more than zero"

        if response !="xxx":
            try:
                response = int(response)

                if response <1:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue
        
        return response


#statement decorator
def statement_decorator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement,sides)
    top_bottom = decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

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

# Displays instructions, returns ""
def instructions():
    print()
    statement_decorator("How To Play",".")

    print('''

    *******************************************************************************************
    *You will first eneter a number of rounds you want to play for or enter for infinite mode.****************************************************
    *Next you will enter a number and the game will tell you if it is higher or lower or yiou can press enter to restart the code or xxx to quit.* 
    *At the end tt will reveal the number and dispay your win rate and choices.*******************************************************************
    **************************************************************************
    ''',)

    return""

# ******* main rotine ********
user_input_history_list = []
result_history_list = []
statement_decorator("Welcome to the higher lower game","/")
print()
played_before = yes_no("have you played before? ")
if played_before =="no":
    instructions()
print()


print()
rounds_wanted = check_rounds("How many rounds?  Press <enter> for infinite mode: ")
mode=""
if rounds_wanted == "":
    mode = "infinite"
    rounds_wanted = 10

rounds_wanted +=1

# play it
rounds_played = 1
user = 0
while rounds_played < rounds_wanted:
    print()
    
    if user =="xxx":
        keep_going = input("press enter to quit ")
        if keep_going == "":
           rounds_played = 0
           break
        else:
            print()
    
    print("-----Round {}-----".format(rounds_played))
    #asks user if they want their own range and asks for numbers
    range_yes = yes_no("Want to enter your own range? ")

    if range_yes == "yes":
        print()
        lower = check_rounds_2("lower number: ")
        print()
        higher = check_rounds_2("Higher number: ")
    else:
        lower=1
        higher = 20
    # choses random number
    comp_choice =random.randint(lower,higher)
    if mode == "infinite":
        rounds_wanted += 1
    result = "lower"
    rounds_played += 1
    print()
    print("chose a number bettwen {} and {} ".format(lower,higher))
    while result == "lower" or "higher":
        print()
        user = check_rounds_2("Number? ")
        print()
        if user =="xxx":
            break
        if user < comp_choice:
            result ="lower"
        elif user == comp_choice:
            result = "you got it"
            print()
            print("You chose {}".format(user,result))
            print()
            statement_decorator("you won","!")
            result_history_list.append(result) 
            break
        elif user > comp_choice:
            result = "higher"

        result_history_list.append(result) 
        
        print()
        print("You chose {}"
                "\nResult: {}".format(user,result))
    

list_amount= 0
items =0
print()
print("))))number was {}((((".format(comp_choice))


while items< rounds_played:
        if list_amount == rounds_played -1:
            break
        elif rounds_played == 0:
            break

        items +=1
        
        user_history = user_input_history_list[list_amount]
        result_history = result_history_list[list_amount]
        print("round {}, you chose ({}) your choice was ({})".format(items,user_history,result_history))

        list_amount +=1
print()
statement_decorator("Thank you for playing","=")