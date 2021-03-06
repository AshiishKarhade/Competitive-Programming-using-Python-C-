""""
Problem Statement
You are given a non-negative number in the form of list elements. For example, the number `123` would be provided as `arr = [1, 2, 3]`. Add one to the number and return the output in the form of a new list. 

Example 1:
`input = [1, 2, 3]`
`output = [1, 2, 4]`

Example 2:
`input = [1, 2, 9]`
`output = [1, 3, 0]`

Example 3:
`input = [9, 9, 9]`
`output = [1, 0, 0, 0]`
"""

def add_one(array):
    # base case
    if array == [9]:
        return [1,0]
    
    # recursive case
    if array[-1] < 9:
        array[-1] += 1
    else:
        array = add_one(array[:-1]) + [0]
    return array


print(add_one([9,9,9]))


