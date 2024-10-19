**Two Heap Coding Pattern - A Comprehensive Guide**

## 1. Core Concepts and Coding Patterns

The **Two Heap pattern** is a commonly used approach for solving problems related to finding the **median** or **balancing priorities** dynamically within a dataset, especially when the data changes over time. It involves the use of two **heaps**:

- **Max-Heap**: Maintains the **lower half** of the numbers.
- **Min-Heap**: Maintains the **upper half** of the numbers.

The idea is to keep the two heaps balanced, with the **Max-Heap** containing elements smaller or equal to the median and the **Min-Heap** containing elements larger than the median. This enables efficient access to the **median** element in logarithmic time.

### Typical Use Cases

- **Finding the median** of a stream of numbers.
- **Balancing priorities**, such as in scheduling and load balancing.
- **Financial applications**, such as maintaining dynamic data for stock prices or calculating running medians for financial data streams.

## 2. What is a Heap?

A **heap** is a specialized binary tree-based data structure that satisfies the **heap property**. There are two main types of heaps:

- **Max-Heap**: In a max-heap, for any given node, the value of the node is greater than or equal to the values of its children. The largest element is always at the root.
- **Min-Heap**: In a min-heap, for any given node, the value of the node is less than or equal to the values of its children. The smallest element is always at the root.

Heaps are typically implemented using **arrays** rather than pointers. The root element is stored at index 0, and for any element at index **i**:

- The **left child** is at index **2i + 1**.
- The **right child** is at index **2i + 2**.
- The **parent** is at index **(i - 1) // 2**.

Heaps are most commonly used to implement **priority queues** due to their efficient insertion and extraction properties.

### Heap Operations

- **Insertion**: Adding an element to the heap while maintaining the heap property. This takes **O(log N)** time.
- **Deletion** (usually of the root): Removing the root element (max or min) while maintaining the heap property. This also takes **O(log N)** time.
- **Peek**: Retrieving the root element without removing it. This takes **O(1)** time.

## 3. Example

Consider the following sequence of numbers:

**Input**: [5, 2, 10, 1, 7, 6]

- **Step 1**: Insert 5 into the Max-Heap.
- **Step 2**: Insert 2 into the Max-Heap. Now, balance the heaps: Max-Heap = [2], Min-Heap = [5].

To better understand how the heaps change during each step, refer to the following diagram:

```
Step 1: Max-Heap = [5], Min-Heap = []
Step 2: Max-Heap = [2], Min-Heap = [5]
Step 3: Max-Heap = [2], Min-Heap = [5, 10]
Step 4: Max-Heap = [2, 1], Min-Heap = [5, 10]
Step 5: Max-Heap = [2, 1], Min-Heap = [5, 7, 10]
Step 6: Max-Heap = [2, 1], Min-Heap = [5, 6, 7, 10]
```

This visual representation illustrates how elements are moved between heaps to maintain balance.

- **Step 3**: Insert 10 into the Min-Heap.
- **Step 4**: Insert 1 into the Max-Heap, then balance: Max-Heap = [2, 1], Min-Heap = [5, 10].
- **Step 5**: Insert 7 into the Min-Heap, then balance.
- **Step 6**: Insert 6 into the Min-Heap, balance accordingly.

After balancing, the median is always efficiently available by looking at the roots of the heaps.

## 4. Problem Identification Checklist

| Criteria                  | Example Problem                                                 |
| ------------------------- | --------------------------------------------------------------- |
| **Continuous Median**     | Find the median of a continuously growing list of numbers.      |
| **Priority Balancing**    | Dynamically manage a workload in two parts (high/low priority). |
| **Balanced Partitioning** | Divide elements such that their sum is balanced.                |

## 5. General Templates with Comments

### Template 1: Finding the Median of a Stream of Numbers

```python
import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap for the lower half
        self.max_heap = []
        # Min-heap for the upper half
        self.min_heap = []

    def add_num(self, num: int) -> None:
        # Add to max-heap (Python has only min-heap, so insert negative for max-heap)
        heapq.heappush(self.max_heap, -num)

        # Balance the heaps
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Ensure max-heap has more elements or equal to min-heap
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
```

**Use Cases**: Best used for problems that require real-time median calculation, such as sensor data analysis.

**Time Complexity**: Each add operation takes **O(log N)**, and finding the median takes **O(1)**.

**Space Complexity**: **O(N)**, where **N** is the number of elements.

## 6. Complexity Analysis

