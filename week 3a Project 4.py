# bouncy.py

initial_height = float(input("Enter the initial height (in feet): "))
bounces = int(input("Enter the number of bounces: "))

bounciness_index = float(input("Enter the bounciness index (e.g., 0.6): "))

total_distance = initial_height
height = initial_height * bounciness_index

for _ in range(bounces):
    total_distance += 2 * height
    height *= bounciness_index

print("Total distance traveled by the ball:", total_distance, "feet")
