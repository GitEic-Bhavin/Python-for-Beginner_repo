# Introduction to sets

# Sets is diff with 2 ways compair to list
# Sets  -- can't have duplicate/repeated values.
#       -- Items contains are unordered

# How to create SETS ?
# 1. use {}    2. use set({})

set_1 = {9, 8, 7, 6}
print(set_1)  # OutPut:- {8, 9, 6, 7}

set_2 = set({"a", "b", "c", "d"})
print(set_2)  # OutPut:- {"a", "d", "b", "c"}

set_3 = set({"a", "b", "b", "c", "d"})
print(set_3)  # OutPut:- {"b", "d", "a", "c"}

# Use range
set_4 = set(range(1, 12, 2))
# OutPut:- {1, 3, 5, 7 ,9, 11}


# sets holds diff data type in sigle sets
set_5 = {"a", 3.14, 18, True}
print(set_5)  # OutPut:- {True, 18, 3.14, "a"}

# SETS are unordered, so you can not access its index number.
# You have to use for loops

set_6 = {3, 6, 9, 12, 15}

for num in set_5:
    print(num)

# OutPut:-
# 3
# 6
# 9
# 12
# 15


set_7 = {3, 6, 9, 12, 15}
print(12 in set_7)  # OutPut:- True

print(10 in set_7)  # OutPut:- False



# SETS Comprehensions

comp_1 = {even+2 for even in range(2, 11, 2)}
print(comp_1)
# OutPut:- {4, 6, 8, 10, 12}

# range(2, 11, 2)  -- start from 2 till 11 with increment 2
# even+2 = will add 2 after each iteration for range(2, 11, 2)

comp_2 = {char.lower() for char in "ALLCAPS"}
print(comp_2)
# OutPut:- {'a', 'p', 's', 'l', 'c'}
