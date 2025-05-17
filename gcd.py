import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD:", math.gcd(a, b))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = abs(a * b) // gcd(a, b)
print("LCM:", lcm)