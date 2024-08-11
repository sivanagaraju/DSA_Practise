"""
Problem Statement:
Given an array of sorted numbers and a target sum, find a pair in the array whose sum equals the given target. Return the indices of the two numbers (0-based index).

arr = [1, 2, 3, 4, 6]
target_sum = 6
"""
def pair_with_target_sum(arr, target_sum):
    left = 0 
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]
        elif current_sum < target_sum:
            left+=1
        else:
            right-=1
    return [-1, -1]

arr = [1, 2, 3, 4, 5]
target_sum = 6
result = pair_with_target_sum(arr, target_sum)
print(result)
    