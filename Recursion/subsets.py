"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

class Solution(object):
    def subsets(self, nums):
        ret = []
        self.dfs(nums, [], ret)
        return ret
    
    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], ret)
       
    # Bit Manipulation    
    def subsets2(self, nums):
        res = []
        nums.sort()
        for i in xrange(1<<len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
		
    # Iteratively
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res
    
def generate_subsets1(nums):
    def backtrack(start, path):
        # Append the current subset (path) to the result
        res.append(path[:])
        for i in range(start, len(nums)):
            # Include the number nums[i] in the current subset
            path.append(nums[i])
            # Move to the next element
            backtrack(i + 1, path)
            # Exclude the number nums[i] from the current subset
            path.pop()
    
    res = []
    backtrack(0, [])
    return res

def generate_subsets(nums):
    def backtrack(index, path):
        # If the end of the array is reached, add the current subset to the result
        if index == len(nums):
            res.append(path[:])
            return
        # Take the current element
        path.append(nums[index])
        backtrack(index + 1, path)
        # Not take the current element
        path.pop()
        backtrack(index + 1, path)
    
    res = []
    backtrack(0, [])
    return res

# print(generate_subsets1(nums))

def print_subsequences_sum_n(nums, N):
    def backtrack(index, path, current_sum):
        if current_sum == N:
            print(path)
            return
        if index == len(nums) or current_sum > N:
            return
        
        # Take the current element
        backtrack(index + 1, path + [nums[index]], current_sum + nums[index])
        # Not take the current element
        backtrack(index + 1, path, current_sum)

    backtrack(0, [], 0)


def print_any_subsequence_sum_n(nums, N):
    def backtrack(index, path, current_sum):
        if current_sum == N:
            print(path)
            return True
        if index == len(nums) or current_sum > N:
            return False
        
        # Take the current element
        if backtrack(index + 1, path + [nums[index]], current_sum + nums[index]):
            return True
        # Not take the current element
        return backtrack(index + 1, path, current_sum)

    if not backtrack(0, [], 0):
        print("No subsequence found with sum", N)
        
def count_subsequences_sum_n(nums, N):
    def backtrack(index, current_sum):
        if current_sum == N:
            return 1
        if index == len(nums) or current_sum > N:
            return 0
        
        # Take the current element
        count_take = backtrack(index + 1, current_sum + nums[index])
        # Not take the current element
        count_not_take = backtrack(index + 1, current_sum)

        return count_take + count_not_take

    return backtrack(0, 0)

"""
Combination Sum
Problem: Given an array of distinct integers and a target sum, find all combinations of numbers in the array that sum up to the target. The same number may be chosen from the array multiple time
"""
def combination_sum(candidates, target):
    def backtrack(start, path, current_sum):
        if current_sum == target:
            print(path)
            # print(start, current_sum)
            return
        if start == len(candidates) or current_sum > target:
            return

        # Take the current element
        path.append(candidates[start])
        backtrack(start, path, current_sum + candidates[start])

        # Not take the current element
        path.pop()
        backtrack(start + 1, path, current_sum)

    # result = []
    backtrack(0, [], 0)
    # return result

# Example Usage
print(combination_sum([2, 3, 6, 7], 7))


# Example Usage
# nums = [1, 2, 3]
# print(generate_subsets(nums))
# Example Usage
# nums = [1, 2, 3, 4]
# N = 5
# print_subsequences_sum_n(nums, N)
#
## Example Usage
#nums = [1, 2, 3, 4]
#N = 5
#print_any_subsequence_sum_n(nums, N)
#
## Example Usage
#nums = [1, 2, 3, 4]
#N = 5
#print(count_subsequences_sum_n(nums, N))
