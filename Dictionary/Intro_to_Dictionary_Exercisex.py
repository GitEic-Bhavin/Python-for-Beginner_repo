# introduction to dictionaries exercises

# Do all of this in a .py file in Pycharm.

# create a variable and assign it a dictionary that has 5 key value pairs
pair = {False: "CPU is software", 3.14: 40, "Ansible": "config", "terraform": "IAC_Tool", 1: 80}

# print and access the value held at the third key in the dictionary
print(pair[3.14])
# OutPut:-40

# use the in keyword to check if a key appears in the dictionary and print the result
print(3.14 in pair)
# OutPut:- True

print("Mars" in pair)
# OutPut:- False

# use not in to check if a key does not appear in the dictionary and print the result
print("Mars" not in pair)
# OutPut:- True

print("terraform" not in pair)
# OutPut:- False


