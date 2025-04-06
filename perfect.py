def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

num = int(input("Enter a number: "))
print("Perfect Number:", is_perfect(num))