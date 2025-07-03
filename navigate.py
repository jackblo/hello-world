fileName = input("Enter the filename: ")

file = open(fileName, "r")
lines = file.readlines()
file.close()

while True:
    print("The file has", len(lines), "lines.")
    lineNumber = int(input("Enter a line number (0 to quit): "))
    if lineNumber == 0:
        break
    if 1 <= lineNumber <= len(lines):
        print(lines[lineNumber - 1].strip())
    else:
        print("Invalid line number.")
