# **Merge Intervals: Comprehensive Guide**

The Merge Intervals pattern is a fundamental technique for dealing with overlapping intervals in a variety of scenarios. It is commonly used in scheduling problems, merging time slots, and finding the union of ranges. This pattern ensures that overlapping ranges are consolidated into non-overlapping intervals, making it an essential tool in interval-based problem solving.

## 1. Core Concepts and Coding Patterns

The **Merge Intervals** pattern is used to deal with overlapping intervals. The fundamental idea is to **sort the intervals** based on the starting point, then iterate over the sorted list to merge overlapping intervals. This approach ensures that all overlapping ranges are consolidated into one, resulting in a set of non-overlapping intervals.

**Typical Use Cases**:

- Merging overlapping meeting times
- Identifying free time slots from a schedule
- Finding union of time-based data

## 2. Example

This example demonstrates how to apply the Merge Intervals pattern to combine overlapping intervals into a set of non-overlapping intervals. It illustrates the steps of sorting the intervals and merging them as needed. Given a set of intervals, such as: **[[1, 3], [2, 6], [8, 10], [15, 18]]**

- **Step 1**: Sort intervals by starting value: **[[1, 3], [2, 6], [8, 10], [15, 18]]**
- **Step 2**: Iterate through intervals:
  - Merge **[1, 3]** and **[2, 6]** into **[1, 6]**.
  - No overlap between **[1, 6]** and **[8, 10]**.
  - No overlap between **[8, 10]** and **[15, 18]**.
- **Result**: **[[1, 6], [8, 10], [15, 18]]**

### 3. Problem Identification Checklist

To identify problems suitable for the Merge Intervals pattern, look for:

- **Intervals that need to be combined** due to overlaps.
- **Union or scheduling problems**.
- **Range-based operations** such as finding free slots or removing overlaps.

| Problem                        | Indicators                                       |
| ------------------------------ | ------------------------------------------------ |
| Merge overlapping time slots   | Intervals with start and end times that overlap. |
| Consolidate free meeting slots | Given busy times, determine free intervals.      |

### 4. General Templates with Comments

#### Template 1: Basic Merge Intervals

```python
from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    # Step 1: Sort the intervals by the starting value
    intervals.sort(key=lambda x: x[0])
    merged = []

    # Step 2: Iterate through each interval
    for interval in intervals:
        # If the merged list is empty or current interval does not overlap
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)  # No overlap, add the interval
        else:
            # Overlapping intervals, merge them
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
```

**Use Case**: This template is applicable to any problem where the goal is to **merge overlapping intervals**, such as scheduling.

**Time Complexity**: **O(N log N)** due to sorting, where **N** is the number of intervals.

**Space Complexity**: **O(N)** for the output list.

### 5. Complexity Analysis

- **Time Complexity**: Sorting takes **O(N log N)**, and merging takes **O(N)**, resulting in **O(N log N)** overall.
- **Space Complexity**: Since we use extra space for the merged output, the space complexity is **O(N)**.
- **Optimization Opportunities**: Use in-place merging where applicable to save space.

### 6. Discussion on Templates and Patterns

The basic template works well for a variety of merging tasks, but adjustments may be needed depending on **additional constraints** (e.g., finding the gaps between merged intervals).

### 7. Multiple Approaches and Implementations

#### Iterative vs. Recursive

- **Iterative**: The above template is iterative, providing a straightforward way to merge intervals.
- **Recursive**: A recursive approach is possible but usually results in higher space complexity due to function call stacks.

```python
from typing import List

def merge_intervals_recursive(intervals: List[List[int]], index: int = 0) -> List[List[int]]:
    if index == len(intervals) - 1:
        return [intervals[index]]
    
    # Recursive call to merge the remaining intervals
    merged_intervals = merge_intervals_recursive(intervals, index + 1)
    current_interval = intervals[index]
    
    # If there is overlap, merge the current interval with the first in merged_intervals
    if merged_intervals and current_interval[1] >= merged_intervals[0][0]:
        merged_intervals[0] = [
            min(current_interval[0], merged_intervals[0][0]),
            max(current_interval[1], merged_intervals[0][1])
        ]
    else:
        merged_intervals.insert(0, current_interval)
    
    return merged_intervals
```

#### Iterative vs. Recursive

- **Iterative**: The above template is iterative, providing a straightforward way to merge intervals.
- **Recursive**: A recursive approach is possible but usually results in higher space complexity due to function call stacks.

### 8. Comparative Analysis

| Approach  | Advantages             | Disadvantages                            |
| --------- | ---------------------- | ---------------------------------------- |
| Iterative | Simple, more efficient | Can be verbose in edge cases             |
| Recursive | Elegant in theory      | Higher space complexity, harder to debug |

### 9. Practice Problems

