# binary search using recursion
# Time complexity: O(logn)
# Space complexity: O(logn)

def binary_search(arr, low, high, x):
    if low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
    
arr = [1, 3, 4, 5, 6, 78, 79, 4, 3]
arr.sort()

print(binary_search(arr, 0, len(arr)-1, 78))
print(binary_search(arr, 0, len(arr)-1, 100))
print(binary_search(arr, 0, len(arr)-1, 1))
print(binary_search(arr, 0, len(arr)-1, 3))
print(binary_search(arr, 0, len(arr)-1, 79))