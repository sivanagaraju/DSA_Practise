"""
Triplet Sum Close to Target (medium)
Problem Statement
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: The triplet [-1, 0, 3] has the sum '2' which is closest to the target.

There are two triplets with distance '1' from the target: [-1, 0, 3] & [-1, 2, 3]. Between these two triplets, the correct answer will be [-1, 0, 3] as it has a sum '2' which is less than the sum of the other triplet which is '4'. This is because of the following requirement: 'If there are more than one such triplet, return the sum of the triplet with the smallest sum.'
Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
Example 4:

Input: [0, 0, 1, 1, 2, 6], target=5
Output: 4
Explanation: There are two triplets with distance '1' from target: [1, 1, 2] & [0, 0, 6]. Between these two triplets, the correct answer will be [1, 1, 2] as it has a sum '4' which is less than the sum of the other triplet which is '6'. This is because of the following requirement: 'If there are more than one such triplet, return the sum of the triplet with the smallest sum.'
Constraints:

3 <= arr.length <= 500
-1000 <= arr[i] <= 1000
-104 <= target <= 104

1. Sort the array
2. initialize a variable to track the closest sum found so far. 
3. Iterate through the array
4. Update the closest sum 


"""

def triplet_sum_close_to_target(nums, target):
    nums.sort()
    closest_sum = float('inf')
    
    # why len(nums) - 2 ?
    # two form a triplet we need three elements. To ensure that there are at least two more elements are 
    # avilable after the current element 'nums[i]' to form a triplet(nums[left], nums[right]). 
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            # sum calculation happens here
            current_sum = nums[i]  +  nums[left] + nums[right]
            
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
                
            if current_sum < target:
                left+=1
            elif current_sum > target:
                right -=1
            else:
                return current_sum
            
    return closest_sum


nums = [-2, 0, 1, 2]
target = 2
print("Closest sum to target:", triplet_sum_close_to_target(nums, target))  # Output: 1
        