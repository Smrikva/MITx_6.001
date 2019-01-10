balance = 320000
annualInterestRate = 0.2






monthlyInterestRate = annualInterestRate / 12.0
minimumFixedMonthlyPayment = balance//12 // 10 * 10 - 10
oldBalance = balance
while True: 
    balance = oldBalance
    for i in range(12):
        balance = (balance - minimumFixedMonthlyPayment) * (1 + monthlyInterestRate)
    if balance <= 0:
        print("Lowest Payment:", minimumFixedMonthlyPayment)
        break
    else:
        minimumFixedMonthlyPayment += 10

