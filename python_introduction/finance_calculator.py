# prompt for monthly income
monthly_income = int (input("enter your monthly income"))
# prompt for total monthly expenses
monthly_expenses = int(input("enter your total monthly expenses"))
# calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
#calculate projected savings
projected_savings = monthly_savings * 12 + (monthly_savings * 0.05)
#print results
print ("your monthly savings are $", monthly_savings)
print ("projected savings after one year,with interest,is", projected_savings)