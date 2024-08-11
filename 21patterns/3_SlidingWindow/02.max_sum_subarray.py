"""
Maximum Sum Subarray of Size K

Problem Statement:
Given an array of integers and a number k, find the maximum sum of a subarray of size k.

Example:

# Array: [2, 1, 5, 1, 3, 2], k = 3
# Expected Output: 9 (subarray [5, 1, 3] has the maximum sum)
"""

def max_sum_subarray(arr, k):
    max_sum, window_sum = 0, 0 
    
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i - (k-1)]  # subract the element going out fo the window
    
    return max_sum


arr = [1,5,4,2,9,9,9, 8]
k = 3
print(max_sum_subarray(arr, k))  # Output: 9
