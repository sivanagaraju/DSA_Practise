from queue import *


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.maxData = float("-infinity")

    # region Traversal
    # C L R
    def pre_order_recursive(self, root, result):
        if not root:
            return
        result.append(root.data)
        self.pre_order_recursive(root.left, result)
        self.pre_order_recursive(root.right, result)

    def pre_order_iterative(self, root, result):
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def in_order_recursive(self, root, result):
        if not root:
            return
        self.pre_order_recursive(root.left, result)
        result.append(root.data)
        self.pre_order_recursive(root.right, result)

    def in_order_iterative(self, root, result):
        # L C R
        if not root:
            return
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.data)
                node = node.right

    def post_order_recursive(self, root, result):
        if not root:
            return
        self.pre_order_recursive(root.left, result)
        self.pre_order_recursive(root.right, result)
        result.append(root.data)

    def post_order_iterative(self, root, result):
        # L R C
        if not root:
            return
        stack = []
        node = root
        visited = set()
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.data)
                    node = None

    def level_order(self, root, result):
        if root is None:
            return
        q = Queue()
        q.put(root)
        node = None

        while not q.empty():
            node = q.get()
            result.append(node.data)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    # Finding the max element
    def find_max_recursive(self, root):
        if not root:
            return self.maxData

        if root.data > self.maxData:
            self.maxData = root.data

        self.find_max_recursive(root.left)
        self.find_max_recursive(root.right)
        return self.maxData

    def find_max_level_order(self, root):
        if root is None:
            return
        q = Queue()
        q.put(root)
        node = None
        maxElement = 0
        while not q.empty():
            node = q.get()
            if maxElement < node.data:
                maxElement = node.data
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
        return maxElement

    # search
    def find_search_recursive(self, root, data):
        if not root:
            return 0
        if root.data == data:
            return 1
        else:
            temp = self.find_search_recursive(root.left, data)
            if temp == 1:
                return temp
            else:
                return self.find_search_recursive(root.right, data)

    def find_search_level_order(self, root, data):
        if root is None:
            return 0
        q = Queue()
        q.put(root)
        node = None
        while not q.empty():
            node = q.get()
            if node.data == data:
                return 1
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return 0

    # Inserting an element in BTree
    def insert_left(self, root, data):

        pass

    def insert_right(self, root, data):
        pass

    def insert_level_order(self, root, data):
        pass

    def find_size_recursive(self, root):
        if root is None:
            return 0
        return self.find_size_recursive(root.left) + self.find_size_recursive(root.right)

    def find_size_level(self, root):
        if root is None:
            return 0
        q = Queue()
        q.put(root)
        node = None
        count = 0
        while not q.empty():
            node = q.get()
            count += 1
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return count

    def reverse_level(self, root):
        if root is None:
            return 0
        q = Queue()
        q.put(root)
        s = []
        node = None
        while not q.empty():
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            s.append(node.data)

        while len(s) != 0:
            print(s.pop())

    def max_depth_level_order(self, root):
        if root is None:
            return 0
        q = []
        q.append([root, 1])
        temp = 0
        while len(q) != 0:
            node, depth = q.pop()
            depth = max(temp, depth)
            if node.left:
                q.append([node.left, depth +1])
            if node.right:
                q.append([node.right, depth + 1])
        return temp


    # endregion
