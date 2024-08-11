class Node:
    def __init__(self, data):
      self.data = data
      self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        curr = self.head
        new_node.next = curr
        if not self.head:
            new_node.next = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node

        self.head = new_node

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.head.next = self.head
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next

            new_node = Node(data)
            curr_node.next = new_node
            new_node.next = self.head





    def print_list(self):
      pass