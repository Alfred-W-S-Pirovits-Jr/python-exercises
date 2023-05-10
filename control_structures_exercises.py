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
odd = 2
while odd.isdigit() == FALSE and odd % 2 ==0:
    odd = input("Type in a n odd integer between 1 and 50: ")
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
# 4.
user_input = int(input("What number would you like to go up to? "))
print()
print("Here is your Table!")
print("number | squared | cubed")
i = 0
while i <= user_input:
    print(i, "      | ", i * i, "       | ", i * i * i)
    i += 1
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
