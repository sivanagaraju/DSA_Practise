# **K-Way Merge: Comprehensive Guide**

## 1. Core Concepts and Coding Patterns

The K-Way Merge is a fundamental coding pattern used to merge multiple sorted arrays or lists into a single sorted list. The core idea is to use a Min-Heap (or Max-Heap) to keep track of the smallest (or largest) elements among the arrays during the merge process.

- **How It Works**: The pattern involves pushing the first element of each sorted array into a Min-Heap, extracting the minimum value, and then adding the next element from the corresponding array to the heap. This process continues until all elements are merged.
- **Typical Use Cases**: This pattern is commonly used in scenarios like merging k sorted arrays or lists, merging k sorted linked lists, or finding the smallest range that includes at least one number from each of the k lists.

### 2. Examples

**Example 1**: Merging Three Sorted Arrays

Given three sorted arrays:

- Array 1: [1, 4, 7]
- Array 2: [2, 5, 8]
- Array 3: [3, 6, 9]

To merge these arrays using a K-Way Merge:

1. Insert the first element from each array into the Min-Heap: [1, 2, 3].
2. Extract the smallest (1) and add the next element from Array 1 to the heap: [2, 3, 4].
3. Continue extracting and adding until all elements are merged.

**Result**: [1, 2, 3, 4, 5, 6, 7, 8, 9]

### 3. Problem Identification Checklist

| Problem Type                           | Example Problem                                                                    |
| -------------------------------------- | ---------------------------------------------------------------------------------- |
| Merging Sorted Lists                   | Merge k sorted linked lists into one sorted list                                   |
| Finding Smallest Range                 | Find the smallest range that includes at least one number from each of the k lists |
| Sorting Elements from Multiple Streams | Given k sorted arrays, return a sorted output of all elements                      |

### 4. General Templates with Comments

#### Template 1: Merging k Sorted Arrays Using a Min-Heap

```python
from heapq import heappush, heappop

def merge_k_sorted_arrays(arrays):
    min_heap = []
    result = []

    # Insert the first element of each array into the heap
    for i, array in enumerate(arrays):
        if array:
            heappush(min_heap, (array[0], i, 0))  # (value, array_index, element_index)

    # Extract elements from the heap and add the next element from the same array
    while min_heap:
        value, array_index, element_index = heappop(min_heap)
        result.append(value)
        
        # If there is another element in the same array, add it to the heap
        if element_index + 1 < len(arrays[array_index]):
            next_value = arrays[array_index][element_index + 1]
            heappush(min_heap, (next_value, array_index, element_index + 1))

    return result
```

**Use Case**: This template is most applicable for merging k sorted arrays where each array is independently sorted.

#### Template 2: Merging k Sorted Linked Lists

```python
from heapq import heappush, heappop

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_k_sorted_linked_lists(lists):
    min_heap = []

    # Insert the head of each linked list into the heap
    for i, root in enumerate(lists):
        if root:
            heappush(min_heap, (root.value, i, root))

    result_head, result_tail = None, None

    # Extract the smallest element from the heap and add the next node from the same list
    while min_heap:
        value, i, node = heappop(min_heap)
        if not result_head:
            result_head = result_tail = node
        else:
            result_tail.next = node
            result_tail = result_tail.next

        if node.next:
            heappush(min_heap, (node.next.value, i, node.next))

    return result_head
```

**Use Case**: This template is ideal for merging k sorted linked lists, where each list is independently sorted.

### 5. Complexity Analysis

- **Time Complexity**: Inserting and extracting from the Min-Heap takes O(log k), and since we process all elements, the time complexity is O(N log k), where N is the total number of elements.
- **Space Complexity**: The space complexity is O(k) for storing elements in the heap.
- **Optimization Opportunities**: One possible optimization is to use a balanced binary search tree instead of a heap if frequent reordering is required.

### 6. Discussion on Templates and Patterns

These templates can be adjusted depending on the specific question. For instance, if the input size is extremely large, consider using a generator to reduce memory usage.

### 7. Multiple Approaches and Implementations

