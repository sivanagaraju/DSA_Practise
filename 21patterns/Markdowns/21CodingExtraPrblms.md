# TWO POINTER PROBLEMS

### **Problem 2: Remove Duplicates from a Sorted Array In-Place**

**Problem Statement:**
Given a sorted array `arr`, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same, and it should be done in **O(1)** extra space. You must modify the input array in-place with the result being stored in the first part of the array, and return the length of the unique elements.

**Example:**

- **Input:** `[2, 3, 3, 3, 6, 9, 9]`
- **Explanation:**
  - The sorted input array has duplicates.
  - We need to modify the array in such a way that each unique element appears only once and the duplicates are removed.
  - Use two pointers:
    - One pointer (`i`) keeps track of where to place the next unique element.
    - Another pointer (`j`) iterates through the entire array.
  - After processing, the first `4` elements of the array will be `[2, 3, 6, 9]` representing unique values.
- **Output:** Length of unique elements = `4`

**Approach:**

- Use the **Two Pointers** technique:
  - The first pointer, `i`, keeps track of the index where the next unique element should be placed.
  - The second pointer, `j`, iterates through the array.
- Since the array is sorted, duplicates are always adjacent. As `j` iterates, if the element at `j` is different from the element at `i - 1`, we have found a new unique element, and we place it at index `i`.

**Python Code with Comments:**

```python
def remove_duplicates(arr):
    # If the array is empty, return 0
    if not arr:
        return 0

    # Initialize the unique element pointer
    i = 1

    # Iterate through the array starting from the second element
    for j in range(1, len(arr)):
        # If the current element is not equal to the previous element
        # It means we have found a unique element
        if arr[j] != arr[i - 1]:
            arr[i] = arr[j]  # Place the unique element at index 'i'
            i += 1           # Increment the unique index pointer

    # Return the length of unique elements
    return i

# Example usage
arr = [2, 3, 3, 3, 6, 9, 9]
length = remove_duplicates(arr)
print(f"Length of unique elements: {length}")  # Output: 4
print(f"Modified array (first {length} elements): {arr[:length]}")  # Output: [2, 3, 6, 9]
```

**Explanation of the Code:**

1. **Initialization:**

   - If the input array is empty, simply return `0`.
   - Start with `i = 1` as the pointer for placing the next unique element.
2. **Iteration Through the Array:**

   - Start iterating from index `1` using the `j` pointer.
   - Compare `arr[j]` with the element at `i - 1` (the last placed unique element).
   - If `arr[j]` is different from `arr[i - 1]`, it means that `arr[j]` is unique and should be placed at the current position of `i`.
   - After placing the unique element, increment `i` to point to the next position.
3. **Return Value:**

   - The value `i` represents the length of the array that contains unique elements.
   - The array itself is modified in-place, with the unique elements placed in the first `i` positions.

**Time Complexity:**

- **O(n)**, where `n` is the length of the array. We only iterate through the array once.

**Space Complexity:**

- **O(1)**, since we are modifying the array in place and not using any extra space.

**Summary**

- The **Two Pointers** technique is used effectively to remove duplicates from a sorted array in **O(n)** time and **O(1)** space.
- The `i` pointer keeps track of where to place the next unique element, while the `j` pointer iterates through the array.
- By keeping the original sorted order and modifying the array in place, this solution is both time and space efficient.

### **Problem 3: Triplet Sum to Zero**

**Problem Statement:**
Given an array of integers `arr`, find all unique triplets in the array which give the sum of zero. The solution set must not contain duplicate triplets.

**Example:**

- **Input:** `[-3, -1, 1, 2, -1, -4]`
- **Explanation:**
  - To find all unique triplets that add up to zero, sort the array first.
  - Iterate through the sorted array and use two pointers to find pairs that sum up with the current element to give zero.
  - Possible unique triplets: `[-3, 1, 2]` and `[-1, -1, 2]`.
- **Output:** `[[-3, 1, 2], [-1, -1, 2]]`

**Approach:**

- The **Two Pointers** technique is used in combination with sorting.
- **Steps:**
  1. **Sort the Array:** Sort the input array to make it easier to find unique combinations and avoid duplicates.
  2. **Fixed Pointer and Two Pointers:**
     - Iterate through the sorted array with a pointer `i`.
     - For each element at `i`, use two pointers (`left` and `right`) to find pairs whose sum is equal to the negative value of the current element (`-arr[i]`).
  3. **Avoid Duplicates:** Skip elements that are the same as the previous one to ensure each triplet is unique.

