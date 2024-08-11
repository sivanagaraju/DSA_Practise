# coding=utf-8
# from builtins import BaseException, bool, len


class ArrayStack:
    """
    LIFO stack implementation using a Python list as Underlying
    Push and Pop are the backbones of stack. (Stack of Dinner Plates)
    LIFO(Last in Fast Out) Major Operations that you perform on the stack are always focused on the End of the stack, called the TOP
    PUSH → Add a new Element to the Stack.
    POP → Remove the element from the stack.
    PEEK → To see the top element in the stack.
    Other Operations in the stack are → isEmpty, ISFULL, Size
    Best way to implement the stack is using the linked list
    """
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def __bool__(self):
        return bool(self.stack)

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.limit

    def push(self, data):
        if self.is_full():
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("Under Flow")
            return None
        data = self.stack.pop()
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.size -1]


class StackOverflowError(BaseException):
    pass
