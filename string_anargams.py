def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Anagrams:", are_anagrams(str1, str2))