**Python Code with Comments:**

```python
def three_sum(arr):
    # Sort the array to make it easier to find unique combinations
    arr.sort()
    # List to store the unique triplets that sum to zero
    result = []

    # Iterate through the array, considering each element as a potential part of a triplet
    for i in range(len(arr) - 2):
        # Skip duplicate elements to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Set up two pointers: one starting just after 'i' and the other at the end of the array
        left, right = i + 1, len(arr) - 1

        # While 'left' is to the left of 'right', try to find a valid triplet
        while left < right:
            # Calculate the current sum of the triplet
            current_sum = arr[i] + arr[left] + arr[right]

            # If the current sum is zero, we found a triplet
            if current_sum == 0:
                result.append([arr[i], arr[left], arr[right]])

                # Move the left pointer to the right while skipping duplicates
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                # Move the right pointer to the left while skipping duplicates
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                # Move both pointers to continue finding other potential triplets
                left += 1
                right -= 1
            # If the current sum is less than zero, move the left pointer to increase the sum
            elif current_sum < 0:
                left += 1
            # If the current sum is greater than zero, move the right pointer to decrease the sum
            else:
                right -= 1

    # Return the list of unique triplets
    return result

# Example usage
arr = [-3, -1, 1, 2, -1, -4]
print(three_sum(arr))  # Output: [[-3, 1, 2], [-1, -1, 2]]
```

**Explanation of the Code:**

1. **Sorting the Array:**

   - The array is sorted to facilitate the use of two pointers and to make it easier to skip duplicate elements.
2. **Iterating with a Fixed Pointer:**

   - Use a for loop to iterate through the array, treating each element as a potential part of the triplet.
   - The index `i` represents the first element of the triplet.
3. **Two-Pointer Technique:**

   - For each element at index `i`, use two pointers:
     - **`left`** starts just after `i`.
     - **`right`** starts at the end of the array.
   - Move the `left` and `right` pointers to find pairs that, together with `arr[i]`, sum to zero.
4. **Handling Duplicates:**

   - Skip duplicate elements for `i`, `left`, and `right` to avoid generating duplicate triplets.

**Time Complexity:**

- Sorting the array takes **O(n log n)**.
- The two-pointer search for each element takes **O(n)**.
- Therefore, the overall complexity is **O(n^2)**.

**Space Complexity:**

- **O(1)**, not counting the space required for the output. No additional space is used apart from the input and output.

**Summary**

- The **Two Pointers** technique is combined with sorting to efficiently find triplets that sum to zero.
- The sorted array allows the use of two pointers (`left` and `right`) to find pairs that, together with the current element (`arr[i]`), form a triplet that sums to zero.
- Careful handling of **duplicates** is crucial to ensure that the solution set contains only unique triplets.

### **Problem 7: Sort Colors (Dutch National Flag Problem)**

**Problem Statement:**
Given an array `arr` with `n` objects colored red, white, or blue, represented by integers `0`, `1`, and `2`, respectively, sort them in-place so that objects of the same color are adjacent, with the colors in the order `red (0)`, `white (1)`, and `blue (2)`.

**Note:** You are not supposed to use the library's sort function for this problem. The idea is to use a single pass (O(n)) and in-place sorting (O(1) space).

**Example:**

- **Input:** `[2, 0, 2, 1, 1, 0]`
- **Explanation:**
  - Use the **Dutch National Flag algorithm**, which involves using three pointers (`low`, `mid`, `high`) to segregate the values in a single pass.
  - After processing, the array should be sorted as `[0, 0, 1, 1, 2, 2]`.
- **Output:** `[0, 0, 1, 1, 2, 2]`

**Approach:**

- Use three pointers:
  - **`low`**: Keeps track of the position where `0`s should be placed.
  - **`mid`**: Current element to be checked.
  - **`high`**: Keeps track of the position where `2`s should be placed.
- Initially, set `low = 0`, `mid = 0`, and `high = len(arr) - 1`.
- Iterate through the array until `mid` exceeds `high`:
  - If `arr[mid] == 0`: Swap `arr[low]` and `arr[mid]`, then increment both `low` and `mid`.
  - If `arr[mid] == 1`: Just increment `mid`.
  - If `arr[mid] == 2`: Swap `arr[mid]` and `arr[high]`, then decrement `high`.

**Python Code with Comments:**

