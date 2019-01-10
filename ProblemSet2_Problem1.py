balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
for i in range(1,13):
    minimumMonthlyPayment = balance * monthlyPaymentRate
    balance = (balance - minimumMonthlyPayment) * (1+annualInterestRate/12)

print("Remaining balance:", round(balance, 2))
    
    
