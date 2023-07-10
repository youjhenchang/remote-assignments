# 有重複，但只回傳第一個的Index
# 找不到target，找比target大的最小值
# 找不到比target大的回傳-1

# 讓while loop 找 the largest number(with biggest index) below target number，之後index再加1即為所求。
# [1, 2, 5, 5, 5, 6, 7], 6)= 4
# [1, 2, 3, 4, 4, 5, 7], 4)= 2
# [1, 2, 3, 4, 4, 5, 7], 10)= 6

def binary_search_first(numbers, target):
    # [low,high)
    low = 0
    high = len(numbers)

    # 讓while迴圈跑出來後，定義域只剩下一個值(一路篩選下去)
    # 只要證明定義域在low < high-1的條件下會持續shrink，則while loop必結束。
    while (low < high-1):
        # 取mid
        mid = (high + low) // 2
        # 跟target比大小
        guessNumber = numbers[mid]
        if guessNumber < target:
            low = mid
        if guessNumber >= target:
            high = mid
    # 回傳前判斷return 的index是否會超出numbers array長度
    # 超出則代表未找到符合項，回傳-1
    if low+1 >= len(numbers):
        return -1
    else:
        return low+1


# should print 1 (the index of the target number ‘2’)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2))
# should print 2 (the index of the ‘first’ target number ‘5’ shows up)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5))
# should print 2 (since it can’t find number 3,return the index of ‘the smallest number larger than 3', that is, the index of the ‘first’ number 5)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3))
# should print -1
print(binary_search_first([1, 2, 3, 4, 4, 5, 7], 10))
