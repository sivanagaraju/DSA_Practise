# Modified Binary Search: Comprehensive Guide

## 1. Core Concepts and Coding Patterns

Modified Binary Search is a variation of the standard binary search that allows us to solve a variety of problems beyond simple element searches. It retains the key concept of binary search—using a divide-and-conquer approach to achieve logarithmic time complexity—but adds specific modifications to fit different types of problems. Modified Binary Search is particularly effective in problems involving finding elements in sorted arrays, searching ranges, or optimizing values.

### Typical Use Cases

- Finding the position of an element in sorted but rotated arrays.
- Determining boundaries like the first or last occurrence of an element.
- Solving optimization problems involving sorted data.

### How It Works

The algorithm keeps dividing the search space in half until the desired element or condition is found. Depending on the problem requirements, you may add logic to determine the left or right boundary, or handle cyclic sorted arrays.

## 2. Examples

1. **Finding First and Last Position of a Target Element**

   - Given an array: `[1, 2, 2, 2, 3, 4, 5]` and target `2`, the Modified Binary Search can be used to find that the first position of `2` is `1` and the last position is `3`.
   - **Explanation**: Start with `left = 0` and `right = 6`. Calculate `mid` each time, and adjust `left` or `right` based on whether you are searching for the first or last occurrence. For the first occurrence, adjust `right` when `target` is found; for the last occurrence, adjust `left`. The final result is `1` for the first occurrence and `3` for the last occurrence.
2. **Searching in a Rotated Array**

   - Given a sorted and rotated array: `[4, 5, 6, 7, 0, 1, 2]`, target `0`, the Modified Binary Search can find the position of `0` as `4`.
   - **Explanation**: Start with `left = 0` and `right = 6`. Calculate `mid` and determine which half is sorted. Adjust `left` or `right` based on which side of the array the target lies. Eventually, the target `0` is found at index `4`.

## 3. Problem Identification Checklist

| Scenario                                  | Example Problem                               | Use Modified Binary Search When |
| ----------------------------------------- | --------------------------------------------- | ------------------------------- |
| Array is sorted or partially sorted       | Finding an element in a sorted rotated array  | Yes                             |
| Need to find boundaries                   | Find first and last occurrence of a target    | Yes                             |
| Problem involves a condition with min/max | Finding the minimum in a rotated sorted array | Yes                             |

## 4. General Templates with Comments

### Template 1: Basic Modified Binary Search

```python
# Generalized binary search template for a wide range of problems
# This template can be used for different conditions by modifying the "condition" function

def binary_search(array, condition) -> int:
    # Define the initial search space
    left, right = 0, len(array) - 1  # or a range based on the problem, e.g., [0, max(array)]
  
    # Loop until the search space is exhausted
    while left <= right:
        mid = left + (right - left) // 2  # Prevent potential overflow in other languages
      
        # Check if the mid value meets the desired condition
        if condition(mid):  # This "condition" function should be problem-specific
            right = mid - 1  # Narrow down the search space to the left half
        else:
            left = mid + 1  # Narrow down the search space to the right half
  
    # When left > right, the loop exits, return the relevant index/value based on the problem
    return left

# Example usage:
# Suppose we want to find the smallest index at which the value is greater than a target
array = [1, 3, 5, 7, 9, 11]
target = 6

def condition_example(index) -> bool:
    return array[index] > target

result = binary_search(array, condition_example)
print(result)  # Output will be the index where the value is greater than the target
```

**Explanation:**

* This generalized template is useful when you want to search for an optimal value that meets a certain condition.
* You start by defining the left and right boundary based on the problem's context, which can vary.
* The condition(mid) function is a placeholder for the logic to determine if the current mid value meets the criteria of the problem.
* Depending on the result of condition(mid), you adjust either the left or right pointer to narrow down the search space.

### Template 2: Find First or Last Occurrence

```python
# Template for finding the first or last occurrence of a target element
def find_boundary(arr, target, find_first=True):
    left, right = 0, len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            boundary_index = mid
            # Adjust search based on whether we're finding the first or last occurrence
            if find_first:
                right = mid - 1  # Extra logic: move left to find the first occurrence
            else:
                left = mid + 1  # Extra logic: move right to find the last occurrence
        elif arr[mid] < target:
            left = mid + 1  # Move right if target is greater
        else:
            right = mid - 1  # Move left if target is smaller
    return boundary_index
```

### Use Cases

- **Basic Template**: Used for standard element searches in sorted or rotated arrays.
- **Boundary Template**: Ideal for finding first/last occurrence or boundaries of elements.

## 5. Complexity Analysis

- **Time Complexity**: Each variation of Modified Binary Search runs in `O(log n)` time since the search space is halved in each iteration.
- **Space Complexity**: Typically `O(1)` as only a fixed amount of additional space is used.
- **Optimization Opportunities**: Reuse existing binary search templates to create hybrid solutions for more complex scenarios, like peak finding.

