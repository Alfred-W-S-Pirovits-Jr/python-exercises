#  1.  

# 99.9 is a float
# "False" is a string
# False is boolean
# '0' is a string
# 0 is an int
# True is boolean
# 'True' is a string
# [{}] is a list
#  {'a';[]} is a dictionary 


#  2.  
"""
strings are best for a term or phrase typed into a search box
boolean is best to determine whether or not a user is logged in
float would be best for a discount
boolean is best for whether or not a coupon code is valid
string is best for an email address
float is best for a the price of a product
lists are bests for email addresses collected on a registration form unless paired with a name
    or something where a dictionary might be better
Dictionaries are great fot iformation about applicants to codeup

"""

#  3 

# '1' + 2 will give a TypeError
# 6 % 4  will give 2
# type(6 % 4) will give <class int>
# type(type(6 % 4)) will give <class 'type'>
# '3 + 4 is' + 3 + 4 will give an error saying you cannnot concatenate two types
# 0 < 0 will give False
# 'False' == False will give False
# True == 'True will give False
# 5 >= -5 will give True
# True or "42" will give True
# 6 % 5 will give 1
# 5 < 4 and 1 == 1 will give False
# 'codeup' == 'codeup' and 'codeup' == 'Codeup' will give False
# 4 >= 0 and 1 !== '1' will give an error syntax
# 6 % 3 will give 0
# 5 % 2 != 0 will give True
# [1] + 2 will give a TypeError cnanot concatenate an int to a list
# [1] + [2] will give [1, 2]
# [1] * 2 will give [1, 1]
# [1] * [2] will give will give an error you cannot multiply lists
# [] + [] == [] will give True
# {} + {} will give error cannot concatenate dictionaries

# 4
# 5 

daily_fee = 3 
lm_length = 3
bb_length = 3
h_length = 1
total_cost = daily_fee * (lm_length + bb_length + h_length)
print(total_cost)

# 6
google_hourly = 400
amazon_hourly = 380
facebook_hourly = 350

this_weeks_earnings = 10 * facebook_hourly + 6 * google_hourly + 4 * amazon_hourly
print(this_weeks_earnings)

# 7
class_not_full = True
no_class_conflict = True
can_take = (class_not_full and no_class_conflict)
print(can_take)

# 8
offer_expired = False
no_purchased = 3
product_offer = offer_expired == False and no_purchased >= 2
print(product_offer)

# 9
username = 'codeup'
password = 'notastrongpassword'
ok = len(password) >= 5 and len(username) <= 20 and password != username
print(ok)

# BONUS
username = 'codeup       '
strip_username = username.strip()
password = '         notastrongpassword'
strip_password = password.strip()
ok = len(strip_password) >= 5 and len(strip_username) <= 20 and password != username
print(ok)

