# Programming Challenge: 
# Find The Number of Characters in A String

# In a .py file, write a program which calculates the number of characters in a string.

# The string should be entered using input() and assigned to a variable. 

# Use print() twice at the end of your program. 
# The first print() will print the string that the user entered and the second print() will display the number of characters in the string. 
# For example, if the user entered the string "hello world", the number of characters would be 11.

strings = str(input("Enter any string to calculate its all character"))
counter = 0

for character in strings:
    counter += 1
    
print(strings)
print(counter)

# OutPut:-
# hi
# 2


# strings = str(input("Enter any string to calculate its all character"))
# counter = 0

# for character in strings:
#     counter += 1
    
#     print(character)
#     print(counter)
    
# OutPut:-
# Enter any string to calculate its all characterhi
# h
# 1
# i
# 2

# strings = str(input("Enter any string to calculate its all character"))
# counter = 0

# for character in strings:
#     counter += 1
    
#     print(character)  # It will print each sigle character then,
# print(counter)        # print each counter lieke 1 after "h" character, 2 after "i" character.

# OutPut:-
# Enter any string to calculate its all characterhi
# h
# i
# 2

# word = "hello worls"

# for letter in word:
#     print(letter)