def mean(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if len(numbers) == 0:
        return 0
    sortedNumbers = sorted(numbers)
    n = len(sortedNumbers)
    middle = n // 2
    if n % 2 == 0:
        return (sortedNumbers[middle - 1] + sortedNumbers[middle]) / 2
    else:
        return sortedNumbers[middle]

def mode(numbers):
    if len(numbers) == 0:
        return 0
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    maxCount = max(frequency.values())
    modes = [key for key in frequency if frequency[key] == maxCount]
    if len(modes) == 1:
        return modes[0]
    return modes[0]

def main():
    sampleData = [4, 1, 2, 2, 3, 5, 4]
    print("Mean:", mean(sampleData))
    print("Median:", median(sampleData))
    print("Mode:", mode(sampleData))

main()
