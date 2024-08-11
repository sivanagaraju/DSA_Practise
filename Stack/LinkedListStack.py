# Implementing Stack using Linked List
class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class Stack(object):
    def __int__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        temp = Node()
        temp.set_data(data)
        temp.set_next(self.head)

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.get_data()
        self.head = self.head.get_next()
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.get_data()


if __name__ =="__main__":
    our_list = ["first", "second", "third", "fourth"]
    our_stack = Stack(our_list)
    print(our_stack.pop())
    print(our_stack.peek())
    print(our_stack.pop())
    print(our_stack.peek())
    print(our_stack.pop())