def is_two(n):
    return n == 2 or n == '2'


def is_vowel(v):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return v in vowel_list

def cap_first_letter(word): #NOT DONE!!! lowercasing all letters then capitalizing the first
    l = []
    new_word = ''
    word = word.lower()
    l = list(word)
    l[0] = l[0].upper()
    for _ in l:
        new_word += _
    return new_word

def calculate_tip(bill, x):
    # bill = float(input('What was the bill total? '))
    # x = float(input('What percent would you like to tip as a decimal between 0 and 1? '))
    if 0 <= x <= 1:
        tip = bill * x
        print(f'Your tip is equal to {tip}')
    else: 
        print('FOLLOW INSTRUCTIONS!!!')


def apply_discount(original_price, discount_percentage): #I am abandoning the decimal for a whole number
    #original_price = float(input('How much is the item? '))
    #discount_percentage = float(input('What percent is your discount as a whole number? '))
    print(f'Your new price is: {original_price * (100 - discount_percentage) / 100}')


def handle_commas(number) -> 'Number as a string' :
    new_number = ''
    n = []
    n = list(number)
    for _ in n:
        if _ == ',':
            n.remove(',')
    for _ in n:
        new_number += _
    return new_number

def get_letter_grade(number_grade) -> "float":
    
    if number_grade >= 90:
        return 'A'
    elif number_grade >= 80:
        return 'B'
    elif number_grade >= 70:
        return 'C'
    elif number_grade >= 60:
        return 'D'
    else:
        return 'F'
    
    def remove_vowels(word):
        new_word = ''
        word = list(word)
        vowels = ['a','e','i','o', 'u', 'A', 'E', 'I', 'O', 'U']
        for letter in word:
            if letter in vowels:
                word.remove(letter)
        for _ in word:
            new_word += _
    return new_word

## do number 10

def cumulative_sum(numbers):
    new_list = [numbers[0]] #initialize new_list with first item
    running_total = numbers[0] # holds the running total for list
    for n in range(len(numbers) - 1):
        n = n + 1
        new_list.append(numbers[n] + running_total)
        running_total = numbers[n] + running_total
    return new_list
    