- **Time Complexity**: Insertions and deletions from the heap take **O(log N)** time.
- **Space Complexity**: Maintaining the heaps takes **O(N)** space.
- **Optimization Opportunities**: The balancing of heaps could be optimized by performing fewer comparisons based on the sequence properties. For example, if the incoming element is smaller than the maximum element in the max-heap, it can be directly added without comparing with the min-heap. Additionally, in scenarios where the data distribution is known to be skewed, fewer balancing operations may be required, which can help reduce overall balancing overhead.

## 7. Discussion on Templates and Patterns

The Two Heap pattern can be extended to solve problems beyond median finding, such as **partitioning tasks** or **maintaining sliding window statistics**. Depending on the problem, you may need to adjust how you balance the heaps or even combine this pattern with others like **Sliding Window**. For example, in the 'Sliding Window Median' problem, you can use the Sliding Window pattern to maintain a window of k elements and then use the Two Heap pattern to quickly find the median of the current window. This combination allows efficient median calculation as the window slides through the data, providing a practical use case of combining these two patterns.

## 8. Practice Problems

| S.No | Question                                        | Example                                                                                                                                                                                                                                   | Difficulty Level | Approach                                                                                                                                              |
| ---- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Find the median of a data stream                | Input: [5, 15, 1, 3] - Output: Median after each insertion: [5, 10, 5, 4]. Explanation: Insert elements one by one and track median.                                                                                                      | Medium           | Two Heap Pattern (maintain two heaps: max-heap for lower half and min-heap for upper half)                                                            |
| 2    | Sliding window median                           | Input: [1, 3, -1, -3, 5, 3, 6, 7] - Output: [1, -1, -1, 3, 5, 6]. Explanation: Calculate the median for each window of size k.                                                                                                            | Hard             | Two Heap + Sliding Win (use two heaps and a deque to maintain window elements efficiently)                                                            |
| 3    | Task scheduling with priority balancing         | Tasks: A, B, C - Output: Balanced task allocation between two workers. Explanation: Distribute tasks based on priority to balance workload.                                                                                               | Medium           | Two Heap Pattern (use max-heap for high priority tasks and min-heap for low priority tasks)                                                           |
| 4    | Find the kth largest element in a stream        | Input: [4, 5, 8, 2], k=3 - Output: 4. Explanation: Maintain a heap of k largest elements and return the kth largest.                                                                                                                      | Medium           | Two Heap, maintain k (use a min-heap of size k to efficiently find the kth largest element)                                                           |
| 5    | Median of two sorted arrays                     | Input: [1, 3], [2] - Output: 2.0. Explanation: Merge two sorted arrays and find the median.                                                                                                                                               | Hard             | Two Heap + Merge (use two heaps to maintain merged state, extra space for merged data)                                                                |
| 6    | Top k frequent elements                         | Input: [1,1,1,2,2,3], k=2 - Output: [1, 2]. Explanation: Use a heap to maintain k most frequent elements.                                                                                                                                 | Medium           | Min-Heap, k elements (use frequency dictionary and min-heap of size k to find top k elements)                                                         |
| 7    | Minimize deviation in an array                  | Input: [1, 2, 3, 4] - Output: 1. Explanation: Minimize the difference between the largest and smallest elements after modifying elements.                                                                                                 | Hard             | Two Heap + Priority (use max-heap to track maximums and minimize deviation)                                                                           |
| 8    | Connect ropes to minimize cost                  | Input: [4, 3, 2, 6] - Output: 29. Explanation: Connect ropes in such a way that the total cost is minimized.                                                                                                                              | Medium           | Min-Heap Pattern (use a min-heap to repeatedly connect the smallest ropes)                                                                            |
| 9    | K closest points to origin                      | Input: Points = [[1,3],[-2,2]], k=1 - Output: [[-2,2]]. Explanation: Find the k points closest to the origin.                                                                                                                             | Medium           | Max-Heap, distance (use max-heap of size k to maintain the closest points)                                                                            |
| 10   | IPO - Maximize capital                          | Projects with profits and capital - Output: Max profit. Explanation: Choose projects with highest profit within available capital.                                                                                                        | Hard             | Two Heap, priorities (use max-heap for profit and min-heap for capital constraints)                                                                   |
| 11   | Kth smallest element in a matrix                | Input: Matrix = [[1,5,9],[10,11,13],[12,13,15]], k=8 - Output: 13. Explanation: Find the kth smallest element in the matrix.                                                                                                              | Medium           | Min-Heap, matrix iter (use min-heap to extract elements in sorted order, track indices)                                                               |
| 12   | Find the running median                         | Input: Stream: [2, 1, 5, 7, 2, 0, 5] - Output: [2, 1.5, 2, 3.5, 2, 2, 2]. Explanation: Insert each element and calculate the median.                                                                                                      | Medium           | Two Heap Pattern (maintain two heaps for dynamic median calculation)                                                                                  |
| 13   | Smallest range from k lists                     | Input: Lists: [[4,10,15],[1,3,5],[6,9,12]] - Output: [4, 6]. Explanation: Find the smallest range that includes at least one element from each list.                                                                                      | Hard             | Min-Heap, multi-list (use min-heap to track the smallest elements across all lists)                                                                   |
| 14   | Kth largest element in an array                 | Input: [3, 2, 1, 5, 6, 4], k=2 - Output: 5. Explanation: Maintain a heap of k largest elements and return the kth largest.                                                                                                                | Medium           | Min-Heap, k elements (use a min-heap of size k to track the largest elements)                                                                         |
| 15   | Reorganize string                               | Input: "aaabbc" - Output: "ababac". Explanation: Reorganize the string so that no adjacent characters are the same.                                                                                                                       | Medium           | Max-Heap, frequency (use max-heap to track character frequency and reorganize the string)                                                             |
| 16   | Frequency sort                                  | Input: [1,1,1,2,2,3] - Output: [1,1,1,2,2,3]. Explanation: Sort elements by frequency in descending order.                                                                                                                                | Easy             | Max-Heap, frequency (use frequency dictionary and max-heap to sort elements by frequency)                                                             |
| 17   | Kth largest element in a stream (variant)       | Input: [5, 7, 2, 3], k=2 - Output: 5. Explanation: Maintain a heap of k largest elements in the stream.                                                                                                                                   | Medium           | Two Heap Pattern (use a min-heap of size k to efficiently track the kth largest element)                                                              |
| 18   | Kth smallest element in a BST                   | Input: BST elements, k=3 - Output: k-th smallest value. Explanation: Perform an in-order traversal and find the kth element.                                                                                                              | Hard             | Min-Heap, in-order (use min-heap to track elements during in-order traversal)                                                                         |
| 19   | Minimize sum of product of two arrays           | Input: A = [3, 1, 1], B = [6, 5, 4] - Output: 23. Explanation: Pair elements to minimize the sum of products.                                                                                                                             | Medium           | Max-Heap, pairing (use max-heap to pair elements in descending order to minimize product sum)                                                         |
| 20   | Furthest building you can reach                 | Input: Heights, bricks, ladders - Output: Index of furthest building. Explanation: Use heaps to allocate resources efficiently and reach the furthest point.                                                                              | Hard             | Two Heap + Greedy (use two heaps to track ladder usage and bricks efficiently)                                                                        |
| 21   | Maximize score after performing k operations    | Input: [1, 10, 3, 3, 3], k=3 - Output: Maximum score. Explanation: Use heaps to maximize score by selecting elements k times.                                                                                                             | Medium           | Max-Heap, k operations (use max-heap to select the highest elements multiple times)                                                                   |
| 22   | Find the median of merged data from two sources | Input: [1, 2], [3, 4] - Output: 2.5. Explanation: Merge two data sources and find the median.                                                                                                                                             | Medium           | Two Heap, merge data (use two heaps to maintain merged state and track median)                                                                        |
| 23   | Shortest path with alternating colors           | Input: Graph with red/blue edges - Output: Shortest distance. Explanation: Find the shortest path considering alternating edge colors.                                                                                                    | Medium           | Two Heap + Graph BFS (use two heaps to track paths with alternating edge colors)                                                                      |
| 24   | Split array into k subarrays with largest sum   | Input: [7, 2, 5, 10, 8], k=2 - Output: Split into [7, 2] and [5, 10, 8] to maximize the minimum largest sum, which is 18. Explanation: Split the array optimally to balance the subarrays and maximize the smallest possible largest sum. | Hard             | Max-Heap, split points, find optimal partitioning to maximize the smallest possible largest sum (use extra tracking variables to evaluate partitions) |

