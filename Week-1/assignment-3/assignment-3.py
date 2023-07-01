def find_max(numbers):
    if len(numbers) == 0:
        raise ValueError("list is empty")
    else:
        max = numbers[0]
        for i in numbers:
            if i > max:
                max = i
        return max


def find_position(numbers, target):
    if target not in numbers:
        return -1
    else:
        for i in range(len(numbers)):
            if numbers[i] == target:
                return i


print(find_max([1, 2, 4, 5]))  # should print 5
print(find_max([5, 2, 7, 1, 6]))  # should print 7
print(find_position([5, 2, 7, 1, 6], 5))  # should print 0
print(find_position([5, 2, 7, 1, 6], 7))  # should print 2
# should print 2 (the first one)
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))
print(find_position([5, 2, 7, 1, 6], 8))  # should print -1