## 6. Discussion on Templates and Patterns

Modified Binary Search patterns are versatile and can be adjusted for a wide range of problems. For example, the condition to determine which side of the array to continue searching can be altered to work in rotated or duplicated-element arrays.

## 7. Multiple Approaches and Implementations

- **Iterative vs Recursive**: An iterative approach is usually preferred for binary search due to lower space usage (`O(1)` stack space). Recursive solutions work but may involve extra stack space (`O(log n)`).
- **Comparative Analysis**: Iterative approaches have advantages in performance due to reduced recursion overhead.

## 8. Practice Problems

| S.No | Question                                    | Example & Output                                                                                                                                                                                                                                         | Difficulty Level | Approach                                                                                                                                                                                     |
| ---- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Find Element in Rotated Sorted Array        | Array `[4, 5, 6, 7, 0, 1, 2]`, Target `0` → Start with `left = 0`, `right = 6`, find `mid = 3` (`arr[mid] = 7`). Since the right half is sorted, adjust `left`. Eventually, `target` is found at index `4`. Output: `4`             | Medium           | Rotated Binary Search. Template: Basic Modified Binary Search. Extra variables:`left`, `right`, `mid`. Logic: Adjust `left` or `right` depending on sorted half.                   |
| 2    | First and Last Position of Element in Array | Array `[5, 7, 7, 8, 8, 10]`, Target `8` → Start with `left = 0`, `right = 5`. First occurrence: adjust `right` when `target` is found. Last occurrence: adjust `left`. First occurrence is at `3` and last at `4`. Output: `[3, 4]` | Medium           | Boundary Search Template. Template: Find First or Last Occurrence. Extra variables:`left`, `right`, `mid`, `boundary_index`. Logic: Adjust `left` or `right` to find boundaries. |
| 3    | Find Peak Element                           | Array `[1, 2, 3, 1]` → Start with `left = 0`, `right = 3`, find `mid = 1` (`arr[mid] = 2`). Move towards the side where elements are increasing to find the peak. Peak is found at index `2`. Output: `2` (index of peak)                 | Medium           | Peak Finding via Binary Search. Template: Basic Modified Binary Search. Extra variables:`left`, `right`, `mid`. Logic: Move towards increasing side to find peak.                      |
| 4    | Find Minimum in Rotated Sorted Array        | Array `[3, 4, 5, 1, 2]` → Start with `left = 0`, `right = 4`. Keep finding `mid` and adjusting `left` or `right` based on the sorted half until the minimum (`1`) is found at index `3`. Output: `3`                                  | Medium           | Rotated Binary Search. Template: Basic Modified Binary Search. Extra variables:`left`, `right`, `mid`. Logic: Adjust `left` or `right` based on sorted half.                       |
| 5    | Search Insert Position                      | Array `[1, 3, 5, 6]`, Target `5` → Use binary search to find where the target fits. Target `5` is found at index `2`. Output: `2`                                                                                                             | Easy             | Basic Binary Search. Template: Basic Modified Binary Search. Extra variables:`left`, `right`, `mid`. Logic: Find the correct position for insertion.                                   |
| 6    | Find Single Element in Sorted Array         | Array `[1, 1, 2, 3, 3, 4, 4, 8, 8]` → Use binary search to find the unique element (`2`). Start with `left = 0`, `right = 8`. Output: `2`                                                                                                     | Medium           | Modified Binary Search. Template: Basic Modified Binary Search. Extra variables:`left`, `right`, `mid`. Logic: Use conditions to find the non-repeating element.                       |
| 7    | Find Closest Element                        | Array `[1, 3, 8, 10, 15]`, Target `12` → Use binary search to find closest value (`10`). Output: `10`                                                                                                                                           | Medium           | Closest Search Template. Template: Basic Modified Binary Search. Extra variables:`closest`. Logic: Track closest value during search.                                                      |
| 8    | Find Range Sum Query                        | Array `[2, 4, 6, 8, 10]`, Query `(1, 3)` → Use binary search for prefix sums. Sum between indices `1` and `3` is `4 + 6 + 8 = 18`. Output: `18`                                                                                             | Medium           | Prefix Sum + Binary Search. Template: Prefix Sum Calculation. Extra variables:`prefix_sums`. Logic: Use prefix sums and binary search to answer range queries.                             |
| 9    | Find Bitonic Peak                           | Array `[1, 3, 8, 12, 4, 2]` → Use binary search to find peak (`12`). Peak found at index `3`. Output: `3`                                                                                                                                       | Medium           | Bitonic Search Template. Template: Basic Modified Binary Search. Extra variables:`left`, `right`, `mid`. Logic: Move in the direction of increasing elements.                          |
| 10   | Search in 2D Matrix                         | Matrix `[[1, 3, 5], [7, 9, 11], [13, 15, 17]]`, Target `9` → Use binary search to find element (`9`). Found at `(1, 1)`. Output: `(1, 1)`                                                                                                     | Medium           | 2D Binary Search. Template: Flattened Binary Search. Extra variables:`rows`, `cols`, `mid_value`. Logic: Treat 2D matrix as flattened 1D array during search.                          |
| 11   | Kth Smallest Element in Sorted Matrix       | Matrix `[[1, 5, 9], [10, 11, 13], [12, 13, 15]]`, `k = 8` → Use binary search to find the `8th` smallest (`13`). Output: `13`                                                                                                                 | Hard             | Matrix Binary Search. Template: Basic Modified Binary Search. Extra variables:`left`, `right`, `mid`. Logic: Apply binary search on matrix values.                                     |
| 12   | Find Smallest Missing Positive Number       | Array `[0, 1, 2, 6, 9, 11, 15]` → Find smallest missing positive (`3`). Output: `3`                                                                                                                                                               | Medium           | Missing Value Search. Template: Basic Modified Binary Search. Extra variables:`left`, `right`, `mid`. Logic: Use binary conditions to locate missing value.                            |
| 13   | Count Occurrences of Element                | Array `[2, 4, 10, 10, 10, 18, 20]`, Target `10` → Use boundary search to find occurrences (`3`). Output: `3`                                                                                                                                    | Easy             | Boundary Search Template. Template: Find First or Last Occurrence. Extra variables:`left`, `right`, `mid`, `boundary_index`. Logic: Adjust `left` and `right` to find the count. |
| 14   | Search in Infinite Sorted Array             | Array `[1, 2, 3, ...]` (infinite), Target `10` → Find bounds and use binary search. Output: `10`                                                                                                                                                  | Medium           | Infinite Array Search. Template: Boundary Expansion. Extra variables:`bound`. Logic: Expand bounds until target is within range, then perform binary search.                               |
| 15   | Split Array Largest Sum                     | Array `[7, 2, 5, 10, 8]`, `m = 2` → Use binary search to split and minimize largest sum (`18`). Output: `18`                                                                                                                                    | Hard             | Array Split Search. Template: Binary Search on Answer. Extra variables:`left`, `right`, `mid`. Logic: Minimize the largest subarray sum.                                               |
| 16   | Aggressive Cows                             | Positions `[1, 2, 8, 4, 9]`, `cows = 3` → Use binary search to maximize distance (`3`). Output: `3`                                                                                                                                             | Hard             | Distance Maximization. Template: Binary Search on Distance. Extra variables:`left`, `right`, `mid`. Logic: Place cows to maximize the minimum distance.                                |
| 17   | Allocate Minimum Pages                      | Books `[12, 34, 67, 90]`, `students = 2` → Use binary search to allocate books (`113`). Output: `113`                                                                                                                                           | Medium           | Page Allocation Search. Template: Binary Search on Answer. Extra variables:`left`, `right`, `mid`. Logic: Minimize the maximum pages allocated to any student.                         |
| 18   | Median of Two Sorted Arrays                 | Arrays `[1, 3]` and `[2]` → Use binary search to find median (`2`). Output: `2`                                                                                                                                                                 | Hard             | Median Finding Template. Template: Binary Search with Partition. Extra variables:`A`, `B`, `i`, `j`. Logic: Partition arrays and adjust search to find the median.                   |
| 19   | Capacity to Ship Packages                   | Weights `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, `days = 5` → Use binary search to minimize capacity (`15`). Output: `15`                                                                                                                             | Medium           | Shipping Capacity Search. Template: Binary Search on Answer. Extra variables:`left`, `right`, `mid`. Logic: Minimize the ship's weight capacity needed to meet the deadline.           |
| 20   | Minimize Max Distance to Gas Station        | Stations `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, `k = 9` → Use binary search to minimize maximum distance (`0.5`). Output: `0.5`                                                                                                                     | Hard             | Distance Minimization. Template: Binary Search on Distance. Extra variables:`left`, `right`, `mid`. Logic: Place additional stations to minimize the maximum distance.                 |

