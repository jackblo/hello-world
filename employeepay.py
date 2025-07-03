hourlyWage = float(input("Enter rthe hourly wage: "))
regularHours = float(input("Enter total regular hours worked: "))
overtimeHours = float(input("Enter total overtime hours worked: "))
regularPay = hourlyWage * regularHours 
overtimePay = overtimeHours * (1.5 * hourlyWage)
totalPay = regularPay + overtimePay
print(f"The employee's total weekly pay is : ${totalPay: .2f}")
