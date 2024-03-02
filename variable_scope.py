#a variable inside a method that we define is having a local scope
#it cannot be used outside of the method.

a=10 #outside the method
def test_method(a): #here the 'a' is call from somewhere outside. it in not the above assigned 'a"
    print('Value of local a is:' + str(a))
    a = 2
    print('New value of local a is:' + str(a))

print ('Value of global a is' + str(a))
test_method(a)
print("Did the value of global a change?" + str(a))

print('*'*20)
#let's use the global variable
a = 10
def test_method():
    global a
    print("Value of 'a' inside the method is: " + str(a))
    a = 2
    print("New value of 'a' inside the method is changed to:" + str(a))

print ("Value of global a is" + str(a))
test_method()
print("Did the value of global a change?" + str(a))

#we can change the value of global variable by using the global key word
