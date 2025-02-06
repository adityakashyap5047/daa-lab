numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Enter the number: "))

# insert at mid 
mid_index = len(numbers) // 2
numbers.append(0) 

for i in range(len(numbers) - 1, mid_index, -1):
    numbers[i] = numbers[i - 1]

# Insert the number at the middle index
numbers[mid_index] = number

print(numbers)