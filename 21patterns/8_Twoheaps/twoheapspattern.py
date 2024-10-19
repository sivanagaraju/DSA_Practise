#Two Heap Pattern Template#
# Python
import heapq

def two_heap_pattern(nums):
    # Initialize two empty heaps, a max heap (left) and a min heap (right)
    left = []  # max heap
    right = []  # min heap

    for num in nums:
        # Add number to the correct heap
        if not left or num < -left[0]:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)

        # Balance the heaps
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))

    # Return the result (e.g., median, or process the heaps)
    # For median, use the following:
    if len(left) == len(right):
        return (-left[0] + right[0]) / 2
    else:
        return -left[0]

"""
# Example usage:
numbers = [1, 2, 3, 4, 5]
print(two_heap_pattern(numbers))  # Output: 3
Pattern Explanation:
Initialize two empty heaps, left (max heap) and right (min heap).
Iterate through the input numbers.
Add each number to the correct heap based on the comparison with the top of left.
Balance the heaps to maintain the property.
Return the result, such as the median, or process the heaps further.
This template can be adapted to various problems that involve finding the median or balancing two sets of numbers.
"""


"""
Two Heap Pattern Coding Interview Questions

Find the Median of a Stream of Numbers
Logic Change: Maintain the balance between the two heaps to ensure the median can be calculated efficiently.
Question: Design a data structure that can efficiently calculate the median of a stream of numbers.
Example: [1, 2, 3, 4, 5] → Median: 3


Kth Largest Element in a Stream
Logic Change: Use a single max heap to keep track of the kth largest element.
Question: Design a data structure that can efficiently find the kth largest element in a stream of numbers.
Example: [1, 2, 3, 4, 5], k = 2 → Kth Largest: 4

Kth Smallest Element in a Stream
Logic Change: Use a single min heap to keep track of the kth smallest element.
Question: Design a data structure that can efficiently find the kth smallest element in a stream of numbers.
Example: [1, 2, 3, 4, 5], k = 2 → Kth Smallest: 2

Maximum of Minimums for Every Window of Size K
Logic Change: Use a deque to store indices and a max heap to store the maximum of minimums.
Question: Given an array and a window size k, find the maximum of minimums for every window of size k.
Example: [1, 2, 3, 4, 5], k = 3 → Maximum of Minimums: [2, 3, 4]

Sliding Window Median
Logic Change: Use two heaps to maintain the balance and calculate the median for every window.
Question: Given an array and a window size k, find the median for every window of size k.
Example: [1, 2, 3, 4, 5], k = 3 → Medians: [2, 3, 4]

Common Logic Changes:
Balancing the heaps to maintain the property.
Using a single heap to keep track of the kth largest or smallest element.
Utilizing a deque to store indices and a heap to store the maximum of minimums.

Tips:
Understand the problem requirements and adjust the logic accordingly.
Practice implementing the two heap pattern to become proficient.
Be prepared to explain the logic and time complexity during the interview.
"""