- **Iterative vs. Recursive**: The K-Way Merge is generally implemented iteratively to avoid the overhead of recursion, especially when dealing with a large number of lists.
- **Comparative Analysis**: Iterative approaches are more memory-efficient, while recursive approaches may offer more elegant code but come with stack overflow risks.

### 9. Practice Problems

| S.No | Question                                         | Example                                                                                                                                                                                                                                                                                                                                  | Difficulty Level | Approach                                        |
| ---- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------- |
| 1    | Merge k Sorted Lists                             | Input: [[1, 4, 5], [1, 3, 4], [2, 6]] - Start by adding the first elements of all arrays into the Min-Heap: [1, 1, 2]. Extract the smallest element (1), and add the next element from the corresponding list to the heap. Continue until all elements are merged. Output: [1, 1, 2, 3, 4, 4, 5, 6]                                      | Medium           | Use Min-Heap to keep track of smallest elements |
| 2    | Smallest Range Covering Elements from k Lists    | Input: [[4, 10, 15], [1, 10, 20], [5, 8, 12]] - Start by adding the first elements from all lists into the Min-Heap: [1, 4, 5]. Track the range using the minimum and maximum elements. Expand the range by including the next element from the corresponding list until the smallest range covering all lists is found. Output: [5, 10] | Hard             | Use Min-Heap to track min and max range         |
| 3    | Merge k Sorted Arrays                            | Input: [[1, 3, 5], [2, 4, 6], [0, 9, 10]] - Add the first elements from all arrays into the Min-Heap: [0, 1, 2]. Extract the minimum element and add the next element from the corresponding array. Repeat until all arrays are merged. Output: [0, 1, 2, 3, 4, 5, 6, 9, 10]                                                             | Medium           | Use Min-Heap to merge sorted arrays             |
| 4    | Find k Smallest Elements in k Sorted Arrays      | Input: [[2, 6, 8], [3, 6, 7], [1, 3, 4]] - Start by adding the first elements from each array into the Min-Heap: [1, 2, 3]. Extract the smallest element and add the next element from the same array to the heap. Continue until all elements are processed. Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]                                        | Medium           | Use Min-Heap to keep track of smallest elements |
| 5    | Kth Smallest Number in M Sorted Lists            | Input: [[2, 6, 8], [3, 6, 7], [1, 3, 4]], k=5 - Add the first elements from each list into the Min-Heap: [1, 2, 3]. Extract the smallest element and add the next element from the corresponding list. Continue extracting until the kth smallest element is found. Output: 4                                                            | Medium           | Use Min-Heap to find kth smallest element       |
| 6    | Merge k Sorted Linked Lists                      | Input: [LinkedList1: 1->4->5, LinkedList2: 1->3->4, LinkedList3: 2->6] - Add the heads of all linked lists to the Min-Heap: [1, 1, 2]. Extract the smallest element, add it to the result, and push the next node from the corresponding list to the heap. Continue until all lists are merged. Output: 1->1->2->3->4->4->5->6           | Medium           | Use Min-Heap to merge linked lists              |
| 7    | Find Smallest Common Number from k Sorted Arrays | Input: [[1, 2, 3, 4], [2, 3, 5], [2, 4, 6]] - Add the first elements from each list into the Min-Heap: [1, 2, 2]. Continue extracting and adding the next element from the corresponding list until a common number is found in all arrays. Output: 2                                                                                    | Hard             | Use Min-Heap to track common elements           |
| 8    | Find the Largest Range Covering k Lists          | Input: [[1, 5, 8], [4, 12], [7, 8, 10]] - Add the first elements from each list into the Min-Heap: [1, 4, 7]. Track the minimum and maximum elements to determine the range. Expand by adding the next element from the corresponding list until the largest range covering all lists is found. Output: [4, 8]                           | Hard             | Use Min-Heap and Max-Heap to track ranges       |
| 9    | Sort k Increasing-Decreasing Arrays              | Input: [[1, 5, 7], [8, 6, 4], [3, 2, 9]] - Split each array into increasing and decreasing parts, reverse the decreasing parts, and add the first elements to the Min-Heap. Extract and add elements to form the sorted output. Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]                                                                      | Medium           | Split, merge, and use Min-Heap                  |
| 10   | Find Median of k Sorted Arrays                   | Input: [[1, 3], [2], [4, 6]] - Add the first elements from each array into the Min-Heap: [1, 2, 4]. Extract the smallest elements while tracking the count until the median is found. Output: 3                                                                                                                                          | Hard             | Use Min-Heap and Max-Heap to find median        |
| 11   | Kth Largest Element in k Sorted Arrays           | Input: [[1, 5, 7], [3, 6, 8], [4, 10]], k=4 - Add the last elements from each array into a Max-Heap: [10, 8, 7]. Extract elements until the kth largest is found. Output: 7 (for k=4)                                                                                                                                                    | Medium           | Use Max-Heap to keep track of largest elements  |
| 12   | Smallest Number Range Covering Elements          | Input: [[1, 3, 5], [4, 8], [6, 10]] - Add the first elements from each list into the Min-Heap: [1, 4, 6]. Track the range using the minimum and maximum elements. Expand until the smallest range covering all lists is found. Output: [4, 6]                                                                                            | Hard             | Use Min-Heap to track range                     |
| 13   | Merge k Sorted Stacks                            | Input: [Stack1: [1, 3, 5], Stack2: [2, 4], Stack3: [6, 7]] - Convert stacks into lists, add the first elements to the Min-Heap, extract the minimum, and push the next element from the corresponding stack. Continue until all stacks are merged. Output: [1, 2, 3, 4, 5, 6, 7]                                                         | Medium           | Use Min-Heap to merge stacks                    |
| 14   | Merge k Lists with Custom Comparator             | Input: [[1, 3, 5], [2, 4], [7, 8, 9]] - Add the first elements from each list into the Min-Heap using a custom comparator. Extract the smallest element and push the next element from the corresponding list until all lists are merged. Output: [1, 2, 3, 4, 5, 7, 8, 9]                                                               | Medium           | Use Min-Heap with custom comparator             |
| 15   | Kth Largest Number in k Arrays                   | Input: [[1, 2, 3], [4, 5], [6, 7, 8]], k=3 - Add the last elements from each array into a Max-Heap: [8, 5, 3]. Extract the largest elements until the kth largest is found. Output: 6                                                                                                                                                    | Medium           | Use Min-Heap for kth largest calculation        |
| 16   | Merge k Binary Search Trees                      | Input: [BST1: [2, 4, 6], BST2: [1, 3, 5], BST3: [0, 7, 8]] - Perform in-order traversal on each BST, add the elements to a Min-Heap, and extract to merge into a sorted tree. Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]                                                                                                                        | Hard             | Use Min-Heap to merge BST nodes                 |
| 17   | Find kth Largest Element in Sorted Streams       | Input: [Stream1: [1, 3, 5], Stream2: [2, 4, 6], Stream3: [0, 9, 10]], k=4 - Add elements from each stream into a Min-Heap and extract until the kth largest element is found. Output: 5                                                                                                                                                  | Hard             | Use Min-Heap to track stream elements           |
| 18   | Find the Largest Interval Covering k Lists       | Input: [[1, 3, 5], [2, 6], [3, 7]] - Add the first elements from each list into the Min-Heap: [1, 2, 3]. Track the interval using the minimum and maximum values, expanding until the largest interval covering all lists is found. Output: [2, 3]                                                                                       | Hard             | Use Min-Heap to determine intervals             |
| 19   | Merge k Arrays with Duplicates                   | Input: [[1, 2, 2], [3, 4], [2, 5]] - Add the first elements from each array into the Min-Heap: [1, 2, 2]. Extract the smallest element, and push the next element from the corresponding list. Continue until all elements are merged. Output: [1, 2, 2, 2, 3, 4, 5]                                                                     | Medium           | Use Min-Heap to merge arrays with duplicates    |
| 20   | Find Smallest Missing Element from k Arrays      | Input: [[0, 1, 2], [3, 4, 5], [6, 7]] - Add the first elements from each array into the Min-Heap: [0, 3, 6]. Extract elements while keeping track of the missing sequence until the smallest missing element is found. Output: 8                                                                                                         | Hard             | Use Min-Heap to track missing elements          |

