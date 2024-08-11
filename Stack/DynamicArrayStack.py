class Dynamicstack:
    def __init__(self, limit=10):
        self.stack = limit*[None]
        self.limit = limit

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) <= 0

    def is_full(self):
        return len(self.stack) >= self.limit

    def push(self, data):
        if self.is_full():
            self.resize()
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
        return self.stack[-1]

    def resize(self):
        new_stk = list(self.stk)
        self.limit = 2 * self.limit
        self.stack = new_stk


class StackOverflowError(BaseException):
    pass