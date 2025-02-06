numbers = [1, 2, 3, 4, 5, 6]

#reverse an array
for i in range(len(numbers)//2):
    #Swap of 2 numbers without third variable using arithmetic operation
    numbers[i] = numbers[i] + numbers[len(numbers)-i-1]
    numbers[len(numbers)-i-1] = numbers[i] - numbers[len(numbers)-i-1]
    numbers[i] = numbers[i] - numbers[len(numbers)-i-1]

    #Swap of 2 numbers without third variable using XOR ( ^ )
    # numbers[i] = numbers[i] ^ numbers[len(numbers)-i-1]
    # numbers[len(numbers)-i-1] = numbers[i] ^ numbers[len(numbers)-i-1]
    # numbers[i] = numbers[i] ^ numbers[len(numbers)-i-1]

print(numbers)