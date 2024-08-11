def binary_serach(lst, n):
    low, high = 0, len(lst) - 1
    # low, high = min(lst), max(lst) # could be [o, 1], [1, n] etc, depends on pbrlm
    
    while low < high:
        mid = (low + high) // 2
        mid_value = lst[mid]
        
        if mid_value == n:
            return mid
        elif mid_value < n:
            low = mid + 1
        else:
            high = mid
    return -1

"""
278. First Bad Version [Easy]
You are a product manager and currently leading a team to develop a new product. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad. You are given an API bool isBadVersion(version) which will return whether version is bad.
Example:
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

"""

def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        mid = left + (right - left) / 2
        if isBadVersion(mid):
            right =  mid
        else:
            left = mid + 1
    return left

"""
Implement int sqrt(int x). Compute and return the square root of x, where x is guaranteed to be a non-negative integer. Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
Example:
Input: 4
Output: 2
 Input: 8
Output: 2

"""

def findsrqt(n):
    left, right = 0, n + 1
    while left < right:
        mid = left + (right - left) // 2
        if mid * mid > n:
            right = mid
        else:
            left = mid + 1
    return left - 1

print(findsrqt(8))

"""
35. Search Insert Position [Easy]
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array.
Example:
Input: [1,3,5,6], 5
Output: 2
 Input: [1,3,5,6], 2
Output: 1

"""

def searchInsert(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else: 
            left = mid + 1
    return left

"""
1011. Capacity To Ship Packages Within D Days [Medium]
A conveyor belt has packages that must be shipped from one port to another within D days. The i-th package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.
Example :
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
"""

def shipWithinDays(weights, days):
    def capacity_chk(mid):
        day = 1
        total = 0 
        for weight in weights:
            total += weight
            if total > mid:
                total = weight
                day += 1
                if day > days:
                    return False
        return True
    
    left, right = max(weights), sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        if capacity_chk(mid):
            right = mid
        else:
            left = mid + 1
    return left


"""
410. Split Array Largest Sum [Hard]
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.
Example:
Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays. The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
 
"""

def splitArray(self, nums, k):
    pass
    
    

# lst = [1, 3, 7, 11, 15, 17, 41, 47, 78]
# print(binary_serach(lst, 17))



