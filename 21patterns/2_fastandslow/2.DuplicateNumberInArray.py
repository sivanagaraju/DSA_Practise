from collections import Counter

def find_duplicate(nums):
    slow, fast = nums[0], nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

def find_duplicates_python(nums):
    count = Counter(nums)
    
    