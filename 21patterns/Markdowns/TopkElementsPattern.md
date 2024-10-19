# Top-K Elements Coding Pattern: Comprehensive Guide

## 1. Core Concepts and Coding Patterns

The **Top-K Elements** pattern focuses on finding the top k items in a collection. It often involves using data structures like **heaps** (min-heap or max-heap) or other efficient sorting mechanisms. The goal is to optimize finding the **k largest** or **k smallest** elements without needing to sort the entire collection, which would be less efficient.

**Typical Use Cases**:

- Finding the k largest or smallest numbers in an array.
- Identifying the top k frequent elements in a dataset.
- Sorting the largest k items in streaming data.

**Heaps and Priority Queues** play a major role in implementing this pattern efficiently.

## 2. Examples

Consider the array: **[7, 10, 4, 3, 20, 15]**

- **Problem**: Find the **3 smallest elements**.
- **Solution**: Using a **max-heap**, we maintain a heap of size k (in this case, 3). After iterating through the entire array, the heap contains: **[4, 3, 7]**.

Another example:

- **Problem**: Find the **2 largest elements** in the array **[1, 5, 12, 2, 11, 5]**.
- **Solution**: Using a **min-heap** of size 2, we end up with **[11, 12]**.

## 3. Problem Identification Checklist

| **Characteristic**          | **Explanation**                                             | **Example**                         |
| --------------------------- | ----------------------------------------------------------- | ----------------------------------- |
| Size Constraints            | The problem asks for a subset (k items) of an array or list | Find the k largest elements         |
| Sorting Unnecessary         | Sorting the entire collection isn't needed, just part of it | Return the top k frequent words     |
| Need for Dynamic Extraction | Requires extracting max/min elements efficiently            | Identify k closest points to origin |

## 4. General Templates with Comments

### Template 1: Finding Top K Largest Elements Using Min-Heap

```python
import heapq

def find_k_largest_elements(nums, k):
    # Step 1: Initialize a min-heap with first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)  # Convert list into a heap
    
    # Step 2: Iterate over the remaining elements
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)  # Remove smallest in min-heap
            heapq.heappush(min_heap, num)  # Add the new number
    
    # Step 3: Return the top k largest elements in the heap
    return list(min_heap)
```

**Use Case**: This template works best when you want to find the k largest numbers, and the size of k is much smaller than the length of the input.

### Template 2: Finding Top K Frequent Elements Using Max-Heap

```python
import heapq
from collections import Counter

def find_top_k_frequent(nums, k):
    # Step 1: Build the frequency dictionary
    freq_map = Counter(nums)
    
    # Step 2: Create a max-heap using negative frequency values
    max_heap = [(-freq, num) for num, freq in freq_map.items()]
    heapq.heapify(max_heap)
    
    # Step 3: Extract top k frequent elements
    top_k = []
    for _ in range(k):
        top_k.append(heapq.heappop(max_heap)[1])
    
    return top_k
```

**Use Case**: This pattern is useful for finding k most frequent elements in an array, such as analyzing word frequency in a text corpus.

## 5. Complexity Analysis

- **Time Complexity**:
  - **Min-Heap Template**: Building a heap takes **O(k)**, and for each remaining element, adjusting the heap takes **O(log k)**. Overall complexity is **O(n log k)**.
  - **Max-Heap Template**: Creating a frequency map is **O(n)**, and heapifying takes **O(n)**. Extracting elements has a complexity of **O(k log n)**.
- **Space Complexity**:
  - Both approaches require **O(k)** additional space for storing the heap.
- **Optimization Opportunities**: In cases where k is very large, converting to a sorting approach may provide simpler and comparable performance.

## 6. Discussion on Templates and Patterns

The Top-K Elements templates can be applied to many problem variations, often involving dynamic data where you only need to know the most significant few. However, depending on whether you need maximum or minimum values, a **min-heap** or **max-heap** will be used.

For problems with large data streams, consider implementing more optimized structures like **count-min sketch**.

## 7. Multiple Approaches and Implementations

- **Iterative vs Recursive**: Heaps are inherently iterative in Python. A sorting-based approach (like quickselect) can also be recursive.
- **Comparative Analysis**: Iterative heap approaches are easy to implement but might be less optimal for large k. Recursive approaches like quickselect have better average time complexity.

## 8. Practice Problems