```python
def sort_colors(arr):
    # Initialize three pointers: 'low', 'mid', and 'high'
    low, mid, high = 0, 0, len(arr) - 1

    # Iterate until 'mid' crosses 'high'
    while mid <= high:
        if arr[mid] == 0:
            # Swap the current element with the element at 'low'
            arr[low], arr[mid] = arr[mid], arr[low]
            # Increment both 'low' and 'mid' pointers
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # If the element is '1', move the 'mid' pointer forward
            mid += 1
        else:  # arr[mid] == 2
            # Swap the current element with the element at 'high'
            arr[mid], arr[high] = arr[high], arr[mid]
            # Decrement the 'high' pointer
            high -= 1

# Example usage
arr = [2, 0, 2, 1, 1, 0]
sort_colors(arr)
print(arr)  # Output: [0, 0, 1, 1, 2, 2]
```

**Explanation of the Code:**

1. **Initialization:**

   - Three pointers are used:
     - `low` (starting from `0`) tracks where the next `0` should be placed.
     - `mid` (starting from `0`) is used to iterate through the array.
     - `high` (starting from the last index) tracks where the next `2` should be placed.
2. **Iterate Through the Array:**

   - If `arr[mid] == 0`:
     - Swap the element at `mid` with the element at `low`.
     - This ensures that `0`s are moved to the beginning.
     - Increment both `low` and `mid`.
   - If `arr[mid] == 1`:
     - Simply move the `mid` pointer to the next element.
     - `1`s are already in the correct position.
   - If `arr[mid] == 2`:
     - Swap the element at `mid` with the element at `high`.
     - This ensures that `2`s are moved to the end.
     - Decrement `high`.
     - Note that after swapping, the `mid` pointer is **not incremented** because we need to recheck the new value at `mid` (since it was just swapped).

**Time Complexity:**

- **O(n)** where `n` is the length of the array. Each element is processed at most once.

**Space Complexity:**

- **O(1)** since no additional space is used other than the input array.

**Summary**

- The **Dutch National Flag Algorithm** is an efficient solution for this problem.
- By using three pointers (`low`, `mid`, `high`), the array is partitioned into three regions:
  - Elements less than `1` (`0`s) are placed at the beginning.
  - Elements equal to `1` are placed in the middle.
  - Elements greater than `1` (`2`s) are placed at the end.
- This approach runs in **O(n)** time and **O(1)** space, making it very efficient for in-place sorting.

# Fast and Slow Pointers

### Problem 3: Linked List Cycle Length

**Problem**: Given a linked list, find the length of the cycle (if it exists).

**Example**:

- **Input**: Linked list: 1 → 2 → 3 → 4 → 2 (Cycle starts at node with value `2`)
- **Output**: `3`
- **Explanation**: The linked list has a cycle starting at node `2` and the cycle length is `3`. The nodes forming the cycle are `2 → 3 → 4 → 2`. To determine the length, we can use the fast and slow pointers to detect the cycle and then determine its length by counting the nodes involved.

**Step-by-Step Solution**:

1. **Detect if a Cycle Exists**:

   - Use the Fast and Slow Pointers method to detect if a cycle is present.
   - The **slow pointer** moves one step at a time while the **fast pointer** moves two steps.
   - If there is a cycle, the fast and slow pointers will eventually meet.
2. **Determine the Length of the Cycle**:

   - Once a cycle is detected (both pointers meet at the same node), keep one pointer fixed and move the other until it meets the fixed pointer again.
   - Count the number of steps taken to determine the cycle length.

**Visualization**:

```
1 → 2 → 3 → 4
    ↑       ↓
    5 ←-----
```

In this example, the cycle is formed by nodes `2 → 3 → 4`, and the length of this cycle is `3`.

**Python Code with Detailed Comments**:

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def cycle_length(head):
    # Step 1: Detect if a cycle exists using slow and fast pointers
    slow, fast = head, head
  
    # Traverse the linked list
    while fast is not None and fast.next is not None:
        slow = slow.next           # Move slow pointer by one step
        fast = fast.next.next      # Move fast pointer by two steps

        # If slow and fast meet, a cycle is detected
        if slow == fast:
            return count_cycle_length(slow)  # Step 2: Calculate the cycle length
  
    return 0  # No cycle found

def count_cycle_length(meeting_node):
    # Start from the meeting node
    current = meeting_node
    length = 0
  
    # Traverse the cycle until we reach the starting point again
    while True:
        current = current.next  # Move to the next node in the cycle
        length += 1             # Increment the length count
        if current == meeting_node:  # If we are back at the start, stop
            break
  
    return length

