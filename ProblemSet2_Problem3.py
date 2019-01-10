balance = 320000
annualInterestRate = 0.2






monthlyInterestRate = annualInterestRate / 12.0
minimumFixedMonthlyPaymentBound = balance/12.0
maximumFixedMonthlyPaymentBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
oldBalance = balance
minimumFixedMonthlyPayment = 0.015
while balance >= 0.01 or balance <= -0.01: 
    balance = oldBalance
    minimumFixedMonthlyPayment = (minimumFixedMonthlyPaymentBound + maximumFixedMonthlyPaymentBound) / 2
    for i in range(12):
        balance = (balance - minimumFixedMonthlyPayment) * (1 + monthlyInterestRate)
    if balance < 0:
        maximumFixedMonthlyPaymentBound = minimumFixedMonthlyPayment      
    else:
        minimumFixedMonthlyPaymentBound = minimumFixedMonthlyPayment


print("Lowest Payment:", round(minimumFixedMonthlyPayment, 2))

