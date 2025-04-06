def second_largest(arr):
    unique_numbers = list(set(arr))
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) > 1 else None

arr = [10, 20, 4, 45, 99, 45]
print("Second Largest:", second_largest(arr))