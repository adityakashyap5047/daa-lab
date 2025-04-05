### Binary Search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
            
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    arr = [1, 3, 4, 5, 6, 78, 79, 4, 3]
    arr.sort() 

    # Test cases
    print(binary_search(arr, 78))  
    print(binary_search(arr, 100)) 
    print(binary_search(arr, 1))   
    print(binary_search(arr, 3))  
    print(binary_search(arr, 79)) 