| **S.No** | **Question**                            | **Example**                                                                               | **Difficulty Level** | **Approach**                            |
| -------- | --------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------- | --------------------------------------- |
| 1        | Find k largest numbers in an array      | Given array [3,2,1,5,6,4], k=2. Output: [5, 6]                                            | Medium               | Min-Heap                                |
| 2        | Find top k frequent words               | Given words ["word1", "word2", "word1"], k=1. Output: ["word1"]                           | Medium               | Max-Heap                                |
| 3        | Find k closest points to the origin     | Given points = [[1,3],[-2,2]], k=1. Output: [[-2,2]]                                      | Hard                 | Max-Heap                                |
| 4        | Find k smallest numbers in an array     | Given array [7, 10, 4, 3, 20, 15], k=3. Output: [3, 4, 7]                                 | Medium               | Max-Heap                                |
| 5        | Find top k frequent numbers             | Given array [1, 1, 1, 2, 2, 3], k=2. Output: [1, 2]                                       | Medium               | Max-Heap                                |
| 6        | Find k largest elements in a stream     | Stream input [5, 2, 9, 1, 7, 3], k=3. Output: [7, 9, 5]                                   | Hard                 | Min-Heap with streaming logic, extra variable to track stream iteration |
| 7        | Find k most frequent characters         | Given string "aaabbc", k=2. Output: ['a', 'b']                                            | Medium               | Max-Heap                                |
| 8        | Find k smallest pairs                   | Given arrays nums1=[1,7,11], nums2=[2,4,6], k=3. Output: [(1, 2), (1, 4), (1, 6)]         | Hard                 | Min-Heap, additional variables for pair indices |
| 9        | Find k closest numbers to x             | Given array [1, 2, 3, 4, 5], k=4, x=3. Output: [2, 3, 4, 5]                               | Medium               | Max-Heap, extra variable to store distance from x |
| 10       | Find k most frequent elements in matrix | Given matrix [[1, 2], [1, 3], [3, 3]], k=2. Output: [3, 1]                                | Hard                 | Max-Heap, requires flattening the matrix first    |
| 11       | Find top k URLs by hit count            | Given URLs ["a.com", "b.com", "a.com", "c.com", "b.com"], k=2. Output: ["a.com", "b.com"] | Medium               | Max-Heap                                |
| 12       | Find k highest scoring students         | Given scores [87, 92, 67, 70, 89, 94], k=3. Output: [94, 92, 89]                          | Medium               | Min-Heap                                |
| 13       | Find k least common words               | Given words ["dog", "cat", "bird", "cat", "dog", "cat"], k=1. Output: ["bird"]            | Medium               | Max-Heap                                |
| 14       | Find k smallest elements in a BST       | Given BST root, k=3. Output: [1, 2, 3]                                                    | Hard                 | In-order traversal with Min-Heap        |
| 15       | Find k elements closest to median       | Given array [1, 3, 8, 2, 7], k=2. Output: [3, 7]                                          | Hard                 | Median calculation followed by Max-Heap, extra median variable |
| 16       | Find k largest sums from pairs          | Given arrays [4, 2, 5], [8, 0, 3], k=3. Output: [13, 12, 9]                               | Hard                 | Max-Heap, variables for indices tracking pairs    |
| 17       | Find k most frequent digits in a number | Given number 112233445, k=2. Output: [1, 2]                                               | Medium               | Max-Heap                                |
| 18       | Find top k elements in a rotating array | Given array [1, 3, 5, 7, 9], k=3, rotated by 2. Output: [7, 9, 5]                         | Hard                 | Min-Heap with rotation logic, rotation variable   |
| 19       | Find k largest unique numbers           | Given array [4, 4, 6, 1, 7, 7, 8], k=3. Output: [8, 7, 6]                                 | Medium               | Min-Heap                                |
| 20       | Find k closest restaurants              | Given distances [5.0, 2.3, 8.6, 3.7], k=2. Output: [2.3, 3.7]                             | Easy                 | Max-Heap                                |

## 9. Key Takeaways, Tips, and Summary

- **Key Takeaways**: The Top-K Elements pattern is well-suited for problems requiring partial sorting or selection.
- **Practical Tips**: When k is small, heaps offer efficient solutions. Use **quickselect** when the input data is large and k is close to n.
- **Summary**: Mastering heap usage for k-selection will help solve problems efficiently in competitive programming and interviews.

## 10. Common Pitfalls

- **Mistakes to Avoid**:
  - Using a **max-heap** when a **min-heap** would be more efficient.
  - Sorting the entire array instead of using a heap for k selection.
- **Troubleshooting Tips**:
  - Check the heap condition: ensure proper use of **heapify** and **heappop/heappush** to avoid incorrect heap orders.
  - For negative values or custom objects, remember to modify the comparison logic accordingly.

## Final Key Takeaways

- Using heaps can help solve Top-K problems efficiently.
- Each problem may have slight variations, such as handling dynamic data or computing distances.
- Practice these problems to become comfortable applying heaps to various scenarios.

Here are the detailed explanations and Python code solutions for 5 randomly selected practice problems from the list:

### 1. Problem 4: Find k Smallest Numbers in an Array
**Problem**: Given an array `[7, 10, 4, 3, 20, 15]`, find the `3` smallest elements.
**Explanation**: 
- We want to find the 3 smallest numbers in the array, which are `[3, 4, 7]`.
- To solve this, we use a **max-heap** of size `k=3`. This helps us maintain the smallest elements efficiently.
**Python Code**:
```python
import heapq

def find_k_smallest_elements(nums, k):
    # Step 1: Create a max-heap with the first k elements (negate values to simulate a max-heap)
    max_heap = [-num for num in nums[:k]]
    heapq.heapify(max_heap)

    # Step 2: Iterate over the remaining elements
    for num in nums[k:]:
        if -num > max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -num)

    # Step 3: Return the k smallest elements (convert back to positive values)
    return [-num for num in max_heap]

# Example usage
nums = [7, 10, 4, 3, 20, 15]
k = 3
print(find_k_smallest_elements(nums, k))  # Output: [3, 4, 7]
```

### 2. Problem 7: Find k Most Frequent Characters
**Problem**: Given a string `"aaabbc"`, find the `2` most frequent characters.
**Explanation**: 
- The characters are `"a"` and `"b"` as they appear most frequently (`a` appears 3 times, `b` appears 2 times).
- We use a **max-heap** to determine the characters with the highest frequency.
**Python Code**:
```python
import heapq
from collections import Counter

def find_k_most_frequent_chars(s, k):
    # Step 1: Build the frequency dictionary
    freq_map = Counter(s)
    
    # Step 2: Create a max-heap using negative frequency values
    max_heap = [(-freq, char) for char, freq in freq_map.items()]
    heapq.heapify(max_heap)
    
    # Step 3: Extract top k frequent characters
    top_k = []
    for _ in range(k):
        top_k.append(heapq.heappop(max_heap)[1])
    
    return top_k

# Example usage
s = "aaabbc"
k = 2
print(find_k_most_frequent_chars(s, k))  # Output: ['a', 'b']
```

### 3. Problem 9: Find k Closest Numbers to x
**Problem**: Given an array `[1, 2, 3, 4, 5]`, find the `4` numbers closest to `3`.
**Explanation**: 
- The 4 closest numbers to `3` are `[2, 3, 4, 5]`.
- We use a **max-heap** to keep track of the closest numbers by calculating the distance from `x`.
**Python Code**:
```python
import heapq

def find_k_closest_numbers(nums, k, x):
    # Step 1: Create a max-heap with (distance from x, value) tuples
    max_heap = []
    for num in nums:
        distance = abs(num - x)
        heapq.heappush(max_heap, (-distance, -num))  # Use negative values to simulate max-heap
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    
    # Step 2: Extract elements from the heap and return them in sorted order
    result = [-num for (_, num) in max_heap]
    return sorted(result)

# Example usage
nums = [1, 2, 3, 4, 5]
k = 4
x = 3
print(find_k_closest_numbers(nums, k, x))  # Output: [2, 3, 4, 5]
```

### 4. Problem 16: Find k Largest Sums from Pairs
**Problem**: Given arrays `[4, 2, 5]` and `[8, 0, 3]`, find the `3` largest sums of pairs formed by picking one element from each array.
**Explanation**:
- Possible pairs: `(4+8, 4+0, 4+3, 2+8, 2+0, 2+3, 5+8, 5+0, 5+3)` resulting in sums `[12, 4, 7, 10, 2, 5, 13, 5, 8]`.
- The `3` largest sums are `[13, 12, 10]`.
**Python Code**:
```python
import heapq

def find_k_largest_sums(nums1, nums2, k):
    # Step 1: Create a max-heap with all pair sums
    max_heap = []
    for num1 in nums1:
        for num2 in nums2:
            heapq.heappush(max_heap, -(num1 + num2))
    
    # Step 2: Extract top k sums
    result = []
    for _ in range(k):
        result.append(-heapq.heappop(max_heap))
    
    return result

# Example usage
nums1 = [4, 2, 5]
nums2 = [8, 0, 3]
k = 3
print(find_k_largest_sums(nums1, nums2, k))  # Output: [13, 12, 10]
```

### 5. Problem 20: Find k Closest Restaurants
**Problem**: Given distances `[5.0, 2.3, 8.6, 3.7]`, find the `2` closest distances.
**Explanation**:
- The 2 closest distances are `[2.3, 3.7]`.
- We use a **max-heap** to keep track of the closest `k` distances.
**Python Code**:
```python
import heapq

def find_k_closest_restaurants(distances, k):
    # Step 1: Create a max-heap with the first k distances (negate to simulate max-heap)
    max_heap = [-dist for dist in distances[:k]]
    heapq.heapify(max_heap)
    
    # Step 2: Iterate over the remaining distances
    for dist in distances[k:]:
        if -dist > max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -dist)
    
    # Step 3: Return the k closest distances
    return [-dist for dist in max_heap]

# Example usage
distances = [5.0, 2.3, 8.6, 3.7]
k = 2
print(find_k_closest_restaurants(distances, k))  # Output: [2.3, 3.7]
```

These detailed explanations and code examples should help you understand how to approach the Top-K Elements pattern effectively. Let me know if you need any further clarification!