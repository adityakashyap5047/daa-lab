# Write a program for bubble sort for the given list of numbers

li = [20, 40, 8, 18, 38, 17]

for i in range(len(li)):
    for j in range(i+1, len(li)):
        if(li[i] > li[j]):
            li[i], li[j] = li[j], li[i]
        
print(li)