inputFileName = input("Enter the name of the file to copy from: ")
outputFileName = input("Enter the name of the file to copy to: ")

inputFile = open(inputFileName, "r")
outputFile = open(outputFileName, "w")

contents = inputFile.read()
outputFile.write(contents)

inputFile.close()
outputFile.close()
