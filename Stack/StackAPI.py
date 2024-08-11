"""
Design a stack that includes a max operation, in addition to push and pop. The max method should
return the maximum value stored in the stack.
"""


class Stack():
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        if self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

