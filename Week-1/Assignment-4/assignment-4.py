def binary_search_position(numbers, target):
    low = 0
    high = len(numbers)

    while (low < high):
        mid = (low + high) // 2
        guessNumber = numbers[mid]
        if guessNumber == target:
            return mid
        elif guessNumber < target:
            low = mid + 1
        elif guessNumber > target:
            high = mid

    return -1


# your code here
print(binary_search_position([1, 2, 5, 6, 7], 1))  # should print 0
print(binary_search_position([1, 2, 5, 6, 7], 6))  # should print 3
