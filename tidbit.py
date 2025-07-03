def main():
    purchasePrice = float(input("Enter the purchase price: "))
    downPayment = 0.10 * purchasePrice
    loanBalance = purchasePrice - downPayment
    monthlyPayment = 0.05 * purchasePrice
    monthlyRate = 0.12 / 12

    print("Month")
    print("Balance")
    print("Interest")
    print("Principal")
    print("Payment")
    print("Remaining")
    print("------")

    month = 1
    while loanBalance > 0:
        interest = loanBalance * monthlyRate
        principal = monthlyPayment - interest

        if principal > loanBalance:
            principal = loanBalance
            monthlyPayment = interest + principal

        remainingBalance = loanBalance - principal

        print("Month: " + str(month))
        print("Balance: " + str(round(loanBalance, 2)))
        print("Interest: " + str(round(interest, 2)))
        print("Principal: " + str(round(principal, 2)))
        print("Payment: " + str(round(monthlyPayment, 2)))
        print("Remaining: " + str(round(remainingBalance, 2)))
        print("------")

        loanBalance = remainingBalance
        month = month + 1

main()
