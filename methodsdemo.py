"""
METHODS-
A group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code


#what if we need to run a command / operation repeatedly;
#we have to make our code reusable
#method is nothing but a group of code statements only,
# which is actually going to complete some kind of workflow,
# like addition only, we can complete some kind of workflow into one logical entity,
# and you can call it that it is the way of doing sum,
# it is the way of doing a particular thing, this is the method of doing things.
"""

#define method

def add_nums(): #empty when no arguments are needed
    print( 3 + 2 ) #body describe all the procedure that our method going to carry out

#we have to call the method to use it
add_nums()
#to reuse to method let's
def add_nums(n1,n2):
    print( n1 + n2 )
add_nums(2,8)

add_nums(3,10)

#define list

l=[1,2,3]
print(l.append(4))
print(l)

len(l)
print(len(l))

#append() accepted one parameter 4, and we passed in that.
# So it depends on what we want to do with the methods.
# It's not mandatory to have the arguments always,
#it depends on what how we want to use them and what we want to achieve with the method.

print('*'*20)
"""
WORKING WITH RETURN VALUES

"""

def sum_nums(n1,n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:

    """
#this is helpful when somebody else uses your code,
    # and they're trying to understand what your code is doing,
    # what this method is doing basically, so they can get the feeling that, okay,
    # this is the description of the method, it takes two parameters,
    # what does those parameters mean, and what does this method return.
    print( n1 + n2 )
    return n1 + n2

sum1 = sum_nums(2,8)

sum2 = sum_nums(3,10)

#let's say i want to save the value and use the value further in the codes
#in thet case we can use the key word return -it allow us to return a result from method
#we can store this return in any variable to use it in further

def isMetro(city):
    l=['sfo','nyc','la']
#let's just keep these three cities in the list.
# And we're just trying to find that if someone calls this method from outside,
# and provide a city name,
#whatever the caller is giving us, if that city is a metro or if it's not a metro.

    if city in l:
        return True
    else:
        return False

x = isMetro('sfo')
print(x)

y = isMetro('boston')
print(y)

string_add = sum_nums('one','two')
print(string_add) #here it is concatenating #high chance of error

"""
WORKING WITH POSITIONAL/OPTIONAL PARAMETERS

"""

#we can assign a default value to the positional parameter if no value is provided from outside.
# So let's make it a positional parameter.
print('*'*20)
#position matter in case of normal argument
#In poitional parameter we can position them anywheere- we can interchange the position, we can assign values
def sum_nums(n1=2, n2=4):
    """

    :param n1:
    :param n2:
    :return:
    """
    return n1+n2
sum1 = sum_nums(n1=8, n2=12)
print(sum1)

print('*'*20)
#let's not pass any parameter here and see what happens
def sum_nums(n1=2, n2=4):
    """

    :param n1:
    :param n2:
    :return:
    """
    return n1+n2
sum2 = sum_nums()
print(sum2)

#sum2 = sum_nums() previously we saw if we try to call the method without providing parameters; because it needs to 2 parameters
#it gives error
#it doesn't happen in positional parameter because they can act like optional parameter
#as they have default value

print('*'*20)
#linstead of 8 and 12 we can put n1=8 and n2=12
def sum_nums(n1=2, n2=4):
    """

    :param n1:
    :param n2:
    :return:
    """
    return n1+n2
sum2 = sum_nums(n2=12 , n1=8)
print(sum2)
#position of parameter doesn't matter
print('*'*20)
#when we don't pass a value for a parameter it will take the default value;
#here we are not assigning value to n2 that's why it is taking by default value of n2 i.e.4
def sum_nums(n1=2, n2=4):
    """

    :param n1:
    :param n2:
    :return:
    """
    return n1+n2
sum2 = sum_nums(n1=8)
print(sum2)

print('*'*20)
#we can use the precedent effective value when we passing a value in mix match manner also
def sum_nums(n1=2, n2=4):
    """

    :param n1:
    :param n2:
    :return:
    """
    return n1+n2
sum2 = sum_nums(4, n2=12)
print(sum2)