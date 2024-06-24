# Ask to user for input gpa
gpa = float(input("What was the applicant's gpa ?"))

# Ask for input as yes or no for Accepted by approved institutions ?
institute = input("Is the student going to be educated at an approved instsitutions ?")

# write if statement for check gpa >= 3.7
if gpa >= 3.7:
    
    # If gpa >= 3.7 then, check approved institute is qualified or not by yes or no.
    # If Institute is qualified mean yes,    
    if institute == "yes":
        print("The applicant qualifies for a low APR student Loan.")
        
        # If institute not qualified means no.
    else:
        print("THe applicant doesn't qualify so, they aren't accepted into an approved institutions.")
        
# If gpa is not >= 3.7 or < 3.7 gpa then , print "Applicant did not have enough gpa to qualify."
else:
    print("The applicant did not have enough gpa to qualify")
