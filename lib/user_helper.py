#!/usr/bin/env python3

from Models.user import User
def exit():
    print("Thank you! for visiting us.")


# We'll implement the user functions in this lesson
def create_user():
    name = input ("Enter the user's name: ")
    location = input("Enter the users's password: ")
    try:
        user = User.create(name, location)
        print(f'Success: {user}')
    except Exception as exc:
        print("Error creating user: ", exc)

def create_account():

    pass

def deposit_funds():
    print('deposit')
    pass

def check_balance():
    print('balance')
    pass

def transfer_funds():
    print('transfer')
    pass

def withdraw_funds():
    print('withdraw')
    pass

