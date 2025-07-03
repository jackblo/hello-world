# population.py

initial_population = int(input("Enter the initial number of organisms: "))
growth_rate = float(input("Enter the rate of growth: "))
growth_period = int(input("Enter the number of hours to achieve this rate: "))
total_hours = int(input("Enter the total number of hours for growth: "))

periods = total_hours // growth_period
population = initial_population

for _ in range(periods):
    population *= growth_rate

print("Predicted population after", total_hours, "hours:", int(population))
