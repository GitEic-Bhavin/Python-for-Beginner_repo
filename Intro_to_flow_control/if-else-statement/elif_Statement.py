# elif Statement

# This is used when you want to do multiple outcomes.

# Use elif instead of else:
#                         if “condition”:

user_num = int(input("Plz, enter an integer"))

if user_num < 0:
    print("The number you entered is less then 0.")

elif user_num == 0:
    print("The number you enterd is equal to 0.")

elif 0 < user_num <= 100:
    print("The number you entered is between 0 to 100")

else:
    print("The number you entered is greater then 100")

# Plz, enter an integer-4
# The number you entered is less then 0.

# Plz, enter an integer-1
# The number you entered is less then 0.

# Plz, enter an integer0
# The number you enterd is equal to 0.

# Plz, enter an integer1
# The number you entered is between 0 to 100

# Plz, enter an integer110
# The number you entered is greater then 100