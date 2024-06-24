# .add()  -- add new string in sets.

scifi = {"start trek", "star wars" , "halo"}
scifi.add("mass effect")
print(scifi)
# OutPut:- {"start trek","mass effect", "star wars" , "halo"}

scifi.add("star wars")
# OutPut:- {"mass effect","start trek", "star wars" , "halo"}
# No change/add in sets bcz, this "star wars" is already availble in sets. And Sets dont support duplicate key/value.


#   .remove()  -- remove items from a set()
fruits = {"apple", "orange", "banana", "tomato"}
fruits.remove("tomato")
print(fruits)

# OutPut:- {"apple", "orange", "banana"}

# fruits.remove("graps")
# OutPut:- ERROR


# .discard() -- same like .remove() but, diff is that .discard() will do nothing.
# Ex. if you want to remove a string which is not present in set() using .remove() . It will give error.
#     if you want to remove a string which is not present in set() using .discard() . It will not give error & dont do anything.

fruits.discard("graps")
# OutPut:- {"apple", "orange", "banana"}

fruits.discard("apple")
# OutPut:- {"orange", "banana"}



# .copy() -- make its own copy.
mountains = {"Everest", "Kilimanjarp", "Fuji"}
set_2 = mountains.copy()
print(set_2 is mountains)  # OutPut:- False. Bcz, value of sets for moutains & set_2 are not same bcz, you make its diff own copy from mountains.

print(mountains)
print(set_2)

# .union() -- to combine /add 2 diff types of sets into a single sets.
ex_1 = {1, 2, 3, 4, 5}
ex_2 = {6, 7, 8, 9, 10}
ex_3 = ex_1.union(ex_2)
print(ex_3)
# OutPut:- {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

ex_4 = ex_2.union(ex_1)
print(ex_4)
# OutPut:- {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

ex_5 = ex_1 | ex_2 # OutPut:- {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# .intersection() -- use to find same , common values in diff sets.

set_1 = {4, 5, 6, 7, 8}
set_2 = {6, 7, 8, 9, 10}
set_3 = set_1.intersection(set_2)
print(set_3)

# OutPut:- {8, 6, 7}

set_4 = set_1 & set_2
print(set_4)
# OutPut:- {8, 6, 7}

# .substractions
set_1 = {4, 5, 6, 7, 8}
set_2 = {6, 7, 8, 9, 10}
set_5 = set_2 - set_1
print(set_5)
# OutPut:- {9, 10}

set_6 = set_1 - set_2
print(set_6)
# OutPutL:- {4, 5}

# .difference()
set_7 = set_1.difference(set_2)
print(set_7)
# OutPut:- {4, 5}

set_8 = set_2.difference(set_1)
print(set_8)
# OutPut:- {9, 10}