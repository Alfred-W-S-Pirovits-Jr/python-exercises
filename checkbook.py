from tkinter import N

user_option = 0

def main():
    print('\n ~~~ Welcome to your terminal checkbook! ~~~ \n')
     #initialize user_options
    continue_or_error() # prompt function to get user input

#user_input = 0
def prompt(): #Function for initial prompt
    global user_option #found another way around scope issues!!!
    user_option = input('What would you like to do ? \n \n'
        '1) view current balance \n' 
        '2) record a debit (withdraw) \n' 
        '3) record a credit (deposit) \n' 
        '4) exit \n \n'
        'Your choice? ')

    return user_option


def continue_or_error(): #Loops through the options until user chooses to exit
    while user_option != 4:
        prompt() #loop and a break?
        if user_option == '1':
            current_balance() # insert a view current balance function
            break
        elif user_option == '2': # insert debit function
            debit()
            break
        elif user_option == '3': # insert credit function
            credit()
            break
        elif user_option == '4': # insert exit function
            print('\nThanks, have a great day!')
            break 
        else:
            print(f'Invalid choice: {user_option} \n')

def current_balance(): #read the current balance from the balance.txt file?
    print(f'\nYour current balance is 100.\n')

def debit():
    input(f'\nHow much would you like to wittdraw? ') # if entry is less than balance then balance minus entry
     # else print your available balance is {} you will overdraw account

def credit(): # adds the user input to the total balance
    input(f'\nHow much would you like to deposit?')

def exit():  #perhaps not needed but records and saves current balance
    print('\nThanks, have a great day!')


main()


# balance function should call balance upon opening and save upon closing probably through a txt file
# def current_balance()


"""
KEEP JUST IN CASE

def continue_or_error(): #Do I need to figure out how to loop this?

    # while != 4 loop and a break?
    if user_input == '1':
        print()
        # insert a view current balance function
    elif user_input == '2':
        print()
        # insert debit function
    elif user_input == '3':
        print()
        # insert credit function
    elif user_input == '4':
        # insert exit function
        print('\nThanks, have a great day!')
        # break 
    else:
        print(f'Invalid choice: {user_input} \n')
"""


