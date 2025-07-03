income = float(input("Enter your taxable income : "))
taxRate = float(input("Enter the tax rate (as a percentage): "))
taxRateDecimal = taxRate / 100
tax = income * taxRateDecimal 
tax = round(tax, 2)
print(f"The tax owed is: ${tax: .2f}")