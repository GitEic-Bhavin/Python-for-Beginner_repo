# To make Upper Case

all_lower = "there are no capitals here."

print(all_lower.upper())
# OutPut:-
# THERE ARE NO CPAITALS HERE.

print(all_lower)
# OutPut:-
# there are no capitals here.

# To make lower case 

all_upper = "THIS IS SHOUTING TEXT!"
print(all_upper.lower())
# OutPut:-
# this is shouting text!

# .isupper() and .islower() string method
is_upper = "this is a string"
print(is_upper.isupper())
# OutPut:- False

is_upper = "THIS IS A STRING"
print(is_upper.isupper())
# OutPut:- TRUE

# .islower()
is_lower = "THIS IS A STRING"
print(is_lower.islower())
# OutPut:- False

is_lower = "this is a string"
print(is_lower.islower())
# OutPut:- TRUE


# .isalpha()  -- give true only when contains only letters, not int, float, numbers.
print("Batman".isalpha())
# OutPut:- TRUE

print("Batman123".isalpha())
# OutPut:- False


# .isalnum() -- give True only when contains only letters, numbers, not symbols like ?, #, $, %
print("Batman123".isalnum())
# OutPut:- True

print("Batman".isalnum())
# OutPut:- 


print("Batman123@#".isalnum())
# OutPut:- False


# .isdecimal -- give True only when contains only integer numbers , not for float, string, symbols etc.
print("1234".isdecimal())
# OutPut:- True

print("Hello 1234".isdecimal())
# OutPut:- False

print("#$1234".isdecimal())
# OutPut:- False

print("3.14".isdecimal())
# OutPut:- False

# .isspace() -- give TRUE only when contains only SPACE "     ".
print("  ".isspace())
# OutPut:- True

print(" 12STIng@".isspace())
# OutPut:-  False

print("not just spaces"[3].isspace())
# OutPut:- True


# .istitle() -- give True only when each words has first charaacter should be Capital.
# Ex. Hello World -- title

print("Hello World".istitle())
# OutPut:- True

print("hello World".istitle())
# OutPut:- False

print("Hello Worls: Good Mornign !".istitle())
# OutPut:- True

# To make lower/upper case to title case
print("hello WOrld".title())
# OutPut:- Hello World




# .startswith() and .endswith()

print("this is the string".startswith("this"))
# OutPut:- True

print("this is the string".startswith("This"))
# OutPut:- False

print("this is the string".startswith("t"))
# OutPut:- True

print("this is the string".endswith("string"))
# OutPut:- True

print("this is the string".endswith("String"))
# OutPut:- False

print("this is the string".endswith("g"))
# OutPut:- True

# With ! mark
print("this is the string!".endswith("string!"))
# OutPut:- True





#     .join() -- when you want to combine multiple stings, words into a single string.
# Ex. one ,  two, three -- onetwothree

print("-".join(["one", "two", "three"]))

# "-" is a joiner like seperator in awk command.
# "" -- means, all 3 words will be joint with not space -- onetwothree
# OutPut:- one-two-three

print("".join(["one", "two", "three"]))
# OutPut:- onetwothree

print(", ".join(["one", "two", "three"]))
# OutPut:- one, two, three

print(" ".join(["one", "two","three"]))
# OutPut:- one twp three


# .split() -- will do opposite of .join()
# It will split the words by sperator like " ", ",", ", ", ":", "-"

print("Eggs, Milk, Waffles, Bacon".split(","))
# OutPut:- ['Eggs', ' Milk', ' Waffles', ' Bacon']

print("Eggs, Milk, Waffles, Bacon".split(", "))
# OutPut:- ['Eggs', 'Milk', 'Waffles', 'Bacon']





# print("Bat-man".isalnum("-"))


print("Batman123".isalnum())

        # if i.alnum() or i.isspace() or i == "-" or i == "'":
