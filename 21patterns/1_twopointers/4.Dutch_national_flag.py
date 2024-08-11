"""
Dutch National Flag Problem:
Given an array containing only 0s, 1s, and 2s, sort the array in-place. 
You should treat the array as if it contains three distinct colors.

Example:
nums = [2, 0, 2, 1, 1, 0]

Expected Output: [0, 0, 1, 1, 2, 2]

"""

def dutch_national_flag(nums):
    # as the requirment is  3 we used te low, mid and high in place of left and right
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else: 
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
            
    return nums

nums = [2, 0, 2, 1, 1, 0]
sorted_nums = dutch_national_flag(nums)
print("Sorted array:", sorted_nums)
    
    