## 9. Key Takeaways, Tips, and Summary

- **Key Takeaways**: Modified Binary Search allows flexibility for a variety of problems, not just basic element search. Templates can be easily adapted.
- **Practical Tips**: Determine if the array is sorted or has properties that allow binary search optimization.
- **Summary**: By understanding and practicing different binary search templates, you can solve many complex problems efficiently.

## 10. Common Pitfalls

- **Mistakes to Avoid**: Misplacing conditions or improperly calculating mid (risk of overflow).
- **Troubleshooting Tips**: Always check boundary conditions and make sure your left and right pointers are correctly adjusted.

Here are detailed explanations for 10 randomly selected practice problems from the list:

### 1. Find Element in Rotated Sorted Array

**Problem**: Given a rotated sorted array `[4, 5, 6, 7, 0, 1, 2]`, find the target element `0`.

**Explanation**:

- Start with `left = 0` and `right = 6`.
- Calculate `mid = (0 + 6) // 2 = 3`. `arr[mid] = 7`.
- Since the right half (`0, 1, 2`) is sorted and the target lies within it, adjust `left` to `mid + 1`.
- Continue searching until you find `target` at index `4`.

```python
# Rotated Binary Search to find target in rotated sorted array
def search_rotated_array(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

### 2. First and Last Position of Element in Array

**Problem**: Find the first and last position of `8` in array `[5, 7, 7, 8, 8, 10]`.

**Explanation**:

- First, use a modified binary search to find the first occurrence (`left = 0`, `right = 5`).
- Then use a similar approach to find the last occurrence.
- The first occurrence is at index `3` and the last occurrence is at index `4`.

```python
# Find first and last occurrence of target in array
def find_first_last(arr, target):
    def find_boundary(find_first):
        left, right, boundary_index = 0, len(arr) - 1, -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                boundary_index = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return boundary_index

    return [find_boundary(True), find_boundary(False)]
