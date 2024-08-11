### Fast and Slow Pointers Concept

**Concept Explanation:**
The Fast and Slow Pointers technique (also known as the Tortoise and Hare algorithm) is a two-pointer strategy commonly used for cycle detection in linked lists and other similar problems. It involves using two pointers that move through the data structure at different speeds. Typically, the fast pointer moves two steps at a time, while the slow pointer moves one step at a time. If there's a cycle, the fast pointer will eventually meet the slow pointer.

**When to Use Fast and Slow Pointers:**
- The problem involves a linked list and you need to detect cycles.
- You need to find the middle of a linked list.
- You need to detect the start of a cycle in a linked list.
- The problem involves repeated patterns or cycles in arrays.

**Visualizing Fast and Slow Pointers:**

Consider the problem of detecting a cycle in a linked list. Let's visualize this:

```
Linked List: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle back to 3)

Initial pointers:
  slow = 1
  fast = 1

Steps:
1. Move slow one step and fast two steps:
   slow = 2
   fast = 3

2. Move slow one step and fast two steps:
   slow = 3
   fast = 5

3. Move slow one step and fast two steps:
   slow = 4
   fast = 4 (cycle detected)
```


Sure, let's visualize the detection of a cycle in the array `[2, 3, 1, 4, 0, 9, 7]` using the Floyd’s Tortoise and Hare algorithm. I'll illustrate each iteration with the positions of the `slow` and `fast` pointers.

### Visualize the Detect cycle in a array:
\[2, 3, 1, 4, 0, 9, 7\]

### Iteration Details:

1. **Initial State:**
   - `slow` starts at index 0.
   - `fast` starts at index 0.
   - Array values: \[2, 3, 1, 4, 0, 9, 7\]

   ```
   slow = 0, fast = 0
   ```

2. **Iteration 1:**
   - `slow` moves to `arr[0]` = 2 (next index is 2).
   - `fast` moves to `arr[arr[0]]` = `arr[2]` = 1 (next index is 1).

   ```
   slow = 2, fast = 1
   ```

3. **Iteration 2:**
   - `slow` moves to `arr[2]` = 1 (next index is 1).
   - `fast` moves to `arr[arr[1]]` = `arr[3]` = 4 (next index is 4).

   ```
   slow = 1, fast = 4
   ```

4. **Iteration 3:**
   - `slow` moves to `arr[1]` = 3 (next index is 3).
   - `fast` moves to `arr[arr[4]]` = `arr[0]` = 2 (next index is 2).

   ```
   slow = 3, fast = 2
   ```

5. **Iteration 4:**
   - `slow` moves to `arr[3]` = 4 (next index is 4).
   - `fast` moves to `arr[arr[2]]` = `arr[1]` = 3 (next index is 3).

   ```
   slow = 4, fast = 3
   ```

6. **Iteration 5:**
   - `slow` moves to `arr[4]` = 0 (next index is 0).
   - `fast` moves to `arr[arr[3]]` = `arr[4]` = 0 (next index is 0).

   ```
   slow = 0, fast = 0
   ```

   At this point, the `slow` and `fast` pointers meet, indicating the presence of a cycle.

### Visualization:
```
Initial State:
Index:  0   1   2   3   4   5   6
Array: [2,  3,  1,  4,  0,  9,  7]
slow:  ^  
fast:  ^

Iteration 1:
Index:  0   1   2   3   4   5   6
Array: [2,  3,  1,  4,  0,  9,  7]
slow:          ^  
fast:      ^

Iteration 2:
Index:  0   1   2   3   4   5   6
Array: [2,  3,  1,  4,  0,  9,  7]
slow:      ^  
fast:                  ^

Iteration 3:
Index:  0   1   2   3   4   5   6
Array: [2,  3,  1,  4,  0,  9,  7]
slow:              ^  
fast:          ^

Iteration 4:
Index:  0   1   2   3   4   5   6
Array: [2,  3,  1,  4,  0,  9,  7]
slow:                  ^  
fast:              ^

Iteration 5:
Index:  0   1   2   3   4   5   6
Array: [2,  3,  1,  4,  0,  9,  7]
slow:  ^  
fast:  ^

Cycle detected at index 0.
```

### Explanation:
- In each iteration, the `slow` pointer moves one step forward and the `fast` pointer moves two steps forward.
- When both pointers meet, it indicates the presence of a cycle.
- The cycle is detected at index 0, confirming that there is a cycle in the array.

**General Template for Fast and Slow Pointers:**

