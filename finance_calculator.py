#promt the user to input their monthly income
monthly_income = int (input("enter your monthly income"))
#promt the user for their total monthly expenses
monthly_expenses = int(input("enter your total monthly expenses"))
#calculate users savings
monthly_savings = monthly_income - monthly_expenses
# calculating projected savings for one year
projected_savings = monthly_savings * 12 + monthly_savings * 0.05
# displaying the result
print ("your monthly savings are $", monthly_savings)
print ("projected savings after one year, with intrest, is :", projected_savings)
