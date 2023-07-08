# Complete the following functions by Python
# 1. count: return an object which shows the count of each character.
# 2. group_by_key: return an object which shows the summed up value of each key.
# Note:
# 1. The input format is different for these two functions.
# 2. In the second function, the input may have same key but different values, the output
# should have each key only once.

def count(input):
    char_frequency={}
    for char in input:
        if char not in char_frequency:
            char_frequency[char] = 1
        else:
            char_frequency[char]+=1
    return char_frequency

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}





def group_by_key(input):
    dict = {}
    for item in input2:
        if item['key'] in dict:
            dict[item['key']] += item['value']
        else:
            dict[item['key']] = item['value']
    return dict

input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}