While the specific implementation can vary based on the problem, a general template for the Fast and Slow Pointers approach can be outlined as follows:

1. **Initialize Pointers:**
   - Set both the fast and slow pointers to the head of the linked list (or start of the data structure).

2. **Move Pointers:**
   - Move the slow pointer one step at a time.
   - Move the fast pointer two steps at a time.

3. **Check for Cycle:**
   - If the fast pointer meets the slow pointer, a cycle is detected.
   - If the fast pointer reaches the end (null), no cycle is present.

### Example Problems and Solutions

**Example 1: Detect Cycle in a Linked List**

**Problem Statement:**
Given the head of a linked list, determine if the linked list has a cycle in it.

**Example:**
```python
# Linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle back to 3)

# Expected Output: True
```

**Solution:**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if not head:
        return False

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next  # Creating a cycle

print(has_cycle(head))  # Output: True
```

**Example 2: Find the Start of the Cycle in a Linked List**

**Problem Statement:**
Given the head of a linked list that contains a cycle, return the node where the cycle begins.

**Example:**
```python
# Linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle back to 3)

# Expected Output: Node with value 3
```

**Solution:**
```python
def find_cycle_start(head):
    if not head:
        return None

    slow, fast = head, head
    cycle_detected = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle_detected = True
            break

    if not cycle_detected:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next  # Creating a cycle

start_of_cycle = find_cycle_start(head)
print(start_of_cycle.val)  # Output: 3
```

**Example 3: Find the Middle of a Linked List**

**Problem Statement:**
Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

**Example:**
```python
# Linked list: 1 -> 2 -> 3 -> 4 -> 5

# Expected Output: Node with value 3
```

**Solution:**
```python
def find_middle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

middle = find_middle(head)
print(middle.val)  # Output: 3
```

### Additional Practice Questions

1. **Linked List Cycle Length**:
   Given the head of a linked list, return the length of the cycle in the list. If there is no cycle, return 0.

   **Example:**
   ```python
   # Linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle back to 3)

   # Expected Output: 3
   ```

2. **Happy Number**:
   Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1. If the number loops endlessly in a cycle that does not include 1, those numbers that do not end in 1 are unhappy.

   **Example:**
   ```python
   n = 19

   # Expected Output: True (because 19 is a happy number)
   ```

3. **Palindrome Linked List**:
   Given the head of a singly linked list, return true if it is a palindrome.

   **Example:**
   ```python
   # Linked list: 1 -> 2 -> 2 -> 1

   # Expected Output: True
   ```

4. **Reorder List**:
   Given a singly linked list L: L0 → L1 → … → Ln-1 → Ln, reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

   **Example:**
   ```python
   # Linked list: 1 -> 2 -> 3 -> 4

   # Expected Output: 1 -> 4 -> 2 -> 3
   ```

5. **Intersection of Two Linked Lists**:
   Write a program to find the node at which the intersection of two singly linked lists begins.

   **Example:**
   ```python
   # Linked lists: A = 1 -> 2
   #               B = 3 -> 2

   # Expected Output: Node with value 2
   ```

### Solutions

**Linked List Cycle Length:**

```python
def cycle_length(head):
    if not head:
        return 0

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return calculate_cycle_length(slow)

    return 0

def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next  # Creating a cycle

print(cycle_length(head))  # Output: 3
```

**Happy Number:**

```python
def is_happy(n):
    def get_next(number):
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit * digit
            number //= 10
        return total_sum

    slow, fast = n, get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1

# Example usage
print(is_happy(19))  # Output: True
```

**Palindrome Linked List:**

```python
def is_palindrome(head):
    if not head or not head.next:
        return True

    # Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow

.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Compare the first and second half
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print(is_palindrome(head))  # Output: True
```

**Reorder List:**

```python
def reorder_list(head):
    if not head or not head.next:
        return

    # Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev, curr = None, slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Merge the two halves
    first, second = head, prev
    while second.next:
        first_next, second_next = first.next, second.next
        first.next = second
        second.next = first_next
        first, second = first_next, second_next

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

reorder_list(head)

while head:
    print(head.val, end=" -> ")
    head = head.next
# Output: 1 -> 4 -> 2 -> 3 -> 
```

**Intersection of Two Linked Lists:**

```python
def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None

    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a

# Example usage
headA = ListNode(1)
headA.next = ListNode(2)
intersection = ListNode(3)
headA.next.next = intersection

headB = ListNode(4)
headB.next = intersection

