'''
from importlib.abc import ExecutionLoader
from unittest import result


How to make a function

def name_of_function(parameters):
    Steps of Execution
    return result

name_of_function(arguments)

dict_of_arguments = {
    'greeting' : 'Greetings',
    'name': 'Ryan'
}
say_hello(**dict_of_arguments)

functions can reach outside to get variables BUT

lambda functions
a one off function to do something

add one 

add_one = lambda n : n+1
# not declaring a variable just creating a one line function
add_one(9)
square = lambda n: n**2
'''
add = lambda x, y : x + y
n = add(2,3)
print(n)