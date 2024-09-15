current_year = 2023
target_year = 2050
# prompt the user for their current age
current_age = int (input("How old are you?") )
# calculate age in current year 
age_in_2050 = current_age + (target_year - current_year)
# print the result with the formatted string
print(f"In {target_year}, you will be {age_in_2050} years old.")