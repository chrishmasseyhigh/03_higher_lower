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
#asks for rounds
rounds_wanted = check_rounds("How many rounds?  Press <enter> for infinite mode: ")
mode=""
if rounds_wanted == "":
    mode = "infinite"
    rounds_wanted = 10


input_2 =0
# play it
rounds_played = 0
user = 0
while rounds_played < rounds_wanted:
    print()
    #asks to quit
    if user =="xxx":
        keep_going = input("press enter to quit ")
        if keep_going == "":
           rounds_played -=1
           break
        else:
            print()
            rounds_played -=1
    rounds_played += 1
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

    print()
    #tells user what number amount they can chose from
    print("chose a number bettwen {} and {} ".format(lower,higher))
    while result == "lower" or "higher":
        print()
        user = check_rounds_2("Number? ")
        
        print()
        if user =="xxx":
            result = "xxx"
            break
        if user < comp_choice:
            input_2 +=1
            result ="higher"
        elif user == comp_choice:

            result = "you got it"
            print()
            print("You chose {}".format(user,result))
            print()
            statement_decorator("you won","!")
            print()
            print("))))number was {}((((".format(comp_choice))
            user_input_history_list.append(user)
            result_history_list.append(result) 
            break
        elif user > comp_choice:
            input_2 +=1
            result = "lower"
        #records history
        user_input_history_list.append(user)
        result_history_list.append(result) 
        #pribnts reult and choice
        print("You chose {}"
                "\nResult: {}".format(user,result))

list_amount = 0
items = 1
items_3 =1
print("----round {}----".format(items))
items = 0
# prints user history
while items < rounds_played:
    
    item_2 = 1
    
    while item_2 < input_2 :
        
        user_history = user_input_history_list[list_amount]
        result_history = result_history_list[list_amount]
        #prints what was chosen
        print("{} choice ".format(item_2))
        print(" you chose ({}) number was was ({})".format(user_history,result_history))
        if result_history =="you got it":
            item_2 = input_2
        item_2 +=1
        list_amount +=1
    items +=1
    items_3 +=1
    if rounds_played >1:
        print("----round {}----".format(items_3))
    else:
        break
    
    list_amount +=1
print()
statement_decorator("Thank you for playing","=")