| S.No | Question                                   | Example (detailed explanation with numeric details and output)                                                                                                                                                                                                                                            | Difficulty Level | Approach                                                                                                                                                                                                               |
| ---- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Merge overlapping intervals                | Given intervals [[1, 4], [2, 5]], the intervals overlap as 2 is within [1, 4]. Hence, we merge them into [1, 5]. The output is [[1, 5]].                                                                                                                                                                  | Easy             | Basic Merge Intervals Template. Sort the intervals, iterate through them, and merge overlapping ones using a merged list. No extra variables are required beyond the merged list.                                      |
| 2    | Find free time slots                       | Given busy time intervals [[1, 3], [6, 9]], the free time slot between them is from 3 to 6. Thus, the output is [[3, 6]].                                                                                                                                                                                 | Medium           | Modified Merge Intervals Template. Sort intervals and find gaps between them. Use additional variables to track previous interval end times.                                                                           |
| 3    | Insert interval                            | Given intervals [[1, 3], [6, 9]] and a new interval [2, 5], we insert [2, 5] and merge it with [1, 3] resulting in [1, 5]. The output is [[1, 5], [6, 9]].                                                                                                                                                | Medium           | Insert and Merge Pattern. Insert the interval into the correct position, then apply the Merge Intervals Template. Use extra variables for insertion index and merged result tracking.                                  |
| 4    | Employee free time                         | Given busy schedules [[1, 3], [5, 6]] and [[2, 3], [6, 8]], the free time available for all employees is from 3 to 5. Thus, the output is [[3, 5]].                                                                                                                                                       | Hard             | Merge Intervals followed by Gap Identification. First, merge all intervals, then iterate to find gaps. Use extra variables to store merged results and track free time intervals.                                      |
| 5    | Interval list intersections                | Given two lists of intervals [[1, 3], [5, 9]] and [[2, 5], [7, 10]], the intersections are [2, 3], [5, 5], and [7, 9]. Thus, the output is [[2, 3], [5, 5], [7, 9]].                                                                                                                                      | Medium           | Two Pointers Approach. Traverse both interval lists simultaneously using pointers, and find overlapping sections. Use two pointers to track current intervals in both lists.                                           |
| 6    | Meeting rooms II                           | Given meeting intervals [[0, 30], [5, 10], [15, 20]], we need to find the minimum number of meeting rooms required. The result is 2 because the intervals overlap such that two rooms are required at most.                                                                                               | Medium           | Heap / Priority Queue Pattern. Use a min-heap to keep track of ongoing meetings and determine room requirements. Extra variables include a heap for meeting end times.                                                 |
| 7    | Minimum number of arrows to burst balloons | Given intervals representing the range of balloons [[10, 16], [2, 8], [1, 6], [7, 12]], the minimum number of arrows required to burst all the balloons is 2, as some of the ranges overlap and can be burst with the same arrow.                                                                         | Medium           | Basic Merge Intervals Template. Sort intervals by their end points, then iterate through to determine the number of non-overlapping groups. Extra variable for counting arrows.                                        |
| 8    | Merge k sorted interval lists              | Given k sorted lists of intervals [[[1, 4], [7, 10]], [[3, 5], [8, 12]]], the merged result is [[1, 5], [7, 12]]. This is done by merging overlapping intervals across all lists.                                                                                                                         | Hard             | Merge Intervals with Min-Heap. Use a heap to efficiently track the smallest current interval across k lists. Extra variable for heap structure to maintain sorted order.                                               |
| 9    | Remove covered intervals                   | Given intervals [[1, 4], [3, 6], [2, 8]], we need to remove intervals that are covered by others. In this case, [1, 4] and [3, 6] are covered by [2, 8], so the output is [[2, 8]].                                                                                                                       | Medium           | Sort Intervals by Start and Length, then iterate to identify covered intervals. Use an extra variable to track the maximum end encountered so far.                                                                     |
| 10   | Car pooling                                | Given trip requests [[2, 1, 5], [3, 3, 7]], where each trip is represented as [num\_passengers, start\_location, end\_location], we need to determine if it is possible to pick up and drop off all passengers with the given capacity. The output is False as the car capacity is exceeded at one point. | Medium           | Sweep Line Algorithm. Use events for start and end points of trips, and calculate the number of passengers at each point. Extra variables for storing events and passenger counts.                                     |
| 11   | Add bold tag in string                     | Given string "abcxyz123" and intervals [[1, 3], [2, 4]], we need to add bold tags around the specified intervals. After merging overlapping intervals, the output string is "abcxyz123".                                                                                                                  | Medium           | Merge Intervals Template. First merge the overlapping intervals, then use the merged intervals to add the bold tags. Extra variable for storing the merged intervals and applying the bold tags in the string.         |
| 12   | Split intervals to avoid overlaps          | Given intervals [[1, 5], [2, 3], [4, 6]], we need to determine the minimum number of intervals to remove to avoid any overlaps. The output is 2, as removing [2, 3] and [4, 6] avoids overlaps.                                                                                                           | Hard             | Greedy Approach. Sort intervals by end time, and iterate to find the minimum number of intervals to remove. Use an extra variable to keep track of the last non-overlapping interval's end time.                       |
| 13   | Maximum CPU load                           | Given tasks represented by intervals with CPU load [[1, 4, 3], [2, 5, 4], [7, 9, 6]], the maximum CPU load at any point in time is 7. This is found by summing the overlapping intervals' loads.                                                                                                          | Hard             | Sweep Line + Heap. Use a sweep line approach to add and remove CPU loads as intervals start and end. Use a heap to efficiently keep track of the current loads. Extra variables for tracking load events and the heap. |
| 14   | Count of range sums                        | Given an array [-2, 5, -1] and a range [0, 2], we need to find the count of range sums that lie in the given range. The result is 3, as three subarrays have sums within this range.                                                                                                                      | Hard             | Divide and Conquer. Split the array and count the range sums in each part, then combine results. Extra variables for storing temporary sums during merge steps.                                                        |
| 15   | Range addition                             | Given operations [[1, 3, 2], [2, 4, 3], [0, 2, -2]], we need to apply the additions to an initial array of zeros. The result after applying all operations is [2, 3, 1, 3, -2].                                                                                                                           | Medium           | Difference Array Technique. Use a difference array to efficiently apply range updates, then compute the final values. Extra variable for storing the difference array before applying the prefix sum.                  |
| 16   | Maximum intervals overlap                  | Given intervals [[1, 5], [2, 6], [3, 7], [10, 15]], the maximum number of overlapping intervals is 3, occurring between times 3 and 5.                                                                                                                                                                    | Medium           | Sweep Line Approach. Use start and end events to determine the number of overlapping intervals at any time. Extra variables for tracking events and maintaining the count of current overlaps.                         |
| 17   | Merge strings                              | Given two strings "abc" and "def", the result of merging them is "abcdef".                                                                                                                                                                                                                                | Easy             | Simple String Concatenation. Directly concatenate both strings without any additional variables.                                                                                                                       |
| 18   | Find the intersection of two intervals     | Given intervals [1, 5] and [4, 8], the intersection is [4, 5], where the two intervals overlap.                                                                                                                                                                                                           | Easy             | Basic Interval Intersection. Compare the start and end points of the two intervals to find their intersection. No extra variables required.                                                                            |
| 19   | Partition labels                           | Given string "ababcbacadefegdehijhklij", we need to partition the string into as many parts as possible so that each letter appears in at most one part. The output partitions are [9, 7, 8].                                                                                                             | Medium           | Greedy + HashMap. Track the last occurrence of each character and partition greedily based on this information. Extra variable for storing the last occurrence index of each character.                                |
| 20   | Non-overlapping intervals                  | Given intervals [[1, 2], [2, 3], [3, 4], [1, 3]], we need to remove the minimum number of intervals to make the rest non-overlapping. The output is 1, as removing [1, 3] achieves this.                                                                                                                  | Medium           | Greedy Approach. Sort by end time and iterate to determine the maximum number of non-overlapping intervals. Use an extra variable to track the end time of the last added interval.                                    |

