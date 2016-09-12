"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance
within 12 months. By a fixed monthly payment, we mean a single number which does not change each month,
but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year,
for example:

Lowest Payment: 180
Assume that the interest is compounded monthly according to the balance at the end of the month
 (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all
 months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay.
 A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""
import math

new_balance = 0
minimum_fixed_monthly_payment = 0
balance = 3229
new_balance = balance
annualInterestRate = 0.2
monthly_interest_rate = annualInterestRate / 12
monthly_unpaid_balance = new_balance - minimum_fixed_monthly_payment
updated_balance_each_month = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
month = 0
lowest_payment = 0

while month < 11:
    # debugging below
    print('balance:  {}'.format(balance))
    print('new_balance: {}'.format(new_balance))
    print('monthly_interest_rate: {}'.format(monthly_interest_rate))
    print('update_balance_each_month: {}'.format(updated_balance_each_month))
    print('month: {}'.format(month + 1))

    new_balance = updated_balance_each_month
    balance = new_balance

    print('month: {}'.format(month + 1))

    month += 1
    print('balance for next month: {}'.format(balance))
    # adding to the loop to be updated each time it runs
    monthly_interest_rate = annualInterestRate / 12
    monthly_unpaid_balance = new_balance - minimum_fixed_monthly_payment
    updated_balance_each_month = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
    lowest_payment = math.ceil(updated_balance_each_month / 12)
    print('Lowest Payment: {}'.format(lowest_payment))
    print()
print('Lowest Payment: {}'.format(lowest_payment))
print()

