numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Enter the number: "))

# insert at mid
mid_index = len(numbers) // 2
numbers.insert(mid_index, number)

print(numbers)
