### Finding the maximum and minimum values in a list

def find_max_min(numbers):
    if not numbers:
        return None, None

    max_value = numbers[0]
    min_value = numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number

    return max_value, min_value

if __name__ == "__main__":
    numbers = [3, 5, 1, 8, 2, 7, 4, 6]
    max_value, min_value = find_max_min(numbers)
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")