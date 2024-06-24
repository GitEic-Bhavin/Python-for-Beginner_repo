# <!-- Programming Challenge: Roman Numeral Equivalent

# For this exercise, start by creating a variable and assigning it a randomly generated integer between and inclusive of both 1 and 10.

# Then, using your knowledge of if, elif, and else statements, 
# create a program which prints the roman numeral equivalent of the randomly generated number.

# For example, if the randomly generated integer was 9, 
# then the program would say that the roman numeral equivalent of 9 is IX in the output. -->

from random import randint

random_value = randint(1, 10)

if random_value == 1:
    print("Roman numeral equivalent of " + str(random_value) + " is I")
    
elif random_value == 2:
    print("Roman numeral equivalent of " + str(random_value) + " is II")
    
elif random_value == 3:
    print("Roman numeral equivalent of " + str(random_value) + " is III")
    
elif random_value == 4:
    print("Roman numeral equivalent of " + str(random_value) + " is IV")
    
elif random_value == 5:
    print("Roman numeral equivalent of " + str(random_value) + " is V")
    
elif random_value == 6:
    print("Roman numeral equivalent of " + str(random_value) + " is VI")
    
elif random_value == 7:
    print("Roman numeral equivalent of " + str(random_value) + " is VII")
    
elif random_value == 8:
    print("Roman numeral equivalent of " + str(random_value) + " is VIII")
    
elif random_value == 9:
    print("Roman numeral equivalent of " + str(random_value) + " is IX")
    
else:
    print("Roman numeral equivalent of " + str(random_value) + " is X")
    
# OutPut:-

# Roman numeral equivalent of 9 is IX

# Roman numeral equivalent of 8 is VIII

# Roman numeral equivalent of 1 is I

# Roman numeral equivalent of 5 is V

# Roman numeral equivalent of 2 is II

# Roman numeral equivalent of 10 is X