"""
Given a sorted array, remove the duplicates in-place such that each element appears only once and return the new length. Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

Example:

nums = [1, 1, 2, 2, 3, 4, 4, 5]
Output:
The array after removing duplicates: [1, 2, 3, 4, 5]
"""

def remove_duplicates(nums):
    if not nums:
        return 0

    write_index = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1

    return write_index

# Example usage
nums = [1, 1, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(nums)
print(f"Array after removing duplicates: {nums[:new_length]}")