print(get_intersection_node(headA, headB).val)  # Output: 3
```

Sure! Here are some additional medium and hard questions that utilize the Fast and Slow Pointers technique:

### Medium-Level Fast and Slow Pointers Problems

1. **Linked List Cycle II**:
   Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

   **Example:**
   ```python
   # Linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle back to 3)
   # Expected Output: Node with value 3
   ```

2. **Middle of the Linked List**:
   Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

   **Example:**
   ```python
   # Linked list: 1 -> 2 -> 3 -> 4 -> 5
   # Expected Output: Node with value 3
   ```

3. **Palindrome Linked List**:
   Given the head of a singly linked list, return true if it is a palindrome.

   **Example:**
   ```python
   # Linked list: 1 -> 2 -> 2 -> 1
   # Expected Output: True
   ```

4. **Remove Nth Node From End of List**:
   Given the head of a linked list, remove the nth node from the end of the list and return its head.

   **Example:**
   ```python
   # Linked list: 1 -> 2 -> 3 -> 4 -> 5, n = 2
   # Expected Output: 1 -> 2 -> 3 -> 5
   ```

5. **Find the Duplicate Number**:
   Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Find the duplicate one.

   **Example:**
   ```python
   nums = [1, 3, 4, 2, 2]
   # Expected Output: 2
   ```

### Hard-Level Fast and Slow Pointers Problems

1. **Find the Duplicate Number (Cycle Detection)**:
   Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), there is only one duplicate number in the array, but it could be repeated more than once. Find the duplicate one using constant space.

   **Example:**
   ```python
   nums = [3, 1, 3, 4, 2]
   # Expected Output: 3
   ```

2. **Intersection of Two Linked Lists**:
   Write a program to find the node at which the intersection of two singly linked lists begins.

   **Example:**
   ```python
   # Linked lists: A = 1 -> 2
   #               B = 3 -> 2
   # Expected Output: Node with value 2
   ```

3. **Cycle in Circular Array**:
   You are given a circular array nums of positive and negative integers. If a number k at an index is positive, move forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element. Determine if there is a cycle in the array.

   **Example:**
   ```python
   nums = [2, -1, 1, 2, 2]
   # Expected Output: True (The cycle is: nums[0] -> nums[2] -> nums[3] -> nums[0])
   ```

4. **Happy Number**:
   Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1. If the number loops endlessly in a cycle that does not include 1, those numbers that do not end in 1 are unhappy.

   **Example:**
   ```python
   n = 19
   # Expected Output: True
   ```

5. **Linked List Cycle Length**:
   Given the head of a linked list, return the length of the cycle in the list. If there is no cycle, return 0.

   **Example:**
   ```python
   # Linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle back to 3)
   # Expected Output: 3
   ```

### Solutions

**Linked List Cycle II:**

```python
def detect_cycle(head):
    if not head or not head.next:
        return None

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next  # Creating a cycle

print(detect_cycle(head).val)  # Output: 3
```

**Middle of the Linked List:**

```python
def middle_node(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(middle_node(head).val)  # Output: 3
```

**Palindrome Linked List:**

```python
def is_palindrome(head):
    if not head or not head.next:
        return True

    # Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Compare the first and second half
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

print(is_palindrome(head))  # Output: True
```

**Remove Nth Node From End of List:**

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy, dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

new_head = remove_nth_from_end(head, 2)

while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
# Output: 1 -> 2 -> 3 -> 5 -> 
```

**Find the Duplicate Number:**

```python
def find_duplicate(nums):
    slow, fast = nums[0], nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Example usage
nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))  # Output: 2
```

**Cycle in Circular Array:**

```python
def circular_array_loop(nums):
    def next_index(i):
        return (i + nums[i]) % len(nums)

    for i in range(len(nums)):
        slow, fast = i, i

        while nums[slow] * nums[next_index(fast)] > 0 and nums[slow] * nums[next_index(next_index(fast))] > 0:
            slow = next_index(slow)
            fast = next_index(next_index(fast))

            if slow == fast:
                if slow == next_index(slow):
                    break
                return True

    return False

# Example usage
nums = [2, -1, 1, 2, 2]
print(circular_array_loop(nums))  # Output: True
```

**Happy Number:**

```python
def is_happy(n):
    def get_next(number):
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit * digit
            number //= 10
        return total_sum

    slow

, fast = n, get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1

# Example usage
print(is_happy(19))  # Output: True
```

**Linked List Cycle Length:**

```python
def cycle_length(head):
    if not head:
        return 0

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return calculate_cycle_length(slow)

    return 0

def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next.next  # Creating a cycle

print(cycle_length(head))  # Output: 3
```
