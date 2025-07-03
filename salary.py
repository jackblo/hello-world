# salary.py
def main():
    print("Salary Schedule Calculator")

    startingSalary = float(input("Enter the starting salary: "))
    percentIncrease = float(input("Enter the percentage increase per year: "))
    years = int(input("Enter the number of years in the schedule: "))

    print("\nYear\tSalary")
    print("---------------")

    salary = startingSalary
    for year in range(1, years + 1):
        print(str(year) + "\t" + str(round(salary, 2)))
        salary = salary + (salary * percentIncrease / 100)

main()