### 10. Key Takeaways, Tips, and Summary

- **Key Takeaways**: Always **sort** intervals first to simplify merging.
- **Practical Tips**: For complex merging, use a **stack** or **linked list** to keep track of merged intervals. For example, a stack can be particularly useful when you need to compare the latest merged interval with the next incoming interval, allowing you to backtrack easily when overlaps occur.
- **Summary**: Merge Intervals is a versatile pattern for solving interval-based problems.

### 11. Common Pitfalls

- **Mistake**: Forgetting to **sort** the intervals.
- **Troubleshooting Tips**: Always check the **boundary conditions** for each interval (start and end values).

Sure! Here are detailed explanations of 5 randomly selected practice problems along with examples, visualizations, and Python code comments:

### 1. **Merge Overlapping Intervals**
**Problem**: Given a list of intervals, merge all overlapping intervals.

**Example**:
- Input: `[[1, 4], [2, 5], [7, 9]]`
- Explanation:
  - Interval `[1, 4]` overlaps with `[2, 5]`. Therefore, we merge them to get `[1, 5]`.
  - `[1, 5]` does not overlap with `[7, 9]`.
  - Final output: `[[1, 5], [7, 9]]`.

**Visualization**:
```
   [1, 4]
      [2, 5]
           [7, 9]
After merging: [1, 5], [7, 9]
```

