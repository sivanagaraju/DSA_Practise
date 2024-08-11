"""
Triplets with Smaller Sum (medium)
Problem Statement
Given an array arr of unsorted numbers and a target sum, 
count all triplets in it such that arr[i] + arr[j] + arr[k] < target 
where i, j, and k are three different indices. Write a function to return 
the count of such triplets.

Example 1:

Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
Example 2:

Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
Constraints:

n == att.length
0 <= n <= 3500
-100 <= arr[i] <= 100
-100 <= target <= 100

1. sort the data
2. take the closest sum 
3. create left, right variables
4. calculate the sum using i. left, right 
"""

def tripelts_with_smaller_sum(nums, target):
    nums.sort()
    count = 0
    
    for i in range(len(nums) - 2):
        left = i + 1
        right =  len(nums) - 1
        # this one loop still left , right 
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < target:
                """
                When you find that the sum of nums[i] + nums[left] + nums[right] is 
                less than the target, it implies that any combination of nums[i], nums[left], 
                and any element between nums[left+1] and nums[right] will also be less than 
                the target. This is because the array is sorted, and increasing the value of 
                right (moving it left) will only decrease the sum further or keep it the same, 
                but never increase it beyond the current sum.
                """
                count += right - left 
                
                left += 1
            else:
                right -= 1
    return count

nums1 = [0, -1, 3, 2]
target = 2
print("count of triplets:", tripelts_with_smaller_sum(nums1, target))

        