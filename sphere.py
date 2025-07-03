import math
radius = float(input("Enter the radius of the sphere: "))
diameter = 2 * radius
circumference = 2 * math.pi * radius
surfaceArea = 4 * math.pi * radius ** 2
volume = (4/3) * math.pi * radius ** 3 
print(f"Diameter: {diameter: .2f}")
print(f"Circumference: {circumference: .2f}")
print(f"Surface Area: {surfaceArea: .2f}")
print(f"Volume: {volume: .2f}")