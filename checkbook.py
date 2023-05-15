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
            current_balance() # insert a view current balance function and loops to continue DONE!!!
        elif user_option == '2': # insert debit function
            debit()
            
        elif user_option == '3': # insert credit function
            credit()
            
        elif user_option == '4': # insert exit function
            print('\nThanks, have a great day!')
            break 
        else:
            print(f'Invalid choice: {user_option} \n')

def current_balance(): #read the current balance from the balance.txt file?
    with open('balance.txt', 'r') as f:
        last_line = f.readlines()[-1]
    print(f'\nYour current balance is {last_line}.\n')
    continue_prompt()

def debit():
    with open('balance.txt', 'r') as f:
        last_line = float(f.readlines()[-1])
        withdrawal = (input(f'\nHow much would you like to withdraw? '))
    if isfloat(withdrawal) == True:
        withdrawal = round(float(withdrawal), 2)
        if withdrawal < 0:
            print('You cannot withdrawal a negative number. That would be a DEPOSIT. ')
            continue_prompt()
        elif withdrawal <= last_line:
            balance = last_line - withdrawal
            with open('balance.txt', 'a') as f:
                f.writelines([f'\n{balance}'])  # if entry is less than balance then balance minus entry
            print(f'\nYou have Withdrawn ${withdrawal: .2f}:')
            print(f'\nYou have ${balance: .2f} remaining.\n')
            continue_prompt()
        else:
            print(f'\nYou only have ${last_line: .2f} in your account.\nWithdrawing ${withdrawal: .2f} will overdraft your account!\n\n')
            continue_prompt()
    else:
        print('Please type in a valid number: ')
        continue_prompt()

     # else print your available balance is {} you will overdraw account

def credit(): # adds the user input to the total balance
    with open('balance.txt', 'r') as f:
        last_line = float(f.readlines()[-1])
        deposit = input(f'\nHow much would you like to deposit? ')
    if isfloat(deposit) == True:
        deposit = round(float(deposit), 2)
        if deposit >= 0:
            balance = last_line + deposit
            with open('balance.txt', 'a') as f:
                f.writelines([f'\n{balance}'])
            print(f'\nYou have deposited ${deposit: .2f}:')
            print(f'\nYou have ${balance: .2f} remaining.\n')
            continue_prompt()
        elif deposit < 0:
            print('You cannot deposit a negative number.  That would be a WITHDRAWAL! ')
            continue_prompt()
    else: 
        print('Please type in a valid number: ')
        continue_prompt()

def exit():  #perhaps not needed but records and saves current balance
    print('\nThanks, have a great day!')

def continue_prompt(): #prompts user to continue 
    c = 0
    while c != 'y':
            c = input('Would you like to continue? (y/n) ')
            if c == 'n':
                global user_option
                user_option = 4
                break
            elif c == 'y':
                continue
            else:
                print('Please enter y or n')

def isfloat(num):  #Checks user puts in valid float
    try:
        float(num)
        return True
    except ValueError:
        return False

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


