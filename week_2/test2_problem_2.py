"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out
the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135
So your program only prints out one thing: the remaining balance at the end of the year in the format:

Remaining balance: 4784.0
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""
# commentting out the debug statements and the folling variables balance, annulaInterestRate, and monthlyPaymentRate
new_balance = 0
balance = 484
new_balance = balance
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthly_interest_rate = annualInterestRate / 12
minimum_monthly_payment = monthlyPaymentRate * new_balance
monthly_unpaid_balance = new_balance - minimum_monthly_payment
update_balance_each_month = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
month = 0


while month < 11:
    # debugging below
    # print('balance:  {}'.format(balance))
    # print('new_balance: {}'.format(new_balance))
    # print('annualInterestRate: {} '.format(annualInterestRate))
    # print('monthly_interest_rate: {}'.format(monthly_interest_rate))
    # print('minimum_monthly_payment: {}'.format(minimum_monthly_payment))
    # print('monthly_unpaid_balance: {}'.format(monthly_unpaid_balance))
    # print('update_balance_each_month: {}'.format(update_balance_each_month))
    # print('month: {}'.format(month))

    # adding to the loop to be updated each time it runs
    minimum_monthly_payment = monthlyPaymentRate * new_balance
    monthly_unpaid_balance = new_balance - minimum_monthly_payment

    new_balance = update_balance_each_month
    # print('new_balance: {}'.format(new_balance))
    # new_balance = balance
    balance = new_balance
    # print('balance for next month: {}'.format(balance))
    month += 1

    # print('Month {} Remaining balance: {}'.format(month + 1, round(update_balance_each_month, 2)))

    # adding to the loop to be updated each time it runs
    minimum_monthly_payment = monthlyPaymentRate * new_balance
    monthly_unpaid_balance = new_balance - minimum_monthly_payment
    update_balance_each_month = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
    # print()
print('Month {} Remaining balance: {}'.format(month + 1, round(update_balance_each_month, 2)))
