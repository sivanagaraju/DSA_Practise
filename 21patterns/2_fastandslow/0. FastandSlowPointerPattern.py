def fast_and_slow_pointers(head):  # or array, or string
    slow = head  # initialize slow pointer
    fast = head  # initialize fast pointer

    while fast and fast.next:  # or fast and fast.next.next for some problems
        slow = slow.next  # move slow pointer one step
        fast = fast.next.next  # move fast pointer two steps

        # check for cycle or condition
        if slow == fast:  # or slow.equals(fast) for some problems
            # cycle detected or condition met
            return True  # or return slow, or return fast

    # no cycle detected or condition not met
    return False  # or return None

# Example usage:
head = [1, 2, 3, 4, 5]  # or a linked list, or a string
result = fast_and_slow_pointers(head)
print(result)


"""
Here are some interview questions based on the Fast and Slow Pointers pattern, along with the logic changes needed:
Detecting a cycle in a linked list:
Logic change: Move fast pointer two steps at a time.
Finding the middle element of a linked list:
Logic change: Move slow pointer one step at a time, move fast pointer two steps at a time.
Finding the first duplicate in an array:
Logic change: Move fast pointer one step at a time, move slow pointer only when a duplicate is found.
Finding the nth node from the end of a linked list:
Logic change: Move fast pointer n steps ahead, then move both pointers one step at a time.
Checking if a linked list is a palindrome:
Logic change: Use slow and fast pointers to find the middle, then compare elements from the start and end.
Finding the start of a loop in a linked list:
Logic change: Use slow and fast pointers to detect the loop, then move the slow pointer to the start and keep the fast pointer at the meeting point.
Detecting a cycle in an array:
Logic change: Use indexing instead of node traversal, move fast pointer two steps at a time.
Finding the maximum sum of a subarray:
Logic change: Move slow pointer only when the fast pointer finds a larger sum.
Finding the minimum window substring:
Logic change: Move slow pointer only when the fast pointer finds a valid substring.
Checking if a string is a rotation of another string:
Logic change: Use slow and fast pointers to compare characters from the start and end of the strings.
Some additional interview questions that may require modifications to the Fast and Slow Pointers pattern include:
Find the longest substring without repeating characters:
Logic change: Use a set to track unique characters, move slow pointer only when a repeating character is found.
Find the longest increasing subsequence:
Logic change: Use dynamic programming to track longest increasing subsequences, move slow pointer only when a larger element is found.
Find the minimum window that contains all elements of another array:
Logic change: Use a count array to track element frequencies, move slow pointer only when all elements are found.
By practicing these questions and modifying the logic accordingly, you'll become proficient in applying the Fast and Slow Pointers pattern to a wide range of problems!
"""