### 10. Key Takeaways, Tips, and Summary

- **Key Takeaways**: The K-Way Merge is efficient for merging multiple sorted inputs, utilizing a Min-Heap to maintain order.
- **Practical Tips**: Always remember to push the next element from the same list after extracting the minimum.
- **Summary**: Mastering the K-Way Merge template is crucial for problems involving merging or sorting multiple sorted data structures.

### 11. Common Pitfalls

- **Mistakes to Avoid**: Forgetting to add the next element from the same list to the heap can lead to incorrect results.
- **Troubleshooting Tips**: Use print statements to debug heap operations and track the elements being added or removed.


Here are five random problems selected from the practice problems section with detailed explanations, including numeric examples and, if required, visualizations. I have also provided Python code as comments to illustrate each solution.

### Problem 1: Merge k Sorted Arrays
- **Input**: `[[1, 3, 5], [2, 4, 6], [0, 9, 10]]`
- **Explanation**: 
  1. Start by adding the first element of each array into the Min-Heap: `[0, 1, 2]`.
  2. Extract the minimum element (`0`) and add the next element from Array 3 to the heap: `[1, 2, 9]`.
  3. Continue this process until all elements are merged.
- **Visualization**:
  ```
  Step 1: Min-Heap = [0, 1, 2] -> Result = []
  Step 2: Extract 0, Add 9 -> Min-Heap = [1, 2, 9] -> Result = [0]
  Step 3: Extract 1, Add 3 -> Min-Heap = [2, 3, 9] -> Result = [0, 1]
  ...
  Final Result = [0, 1, 2, 3, 4, 5, 6, 9, 10]
  ```
