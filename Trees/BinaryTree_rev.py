from queue import *

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.maxData = float()