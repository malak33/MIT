balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12
originalBalance = balance