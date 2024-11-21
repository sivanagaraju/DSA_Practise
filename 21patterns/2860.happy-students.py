#
# @lc app=leetcode id=2860 lang=python3
#
# [2860] Happy Students
#

# @lc code=start
class Solution:
    def countWays(self, nums: List[int]) -> int:
        from bisect import bisect_left, bisect_right

        n = len(nums)
        nums_sorted = sorted(nums)
        count = 0

        for k in range(0, n + 1):
            # Number of students with nums[i] < k
            count_less = bisect_left(nums_sorted, k)
            
            # Number of students with nums[i] == k
            count_eq = bisect_right(nums_sorted, k) - count_less
            
            # Check the two conditions
            if count_less == k and count_eq == 0:
                count += 1

        return count
            
# @lc code=end