**Python Code**:
```python
from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = []
    
    for interval in intervals:
        # If no overlap, add the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge overlapping intervals
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example usage
print(merge_intervals([[1, 4], [2, 5], [7, 9]]))  # Output: [[1, 5], [7, 9]]
```

### 2. **Find Free Time Slots**
**Problem**: Given busy intervals of multiple employees, find the common free time slots.

**Example**:
- Input: `[[1, 3], [6, 9]], [[2, 4], [7, 10]]`
- Explanation:
  - Merge busy slots to get `[[1, 4], [6, 10]]`.
  - Free time slot is between `4` and `6`.
  - Output: `[[4, 6]]`.

**Visualization**:
```
Employee 1: [1, 3],       [6, 9]
Employee 2:    [2, 4],        [7, 10]
Merged:     [1, 4],       [6, 10]
Free Slot:              [4, 6]
```

**Python Code**:
```python
def find_free_time(intervals: List[List[int]]) -> List[List[int]]:
    # Step 1: Flatten all intervals
    all_intervals = [interval for sublist in intervals for interval in sublist]
    all_intervals.sort(key=lambda x: x[0])
    
    # Step 2: Merge busy intervals
    merged = []
    for interval in all_intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    # Step 3: Find free slots
    free_time = []
    for i in range(1, len(merged)):
        free_time.append([merged[i-1][1], merged[i][0]])
    
    return free_time

# Example usage
print(find_free_time([[[1, 3], [6, 9]], [[2, 4], [7, 10]]]))  # Output: [[4, 6]]
```

### 3. **Minimum Number of Arrows to Burst Balloons**
**Problem**: Given a set of balloons represented as intervals, find the minimum number of arrows needed to burst all balloons.

**Example**:
- Input: `[[10, 16], [2, 8], [1, 6], [7, 12]]`
- Explanation:
  - Sort by end points: `[[1, 6], [2, 8], [7, 12], [10, 16]]`.
  - Use one arrow for `[1, 8]`, which bursts the first two intervals.
  - Use a second arrow for `[7, 16]` to burst the rest.
  - Output: `2`.

**Visualization**:
```
Balloon ranges: [1, 6], [2, 8], [7, 12], [10, 16]
First Arrow: [1, 8]
Second Arrow:       [7, 16]
```

**Python Code**:
```python
def min_arrows_to_burst_balloons(intervals: List[List[int]]) -> int:
    # Sort intervals by their end points
    intervals.sort(key=lambda x: x[1])
    arrows = 1
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] > end:
            arrows += 1
            end = intervals[i][1]
    
    return arrows

# Example usage
print(min_arrows_to_burst_balloons([[10, 16], [2, 8], [1, 6], [7, 12]]))  # Output: 2
```

### 4. **Meeting Rooms II**
**Problem**: Find the minimum number of meeting rooms required.

**Example**:
- Input: `[[0, 30], [5, 10], [15, 20]]`
- Explanation:
  - Meeting `[0, 30]` overlaps with `[5, 10]` and `[15, 20]`.
  - The maximum number of overlapping meetings at any point is `2`.
  - Output: `2`.

**Visualization**:
```
Meetings: [0, 30]
           [5, 10]
                  [15, 20]
Overlaps: Two rooms are required simultaneously.
```

**Python Code**:
```python
import heapq

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    
    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Use a min-heap to track end times of meetings
    heap = []
    heapq.heappush(heap, intervals[0][1])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])
    
    return len(heap)

# Example usage
print(min_meeting_rooms([[0, 30], [5, 10], [15, 20]]))  # Output: 2
```

### 5. **Car Pooling**
**Problem**: Given trip requests as `[num_passengers, start_location, end_location]`, determine if the car capacity is enough.

**Example**:
- Input: `[[2, 1, 5], [3, 3, 7]]`, capacity = 4
- Explanation:
  - At time `1-5`, there are `2` passengers.
  - At time `3-7`, `3` additional passengers are picked up, making a total of `5`.
  - Since `5 > 4`, output is `False`.

**Visualization**:
```
Time: 1---5---7
Passengers: 2 at [1, 5], additional 3 at [3, 7]
Capacity Exceeded: 5 > 4
```

**Python Code**:
```python
def car_pooling(trips: List[List[int]], capacity: int) -> bool:
    events = []
    for trip in trips:
        events.append((trip[1], trip[0]))  # Start of the trip
        events.append((trip[2], -trip[0])) # End of the trip
    
    events.sort()
    current_passengers = 0
    
    for _, passengers in events:
        current_passengers += passengers
        if current_passengers > capacity:
            return False
    
    return True

# Example usage
print(car_pooling([[2, 1, 5], [3, 3, 7]], 4))  # Output: False
```

These detailed examples demonstrate how the Merge Intervals pattern and related approaches can solve real-world problems effectively.