- **Python Code**:
  ```python
  # Use Min-Heap to merge sorted arrays
  from heapq import heappush, heappop
  
  def merge_k_sorted_arrays(arrays):
      min_heap = []
      result = []
  
      # Insert the first element of each array into the heap
      for i, array in enumerate(arrays):
          if array:
              heappush(min_heap, (array[0], i, 0))  # (value, array_index, element_index)
  
      # Extract elements from the heap and add the next element from the same array
      while min_heap:
          value, array_index, element_index = heappop(min_heap)
          result.append(value)
          
          # If there is another element in the same array, add it to the heap
          if element_index + 1 < len(arrays[array_index]):
              next_value = arrays[array_index][element_index + 1]
              heappush(min_heap, (next_value, array_index, element_index + 1))
  
      return result
  ```

### Problem 2: Find Smallest Common Number from k Sorted Arrays
- **Input**: `[[1, 2, 3, 4], [2, 3, 5], [2, 4, 6]]`
- **Explanation**:
  1. Add the first elements from each list into the Min-Heap: `[1, 2, 2]`.
  2. Extract and continue until a common number (`2`) is found in all arrays.
- **Visualization**:
  ```
  Step 1: Min-Heap = [1, 2, 2] -> Extract 1
  Step 2: Add next element from the first array -> Min-Heap = [2, 2, 3]
  ...
  Common Number Found = 2
  ```
- **Python Code**:
  ```python
  # Use Min-Heap to find smallest common number
  from heapq import heappush, heappop
  
  def find_smallest_common(arrays):
      min_heap = []
  
      # Insert the first element of each array into the heap
      for i, array in enumerate(arrays):
          if array:
              heappush(min_heap, (array[0], i, 0))  # (value, array_index, element_index)
  
      current_common = set()
  
      while min_heap:
          value, array_index, element_index = heappop(min_heap)
          current_common.add(value)
          
          # If there are multiple occurrences, check if they are in all arrays
          if len(current_common) == len(arrays):
              return value
  
          # Add next element from the same array if available
          if element_index + 1 < len(arrays[array_index]):
              next_value = arrays[array_index][element_index + 1]
              heappush(min_heap, (next_value, array_index, element_index + 1))
  
      return -1  # Return -1 if no common element is found
  ```

