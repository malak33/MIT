balance = 42
annualInterestRate = 0.2
# balance = 320000
# annualInterestRate = 0.2

originalBalance = balance
month = 1
monthly_interest = annualInterestRate / 12
low = originalBalance/12
high = (originalBalance*(1 + monthly_interest)**12)/12
epsilon = 0.01
min_payment = (high + low)/2.0

while min_payment*12 - originalBalance > epsilon:
    month = 1          # < -- do this
    while month < 13:
        balance = (originalBalance - min_payment)/10 * (1 + monthly_interest)
        if balance < 0.00:
            low = min_payment
            min_payment = (high + low)/2.0
        elif balance > 0.00:
            high = min_payment
            min_payment = (high + low)/2.0
        month += 1
#print "Lowest payment: " + str(round(min_payment, 2))
print(" Lowest Payment:", min_payment)
#print('Lowest Payment: '.format(round(mmp, 2)))