## 09. Key Takeaways, Tips, and Summary

- **Key Takeaways**: The Two Heap pattern helps in efficiently balancing elements and provides quick access to the median.
- **Practical Tips**: Always ensure **Max-Heap** and **Min-Heap** are balanced, especially when dealing with insertion and deletion.
- **Summary**: The Two Heap pattern is efficient for problems involving **median** and **balancing elements dynamically**.

## 10. Common Pitfalls

- **Mistakes to Avoid**: Forgetting to balance the heaps after every insertion can lead to incorrect median calculations.
- **Troubleshooting Tips**: If the median value seems off, check the balancing condition of the heaps; they should either be of equal size or the max-heap should have one extra element.

TSure, here are detailed explanations for five random practice problems, including numeric examples and Python code as comments.

### Problem 1: Find the Median of a Data Stream
**Problem**: You need to find the median of a stream of numbers as they are added one by one.

**Example**:
- **Input**: [5, 15, 1, 3]
- **Output**: [5, 10, 5, 4]
- **Explanation**: After inserting each number, the median changes:
  - Insert 5: Median is 5.
  - Insert 15: Median is (5 + 15) / 2 = 10.
  - Insert 1: Median is 5.
  - Insert 3: Median is (3 + 5) / 2 = 4.

**Python Code**:
```python
# Python code for finding the median of a data stream
import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap for the lower half of the numbers
        self.max_heap = []
        # Min-heap for the upper half of the numbers
        self.min_heap = []

    def add_num(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

# Test the implementation
median_finder = MedianFinder()
stream = [5, 15, 1, 3]
for num in stream:
    median_finder.add_num(num)
    print(f"Median after inserting {num}: {median_finder.find_median()}")
```

