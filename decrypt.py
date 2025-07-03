import string

characters = string.printable
charCount = len(characters)

cipherText = input("Enter the text to decrypt: ")
distance = int(input("Enter the distance value: "))

plainText = ""

for ch in cipherText:
    index = characters.find(ch)
    newIndex = (index - distance) % charCount
    plainText += characters[newIndex]

print("Decrypted text:", plainText)