### Problem 3: Kth Smallest Number in M Sorted Lists
- **Input**: `[[2, 6, 8], [3, 6, 7], [1, 3, 4]]`, `k=5`
- **Explanation**:
  1. Add the first elements from each list into the Min-Heap: `[1, 2, 3]`.
  2. Extract the smallest element (`1`), add the next element from the corresponding list, and continue until the `kth` smallest is found.
- **Visualization**:
  ```
  Step 1: Min-Heap = [1, 2, 3]
  Step 2: Extract 1, Add 3 -> Min-Heap = [2, 3, 3]
  Step 3: Extract 2, Add 6 -> Min-Heap = [3, 3, 6]
  ...
  5th Smallest Element = 4
  ```
- **Python Code**:
  ```python
  # Use Min-Heap to find kth smallest element
  def kth_smallest_in_m_lists(arrays, k):
      min_heap = []
  
      # Insert the first element of each array into the heap
      for i, array in enumerate(arrays):
          if array:
              heappush(min_heap, (array[0], i, 0))  # (value, array_index, element_index)
  
      number_count, kth_smallest = 0, None
  
      while min_heap:
          value, array_index, element_index = heappop(min_heap)
          number_count += 1
          
          if number_count == k:
              kth_smallest = value
              break
  
          # Add next element from the same array if available
          if element_index + 1 < len(arrays[array_index]):
              next_value = arrays[array_index][element_index + 1]
              heappush(min_heap, (next_value, array_index, element_index + 1))
  
      return kth_smallest
  ```

### Problem 4: Find the Largest Range Covering k Lists
- **Input**: `[[1, 5, 8], [4, 12], [7, 8, 10]]`
- **Explanation**:
  1. Add the first element of each list into the Min-Heap: `[1, 4, 7]`.
  2. Track the range using the minimum and maximum elements until the largest range covering all lists is found.
- **Visualization**:
  ```
  Step 1: Min-Heap = [1, 4, 7] -> Current Max = 7
  Step 2: Extract 1, Add 5 -> Min-Heap = [4, 5, 7] -> Current Max = 7
  ...
  Largest Range = [4, 8]
  ```
- **Python Code**:
  ```python
  # Use Min-Heap to determine largest range
  def largest_range_covering_k_lists(arrays):
      min_heap = []
      current_max = float('-inf')
  
      for i, array in enumerate(arrays):
          if array:
              heappush(min_heap, (array[0], i, 0))
              current_max = max(current_max, array[0])
  
      range_start, range_end = 0, float('inf')
  
      while min_heap:
          value, array_index, element_index = heappop(min_heap)
  
          if current_max - value < range_end - range_start:
              range_start, range_end = value, current_max
  
          if element_index + 1 < len(arrays[array_index]):
              next_value = arrays[array_index][element_index + 1]
              heappush(min_heap, (next_value, array_index, element_index + 1))
              current_max = max(current_max, next_value)
          else:
              break
  
      return (range_start, range_end)
  ```

### Problem 5: Smallest Number Range Covering Elements
- **Input**: `[[1, 3, 5], [4, 8], [6, 10]]`
- **Explanation**:
  1. Add the first element of each list into the Min-Heap: `[1, 4, 6]`.
  2. Track the range using the minimum and maximum elements, adjusting as needed.
- **Visualization**:
  ```
  Step 1: Min-Heap = [1, 4, 6] -> Range = [1, 6]
  Step 2: Extract 1, Add 3 -> Min-Heap = [3, 4, 6] -> Range = [3, 6]
  ...
  Smallest Range = [4, 6]
  ```
- **Python Code**:
  ```python
  # Use Min-Heap to track range covering all elements
  def smallest_number_range(arrays):
      min_heap = []
      current_max = float('-inf')
  
      for i, array in enumerate(arrays):
          if array:
              heappush(min_heap, (array[0], i, 0))
              current_max = max(current_max, array[0])
  
      range_start, range_end = 0, float