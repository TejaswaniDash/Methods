"""
SOME BUILT_IN_FUNCTIONS:

max() : it takes any number of arguments and returns the largest one.
min() : it takes any number of arguments and returns the smallest one.
abs(): It returns the absolute value of the number, that number's distance from 0
It always returns a positive value and it only takes a single number.
type() : It returns the type of the data it receives as an argument.
"""

#max()
#arguments are in numbers
#when there is * it means it can take any number of arguments
def largest_num(*args):
    print(max(args))

#call the method from outside

largest_num(-20, -10, 0, 10, 100)

print('*'*20)

def largest_num(*args):
    print(max(args))
    return(max(args))

#we can return the value and capture in variable x and can use in further

x= largest_num(-20, -10, 0, 10, 100)

#min()

print('*'*20)
#arguments are in numbers
#when there is * it means it can take any number of arguments
def smallest_num(*args):
    print(min(args))

#call the method from outside

smallest_num(-20, -10, 0, 10, 100)

print('*'*20)

def smallest_num(*args):
    print(min(args))
    return(min(args))

#we can return the value and capture in variable x and can use in further

x= smallest_num(-20, -10, 0, 10, 100)

print('*'*20)

#abs()

def abs_function(a):
    print (abs(a))

abs_function(-20)
abs_function(20)

#for both the abs the output result is 20 because the distance from 0 is 20 for bothg


#Type()
print(type(99))
print(type(99.9))
print(type("99.9"))
l=[1,2,3]
print(type(l))