### Problem 2: Sliding Window Median
**Problem**: Given an array of numbers and a window size `k`, find the median of all sliding windows of size `k`.

**Example**:
- **Input**: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
- **Output**: [1, -1, -1, 3, 5, 6]
- **Explanation**: The medians of each sliding window are:
  - Window [1, 3, -1]: Median is 1.
  - Window [3, -1, -3]: Median is -1.
  - Window [-1, -3, 5]: Median is -1.
  - Window [-3, 5, 3]: Median is 3.
  - Window [5, 3, 6]: Median is 5.
  - Window [3, 6, 7]: Median is 6.

**Python Code**:
```python
# Python code for finding the sliding window median
import heapq
from sortedcontainers import SortedList

def sliding_window_median(nums, k):
    result = []
    window = SortedList()

    for i in range(len(nums)):
        window.add(nums[i])
        if len(window) > k:
            window.remove(nums[i - k])
        if len(window) == k:
            median = (window[k // 2] + window[(k - 1) // 2]) / 2
            result.append(median)

    return result

# Test the implementation
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_median(nums, k))
```

### Problem 3: K Closest Points to Origin
**Problem**: Given an array of points, find the `k` points closest to the origin.

**Example**:
- **Input**: points = [[1, 3], [-2, 2]], k = 1
- **Output**: [[-2, 2]]
- **Explanation**: The point [-2, 2] is closer to the origin than [1, 3].

**Python Code**:
```python
# Python code to find the k closest points to the origin
import heapq

def k_closest(points, k):
    max_heap = []
    for (x, y) in points:
        distance = -(x * x + y * y)  # Using negative for max-heap
        heapq.heappush(max_heap, (distance, x, y))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [[x, y] for (dist, x, y) in max_heap]

# Test the implementation
points = [[1, 3], [-2, 2]]
k = 1
print(k_closest(points, k))
```

### Problem 4: Top K Frequent Elements
**Problem**: Given a non-empty array of integers, return the `k` most frequent elements.

**Example**:
- **Input**: nums = [1, 1, 1, 2, 2, 3], k = 2
- **Output**: [1, 2]
- **Explanation**: The numbers 1 and 2 are the two most frequent elements.

**Python Code**:
```python
# Python code to find the top k frequent elements
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# Test the implementation
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k))
```

### Problem 5: Minimize Deviation in Array
**Problem**: You are given an array `nums` of `n` positive integers. You can perform two types of operations on any element of the array: if the element is even, divide it by 2; if the element is odd, multiply it by 2. Return the minimum possible difference between the maximum and minimum values in `nums`.

**Example**:
- **Input**: nums = [1, 2, 3, 4]
- **Output**: 1
- **Explanation**: Convert the array to [2, 2, 3, 4], then [2, 2, 3, 2], the difference is 1.

**Python Code**:
```python
# Python code to minimize deviation in an array
import heapq

def minimum_deviation(nums):
    max_heap = []
    for num in nums:
        if num % 2 == 1:
            num *= 2
        heapq.heappush(max_heap, -num)

    min_value = -max(max_heap)
    min_deviation = float('inf')

    while max_heap:
        max_value = -heapq.heappop(max_heap)
        min_deviation = min(min_deviation, max_value - min_value)
        if max_value % 2 == 1:
            break
        max_value //= 2
        min_value = min(min_value, max_value)
        heapq.heappush(max_heap, -max_value)

    return min_deviation

# Test the implementation
nums = [1, 2, 3, 4]
print(minimum_deviation(nums))
```

These explanations provide detailed steps for understanding the problem along with Python code to implement the solution. Let me know if you'd like any more examples or further assistance!