# Example usage:
# Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle starts at 3)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next  # Create a cycle back to node 3

print(cycle_length(head))  # Output: 3
```

- **Time Complexity**:

  - **Cycle Detection**: The time complexity of detecting a cycle is **O(N)**, where **N** is the number of nodes in the linked list. This is because, in the worst case, we need to traverse the entire list until the fast pointer catches up to the slow pointer.
  - **Cycle Length Calculation**: Once the cycle is detected, the time complexity of counting the cycle length is **O(C)**, where **C** is the length of the cycle. In the worst case, **C** could be all the nodes in the list.
  - Therefore, the overall time complexity is **O(N)**.
- **Space Complexity**:

  - The space complexity is **O(1)** because we only use a constant amount of extra space (two pointers, `slow` and `fast`, and a few additional variables).

**Summary**

- **Fast and Slow Pointers** are used to detect a cycle.
- Once a cycle is detected, **counting the length** is done by fixing one pointer and moving another until it completes the cycle.
- The solution is efficient, requiring only **O(N)** time and **O(1)** space, making it suitable for large linked lists.

## Problem 5: Intersection of Two Linked Lists

**Problem**: Given two singly linked lists, determine if they intersect, and return the intersecting node. Intersection is defined based on reference, not value; if the same node is shared between the two linked lists, they intersect at that node.

**Example**:

- **Input**:
  - **List A**: `1 → 2 → 3 → 4 → 5`
  - **List B**: `9 → 4 → 5`
- **Output**: `Node with value 4`
- **Explanation**: Both lists intersect at the node with value `4`. This means they share the same reference from that point onward.

**Visualization**:

```
List A: 1 → 2 → 3 → 4 → 5
                      ↑
List B:         9 → 4
```

The lists intersect at node `4`.

**Approach to Solve the Problem**

1. **Two Pointers Technique**:
   - Use two pointers, one for each list (`pointerA` and `pointerB`).
   - Traverse each list simultaneously.
   - When a pointer reaches the end of its list, move it to the head of the other list.
   - If the lists intersect, the two pointers will meet at the intersection point after swapping heads once. If they do not intersect, both pointers will reach the end (`None`) at the same time.

**Detailed Explanation**

- **Initialization**:
  - Start with two pointers, one at the head of each list (`pointerA` at the head of List A, and `pointerB` at the head of List B).
- **Traversing**:
  - Move each pointer one step at a time.
  - When a pointer reaches the end of its list, redirect it to the head of the other list.
- **Meeting Point**:
  - If there is an intersection, both pointers will eventually meet at the intersection node.
  - If there is no intersection, both pointers will reach the end (`None`) simultaneously.

**Python Code with Detailed Comments**

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def get_intersection_node(headA, headB):
    # If either list is empty, there can be no intersection
    if headA is None or headB is None:
        return None

    # Initialize two pointers, starting at the heads of both lists
    pointerA, pointerB = headA, headB

    # Traverse both lists until the pointers meet or reach the end
    while pointerA != pointerB:
        # If pointerA reaches the end of List A, redirect it to the head of List B
        pointerA = pointerA.next if pointerA is not None else headB
    
        # If pointerB reaches the end of List B, redirect it to the head of List A
        pointerB = pointerB.next if pointerB is not None else headA

    # Either both pointers are None (no intersection) or they meet at the intersection node
    return pointerA

# Example usage:
# Create intersecting linked lists:
# List A: 1 -> 2 -> 3 -> 4 -> 5
# List B: 9 -> 4 -> 5
headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
intersection = ListNode(4)
intersection.next = ListNode(5)
headA.next.next.next = intersection

headB = ListNode(9)
headB.next = intersection

# Find intersection node
result = get_intersection_node(headA, headB)
if result:
    print(f"Intersecting Node: {result.value}")  # Output: Intersecting Node: 4
else:
    print("No intersection")
```

**Complexity Analysis**

- **Time Complexity**: **O(M + N)**, where **M** is the length of List A and **N** is the length of List B.
  - The worst case is when we traverse both lists entirely (when there is no intersection).
- **Space Complexity**: **O(1)**.
  - The solution uses only constant space (two pointers) and does not require any additional data structures.

**Key Points**

- The **two-pointer technique** ensures that both pointers traverse the entire length of both lists.
- If the lists intersect, the pointers will meet at the intersection node after switching heads once.
- If there is no intersection, both pointers will reach `None` at the same time.

This approach guarantees that the intersection node is found efficiently without extra memory, making it optimal for large linked lists.
