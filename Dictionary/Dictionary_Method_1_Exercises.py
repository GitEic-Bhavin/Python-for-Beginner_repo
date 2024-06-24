# dictionary methods 1 exercises

# Do all of this in a .py file in Pycharm.

# create a variable and assign it the following dictionary:

# {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
dict = {"Queen": "Bohemian Rhapsody",
        "Bee Gees": "Stayin' Alive", 
        "U2": "One", 
        "Michael Jackson": "Billie Jean", 
        "The Beatles": "Hey Jude", 
        "Bob Dylan": "Like A Rolling Stone"}

# make the dictionary span multiple lines so that the line the dictionary starts on is not too long.

# print the length of the dictionary.
print(len(dict))
# OutPut:- 6

# use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.
for key in dict.keys():
    print(key)
# OutPut:-
# Queen
# Bee Gees
# U2
# Michael Jackson
# The Beatles
# Bob Dylan

# print all of the values from the dictionary using the .values() method.
print(dict.values())
# OutPut:- dict_values(['Bohemian Rhapsody', "Stayin' Alive", 'One', 'Billie Jean', 'Hey Jude', 'Like A Rolling Stone'])

# use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.
for key in dict.items():
    print(key)
# OutPut:-
# ('Queen', 'Bohemian Rhapsody')
# ('Bee Gees', "Stayin' Alive")
# ('U2', 'One')
# ('Michael Jackson', 'Billie Jean')
# ('The Beatles', 'Hey Jude')
# ('Bob Dylan', 'Like A Rolling Stone')  

# OR
for key, value in dict.items():
    print(key, value)

# OutPut:-
# Queen Bohemian Rhapsody
# Bee Gees Stayin' Alive
# U2 One
# Michael Jackson Billie Jean
# The Beatles Hey Jude
# Bob Dylan Like A Rolling Stone

# use the .get() method to check the dictionary for the key
print(dict.get("Promise of the Real", "This key is not found in dict."))
# OutPut:- This key is not found in dict.

# "Promise of the Real"
# and create a message that will print if the key is not found in the dictionary.

