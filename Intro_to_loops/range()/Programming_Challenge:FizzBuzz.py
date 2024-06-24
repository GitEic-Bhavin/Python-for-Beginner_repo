# Programming Challenge: Fizz Buzz
# Write a program that iterates over the integers 1 through 50 using a loop.

# However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output. 
# For example, 15 is divisible by both 3 and 5, so instead of printing 15, print "FizzBuzz". 
# For numbers which are multiples of 3 but not 5 (such as 42) print “Fizz” instead of the number.  
# For the numbers that are multiples of 5 but not 3 (such as 20) print “Buzz” instead of the number.

# All of the integers which are not multiples of 3 or 5 should just be printed as themselves.

two_inputs = range(1, 51)

for num in two_inputs:
    if num % 3 and 5:
        print(str(num) + " FizzBuzz")
        if num % 3:
            print(str(num) + " Fizz")
            if num % 5:
                print(str(num) + " Buzz") 
    else: 
        print(str(num) + " is not divided by 3 or 5")
        
        
        # OR Using elif loops
        
for num in range(1, 51):
    
    # If num is divisible by both 3 and 5, "FizzBuzz" will be printed.
    
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        
    # If num is only divisible by 3, "Fizz" will be printed.
    
    elif num % 3 == 0:
        print("Fizz")
        
    # If num is only divisible by 5, "Buzz" will be printed.
    
    elif num % 5 == 0:
        print("Buzz")
        
    # num itself will be printed in all other cases.
    
    else:
        print(num)