
# Elshaddai | Lab 4 | Intro to Python |



# Ticket 1

ages = [17, 11, 25, 13, 9]

for age in ages:
    if age >= 13:  
        print(f"{age} - Access granted")
    else:
        print(f"{age} - Too young")
# the ages that will get "Acess granted" are 17, 25, and 13. The ages that will get "Too young" are 11 and 9.
# the variable age acts as a placeholder



# Ticket 2

keep_checking = "yes"

while keep_checking == "yes":
    age = int(input("Enter an age: "))
    if age >= 13:
        print("Access granted")
    else: 
        print("Too young")
    keep_checking = input("Do you want to check another age? (yes/no):")
# the loop will not run at all
# It is better because you don't know how many times the user wants to repeat the process.



    # Ticket 3

while True:
    user_input = input("Enter an age or type 'stop': ")
    if user_input == "stop":
        break
    age = int(user_input)
    if age >= 13:
        print("Access granted")
    else:
        print("Too young")
# The loop will never stop and become an infinite loop
# It is different because it uses while True which needs a break to stop



    # Ticket 4
def can_access(age):
    return age >= 13
ages = [17, 11, 25, 13, 9]

for age in ages:
    if can_access(age):
        print(f"{age} - Access granted")
    else:
        print(f"{age} - Too young")
# It's different because it uses a defined function instead of if/else
# It better because you only have to write it once and then reuse it



    # Ticket 5
signups = [22, 10, 15, 8, 19, 13]

def signup_report(ages_list):
    print("...StreamPass Signup Report ...")
    approved = 0
    for i, age in enumerate(ages_list):
        signup_num = i + 1
        if can_access(age):
            print(f"Signup #{signup_num} | Ages {age} - Access granted")
            approved += 1
        else:
            print(f"Signup #{signup_num} | Ages {age} - Too young")
    print(f"Approved: {approved} out of {len(ages_list)}")
signup_report(signups)
# Signup #1 | Ages 22 - Access granted
# Signup #2 | Ages 10 - Too young
# Signup #3 | Ages 15 - Access granted
# Signup #4 | Ages 8 - Too young
# Signup #5 | Ages 19 - Access granted
# Signup #6 | Ages 13 - Access granted
# There will be 4 out of 6 approved
# I used lists, for loops, enumerate(), conditionals, and a counter variable.