# string methods 2 exercises

# Do all of this in a .py file:

# Create a variable called the_string and assign it the string "North Dakota".
the_string = "North Dakota"
# OutPut:-
#     North Dakota

# Call .rjust() on the_string with 17 as its argument and print() the result.
print(the_string.rjust(17)) 
# OutPut:-
#North Dakota

# Call .ljust() on the_string with the arguments 17 and "*" then print() the result.
print(the_string.ljust(17,"*"))
# OutPut:-
#North Dakota*****

# Create a variable called center_plus and assign it the result of .center() being called on the_string with 16 and "+" as arguments.
# center_plus = (the_string.center(16, "+"))
# print(center_plus)
# OutPut:-
#++North Dakota++
center_plus = (the_string.center(16, "+"))
print(center_plus)


# Use print() to display the string assigned to center_plus.

# Call .lstrip() on the_string to remove "North" then print() the result.
print(center_plus.lstrip("North"))
# OutPut:-
#++North Dakota++

# Call .rstrip() on center_plus with "+" as its argument and print() the result.
print(center_plus.rstrip("+"))
# OutPut:-
#++North Dakota

# Call .strip() on center_plus with "+" as its argument and print() the result.
print(center_plus.strip("+"))
# OutPut:-
#North Dakota

# Call .replace() on the_string and replace "North" with "South".  print() the result.
print(center_plus.replace("North", "South"))
# OutPut:-
#++South Dakota++




  












