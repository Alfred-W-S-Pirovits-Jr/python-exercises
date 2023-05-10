'''# 1a.  
day_of_week = input("What day of the week is it? ")
if day_of_week == 'Monday':
    print("It's Monday!")
else:
    print("It's NOT Monday!")

# 1b.
day_of_week = input("What day of the week is it? ")
if day_of_week in ['Monday', 'Tuesday', 'Wednessday', 'Thursday', "Friday"]:
    print("It's a Weekday!")
else:
    print("It's a Weekend!")

# 1c.
number_of_hours_worked = int(input("How many hours did you work? "))
hourly_rate = int(input("What is your rate? "))

if number_of_hours_worked <= 40:
    print(f"Your pay is {number_of_hours_worked * hourly_rate}")
else:
    print(f"Your pay is {(40 * hourly_rate) + (number_of_hours_worked - 40) * 1.5 * hourly_rate}")


# 2a.

i = 5
while i <= 15:
    print(i)
    i += 1

i = 0
while i <= 100:
    print(i)
    i += 2

i = 2
while i <= 65536:
    print(i)
    i = i * i

i = 100
while i >= 5:
    print(i)
    i -=5

# 2bi.
x = int(input("Give me a number! "))
for n in range(10):
    print(f"{x} x {n + 1} = {x * (n + 1)}")

# 2bii

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for num in numbers:
    print(num * int(num))


# 2ci
positive_integer = int(input("Type in a positive integer: "))
while positive_integer >=1:
    print(positive_integer)
    positive_integer -= 1

# 2cii
positive_integer = int(input("Type in a positive integer: "))
i = 0
while i <= positive_integer:
    print(i)
    i += 1
    '''

'''
# 2 ciii

odd_number = int(input('Type in a positive odd integer between 1 and 50: '))
odd = 1
while odd < 50:
    while (odd_number < 1 or odd_number % 2 == 0 or odd_number > 50):
        print("You're an Idiot --- try again! ")
        odd_number = int(input('Type in a positive odd integer between 1 and 50: '))
    if odd == odd_number:
            if odd == 1:
                print()
                print(f"Number to skip is: {odd_number}")
                print()
                print(f"Yikes!  Skipping number {odd_number}")
                odd += 2
            else:
                print(f"Yikes!  Skipping number {odd_number}")
                odd += 2
                continue
    else:
        if odd == 1: 
            print()
            print(f"Number to skip is: {odd_number}")
            print()
            print(f"Here is an odd number: {odd}")
            odd += 2
        else:
            print(f"Here is an odd number: {odd}")
            odd += 2
'''
'''
# 3.  
for n in range(100):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
'''
'''
# 4. ASK THE USER IF HE WANTS TO CONTINUE
user_prompt = input("Do you want to continue? (y/n)")
if user_prompt == 'y':
    user_input = int(input("What number would you like to go up to? "))
    print()
    print("Here is your Table!")
    print("number | squared | cubed")
    i = 0
    while i <= user_input:
        print(i, "      | ", i * i, "       | ", i * i * i)
        i += 1
else: 
    print("OK! Guh Bie")
'''

'''

# 5.
grade = int(input("Enter a numerical grade from 0 to 100: "))
if grade >= 88:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 67:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
'''
'''
# 6.

books_read = [{'title': 'Think and Grow Rich', 'author': 'Napoleon Hill', 'genre': 'Self Help'},
              {'title': 'The Hobbit', 'author': 'J. R. R. Tolkien', 'genre': 'Fiction'},
              {'title': 'Calculus with Analytic Geometry', 'author': 'George Simmons', 'genre': 'Textbook'},
              {'title': 'Astrophysics for People in a Hurry', 'author': 'Neil DeGrasse Tyson', 'genre': 'Non-fiction'},
              {'title': 'The Obesity Code', 'author': 'Jason Fung', 'genre': 'Health'}]

# i = 0 
# while i < len(books_read):
#     print(books_read[i])
#     i += 1

for book in books_read:
    for key in book.keys():
        print(book[key], end = " ")
    print()

'''

#   BONUS
# USE MAX LENGTH MAYBE

user_prompt = input("Do you want to continue? (y/n)")
if user_prompt == 'y':
    user_input = int(input("What number would you like to go up to? "))
    print()
    print("Here is your Table!")
    print("number | squared | cubed")
    i = 0
    while i <= user_input:
        print(f"{i}\t\t\t"|" {i * i}\t\t\t"|" {i * i * i}")
        i += 1
else: 
    print("OK! Guh Bie")
'''
grade = int(input("Enter a numerical grade from 0 to 100: "))
if grade >= 88:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 67:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
'''