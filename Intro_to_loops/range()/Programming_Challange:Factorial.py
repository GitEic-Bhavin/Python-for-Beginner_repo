# Programming Challenge: Factorial

# Create a function which takes one positive integer as its input and returns its factorial.

# To make sure that your function works correctly, 
# you should call it with the inputs 3, 4, and 5 and print what is returned by those calls. 
# For those inputs, you should get 6, 24, and 120, respectively.


# Defined value 3,4,5 when calling function.

def factorial(integer_num):
    returned = 1
    
    for item in range(integer_num, 1,-1):
        returned *= item  # this will stores , multipled items after each loop.
        
        # first input is 3 when  calling function,
        # it go under function range(integer_num = 3, 1, -1)  -- 3 will decrease by -1 till it reach 1.
        # after this 3 will stores in vars retuerned & multiplied by items
        
    return returned
print(factorial(3))
print(factorial(4))
print(factorial(5))

# To get input from user

fact1 = int(input("Enter integer to get factorial"))
fact2 = int(input("Enter integer to get factorial"))
fact3 = int(input("Enter integer to get factorial"))

def factorial(integer_num):
    returned = 1
    
    for item in range(integer_num, 1,-1):
        returned *= item
        
    return returned
print(factorial(fact1))
print(factorial(fact2))
print(factorial(fact3))
        
        