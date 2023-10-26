def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Create a sorted list of numbers
sorted_numbers = [1, 4, 7, 9, 12, 15, 18, 21, 25, 28]

# Ask the user for a number
user_number = int(input("Enter a number to predict: "))

# Use binary search to predict if the number is in the list
result = binary_search(sorted_numbers, user_number)

if result != -1:
    print(f"The number {user_number} is in the list at index {result}.")
else:
    print(f"The number {user_number} is not in the list.")
