numbers = [1, 3, 4, 5, 6, 78, 79, 4, 3]

# print consecutive numbers
for i in range(len(numbers)-1):
    if numbers[i] + 1 == numbers[i+1]:
        print(numbers[i], numbers[i+1])