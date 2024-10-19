class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def in_place_manipulation(head):
    """
    In-place manipulation of a linked list.

    Args:
        head (ListNode): Head of the linked list.

    Returns:
        ListNode: Modified head of the linked list.
    """
    # Initialize pointers
    prev = None
    current = head

    while current:
        # Store next node
        next_node = current.next

        # Perform operation (e.g., delete, insert, reverse)
        # ...

        # Move pointers
        prev = current
        current = next_node

    return head

# Example operations:

def delete_node(head, key):
    """
    Delete a node with a given key.

    Args:
        head (ListNode): Head of the linked list.
        key (int): Key to delete.

    Returns:
        ListNode: Modified head of the linked list.
    """
    prev = None
    current = head
    while current:
        if current.val == key:
            if prev:
                prev.next = current.next
            else:
                head = current.next
            return head
        prev = current
        current = current.next
    return head

def insert_node(head, val, pos):
    """
    Insert a new node at a given position.

    Args:
        head (ListNode): Head of the linked list.
        val (int): Value to insert.
        pos (int): Position to insert.

    Returns:
        ListNode: Modified head of the linked list.
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head
    for _ in range(pos):
        prev = current
        current = current.next
    new_node = ListNode(val)
    new_node.next = current
    prev.next = new_node
    return dummy.next

def reverse_linked_list(head):
    """
    Reverse the entire linked list.

    Args:
        head (ListNode): Head of the linked list.

    Returns:
        ListNode: Modified head of the linked list.
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example usage:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original Linked List:")
while head:
    print(head.val, end=" ")
    head = head.next
print()

head = delete_node(head, 3)
print("Deleted Linked List:")
while head:
    print(head.val, end=" ")
    head = head.next
print()


"""
Here are some common interview questions using the In-Place Manipulation of a Linked List pattern:
Reverse Linked List:
Question: Reverse a singly linked list.
Logic: Initialize three pointers (prev, current, next). Traverse the list, and for each node, reverse the next pointer. Finally, return the new head.

Delete Node in a Linked List:
Question: Delete a node with a given key in a linked list.
Logic: Traverse the list, and when the key is found, update the next pointer of the previous node to skip the current node.

Insert Node in a Sorted Linked List:
Question: Insert a new node into a sorted linked list while maintaining the sorted order.
Logic: Traverse the list, and when the correct position is found, update the next pointers of the previous and new nodes.

Rotate Linked List:
Question: Rotate a linked list by a given number of positions.
Logic: Find the new tail node (length - k % length - 1 positions from the beginning), and update the next pointers to form a circular linked list. Then, find the new head node (k positions from the new tail), and update the next pointers to break the circular linked list.

Remove Duplicates from a Sorted Linked List:
Question: Remove duplicates from a sorted linked list.
Logic: Traverse the list, and when a duplicate is found, update the next pointer of the previous node to skip the current node.
Partition Linked List:
Question: Partition a linked list around a given value (all nodes less than the value come before all nodes greater than the value).
Logic: Initialize two lists (before and after), and traverse the original list. Update the next pointers to add nodes to the correct list. Finally, merge the two lists.
Reverse Linked List in Groups:
Question: Reverse a linked list in groups of a given size.
Logic: Traverse the list, and for each group, reverse the nodes using the standard reverse linked list logic.
These questions require you to manipulate the linked list in-place, without using extra space or modifying the original list structure. The key is to carefully update the next pointers to achieve the desired result.
"""