```

### 3. Find Peak Element

**Problem**: Given an array `[1, 2, 3, 1]`, find the peak element.

**Explanation**:

- A peak element is greater than its neighbors.
- Start with `left = 0` and `right = 3`.
- Move towards the direction where elements are increasing until you find the peak at index `2`.

```python


# Find peak element in the array
def find_peak(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left



```

### 4. Find Minimum in Rotated Sorted Array

**Problem**: Given a rotated sorted array `[3, 4, 5, 1, 2]`, find the minimum.

**Explanation**:

- The minimum element is the pivot point of rotation.
- Start with `left = 0` and `right = 4`, keep finding `mid` and adjusting `left` or `right`.
- Minimum (`1`) is found at index `3`.

```python
# Find minimum element in rotated sorted array
def find_minimum_rotated(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return arr[left]
```

### 5. Search Insert Position

**Problem**: Find the insert position of `5` in `[1, 3, 5, 6]`.

**Explanation**:

- Use binary search to find where the target fits.
- The target `5` is already present at index `2`.

```python
# Search insert position for target
def search_insert_position(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
```

### 6. Find Single Element in Sorted Array

**Problem**: Find the unique element in `[1, 1, 2, 3, 3, 4, 4, 8, 8]`.

**Explanation**:

- Use binary search to find the element that appears only once.
- Unique element (`2`) is found at index `2`.

```python
# Find single non-duplicate element
def find_single_element(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if mid % 2 == 1:
            mid -= 1
        if arr[mid] == arr[mid + 1]:
            left = mid + 2
        else:
            right = mid
    return arr[left]
```

### 7. Find Closest Element

**Problem**: Given array `[1, 3, 8, 10, 15]` and target `12`, find the closest element.

**Explanation**:

- Use binary search to find the closest value.
- Closest value to `12` is `10`.

```python
# Find closest element to target
def find_closest_element(arr, target):
    left, right = 0, len(arr) - 1
    closest = arr[0]
    while left <= right:
        mid = left + (right - left) // 2
        if abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return closest
```

### 8. Find Bitonic Peak

**Problem**: Given a bitonic array `[1, 3, 8, 12, 4, 2]`, find the peak.

**Explanation**:

- A bitonic array is first increasing, then decreasing.
- Use binary search to find the peak (`12` at index `3`).

```python
# Find peak element in a bitonic array
def find_bitonic_peak(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
```

### 9. Search in 2D Matrix

**Problem**: Given a matrix `[[1, 3, 5], [7, 9, 11], [13, 15, 17]]`, find target `9`.

**Explanation**:

- Use binary search on the 2D matrix by treating it as a flattened 1D array.
- Target `9` is found at position `(1, 1)`.

```python
# Search in 2D matrix
def search_2d_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = matrix[mid // cols][mid % cols]
        if mid_value == target:
            return (mid // cols, mid % cols)
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    return (-1, -1)
```

### 10. Median of Two Sorted Arrays

**Problem**: Given arrays `[1, 3]` and `[2]`, find the median.

**Explanation**:

- Merge the arrays virtually using binary search to find the median.
- The median is `2`.

```python
# Find median of two sorted arrays
def find_median_sorted_arrays(nums1, nums2):
    A, B = nums1, nums2
    if len(A) > len(B):
        A, B = B, A
    total = len(A) + len(B)
    half = total // 2

    left, right = 0, len(A) - 1
    while True:
        i = (left + right) // 2
        j = half - i - 2

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            right = i - 1
        else:
            left = i + 1
```
