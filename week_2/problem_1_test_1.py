balance = 132
annualInterestRate = 0.22
# monthlyPaymentRate = 0.06

new_balance = 0
new_balance = balance
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
    # minimum_monthly_payment = monthlyPaymentRate * new_balance
    # monthly_unpaid_balance = new_balance - minimum_monthly_payment

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
print('Remaining balance: {}'.format(round(update_balance_each_month, 2)))
