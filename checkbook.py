from tkinter import N

# prompt function to get user input
user_input = 5
def prompt():
    user_input = input('What would you like to do ? \n \n'
        '1) view current balance \n' 
        '2) record a debit (withdraw) \n' 
        '3) record a credit (deposit) \n' 
        '4) exit \n')
    return user_input

def error(): #need to figure out how to loop this
    if user_input in (1, 2, 3, 4):
        print(f'Your choice? {user_input}' /n)
    else:
        print(f'Your choice? {user_input} \n'
        f'Invalid choice: {user_input} \n')

prompt()
error()
# balance function should call balance upon opening and save upon closing probably through a txt file
# def current_balance()
