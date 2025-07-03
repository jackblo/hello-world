import string

characters = string.printable
charCount = len(characters)

plainText = input("Enter the text to encrypt: ")
distance = int(input("Enter the distance value: "))

cipherText = ""

for ch in plainText:
    index = characters.find(ch)
    newIndex = (index + distance) % charCount
    cipherText += characters[newIndex]

print("Encrypted text:", cipherText)
