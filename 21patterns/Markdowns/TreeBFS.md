# Comprehensive Guide to Tree BFS Coding Pattern

## 1. Core Concepts and Coding Patterns

**Breadth-First Search (BFS)** for a tree is an algorithm used to traverse or search data structures like trees and graphs. The fundamental idea is to explore nodes level by level, moving from the root level to deeper levels sequentially. Typically, BFS utilizes a queue to ensure that nodes are visited in the correct order.

**Typical Use Cases:** BFS is ideal when you need to explore nodes level-wise, such as finding the shortest path in an unweighted tree or determining the minimum depth of a binary tree. Other practical applications include finding all possible paths in a tree or solving puzzles represented as trees.

- **Working Principle:** Starting from the root, BFS explores all nodes at the present level before moving on to nodes at the next depth level. This traversal can be easily achieved using a queue, as it ensures that the nodes are visited in a first-in-first-out (FIFO) manner.

## 2. Numeric Examples

Consider the following binary tree:

```
       1
      / \
     2   3
    / \   \
   4   5   6
```

**BFS Traversal Output:** 1, 2, 3, 4, 5, 6

- The traversal starts from the root (1), explores nodes 2 and 3, then moves on to nodes 4, 5, and 6.

## 3. Problem Identification Checklist

**When to Use Tree BFS:**

| Problem Identified                        | Example                                           |
| ----------------------------------------- | ------------------------------------------------- |
| Explore a tree level by level             | Level-order traversal of nodes in a tree          |
| Shortest path in an unweighted tree       | Find the minimum depth of a binary tree           |
| Calculate minimum/maximum depth of a tree | Calculate the depth of a tree from root           |
| Group nodes at each level                 | Level-by-level grouping of nodes in a tree        |
| Connect nodes at the same level           | Connect all nodes at the same level with pointers |

## 4. General Templates with Comments

To understand the purpose of each template, it helps to start with a high-level overview before diving into the code. The first template focuses on basic BFS for level-order traversal, which is useful for visiting all nodes. The second template groups nodes by their levels, which is beneficial for problems requiring level-wise analysis.

**Template 1: Basic BFS Traversal**

```python
from collections import deque

def bfs_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        current_node = queue.popleft()  # Pop the front element
        result.append(current_node.val)  # Process the current node
        
        if current_node.left:
            queue.append(current_node.left)  # Add left child to the queue
        if current_node.right:
            queue.append(current_node.right)  # Add right child to the queue
    
    return result
```

- **Use Case:** This template is used for basic level-order traversal of a binary tree.
- **Explanation:** Nodes are appended to a queue and visited one by one in FIFO order.

**Template 2: Level-by-Level Traversal**

```python
from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)  # Number of elements at the current level
        current_level = []
        
        for _ in range(level_size):
            current_node = queue.popleft()  # Pop the front element
            current_level.append(current_node.val)  # Process the current node
            
            if current_node.left:
                queue.append(current_node.left)  # Add left child to the queue
            if current_node.right:
                queue.append(current_node.right)  # Add right child to the queue
        
        result.append(current_level)
    
    return result
```

- **Use Case:** This template is used when the problem requires nodes at each level to be grouped together.

## 5. Complexity Analysis

- **Time Complexity:** Both templates have a time complexity of **O(N)**, where **N** is the number of nodes in the tree, as each node is visited exactly once. In the worst case, such as a perfectly balanced binary tree, all nodes are traversed level by level, leading to a linear time complexity. However, in cases where the tree is highly unbalanced, BFS may end up exploring many levels, resulting in a similar time complexity but potentially more operations if the tree depth is significant.

- **Space Complexity:** The space complexity is **O(N)** in the worst case, which occurs when the tree is a complete binary tree, requiring space to store all nodes at the current level in the queue. In a balanced binary tree, the maximum number of nodes at the last level can be around **N/2**, leading to **O(N)** space. For a skewed tree, the space complexity could be **O(1)** if there are no sibling nodes, but in general, the worst-case scenario requires storing a significant number of nodes, especially if the tree is wide.

## 6. Discussion on Templates and Patterns

These BFS templates can be adjusted based on the problem requirements, such as including conditional checks to calculate specific metrics (e.g., minimum depth). The key idea is to identify when a level-by-level exploration is required and modify the traversal accordingly.

## 7. Multiple Approaches and Implementations

**Iterative vs. Recursive BFS:**

- **Iterative BFS:** Uses a queue to traverse the tree. This is the standard approach and is more commonly used.
- **Recursive BFS:** BFS is generally implemented iteratively, as the queue-based approach naturally fits the level-order traversal mechanism. Implementing BFS recursively would require additional helper functions and stack management, which can make it more complex.

## 9. Practice Problems

| S.No | Question                             | Detailed Example                                                                                              | Difficulty Level | Approach                                             |
| ---- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------- |
| 1    | Level Order Traversal of Binary Tree | **Example:** Given the tree: `1 -> [2, 3] -> [4, 5, 6]`, perform level order traversal. **Output:** `[1], [2, 3], [4, 5, 6]`. Traverse the tree level-wise and print the nodes at each level. | Easy             | Basic BFS                                            |
| 2    | Minimum Depth of Binary Tree         | **Example:** Given the tree: `1 -> [2, 3] -> [4]`, the shortest path to a leaf is from `1 -> 3`. **Output:** Minimum depth = 2. Calculate the minimum level required to reach a leaf node. | Medium           | Level-by-Level BFS                                   |
| 3    | Zigzag Level Order Traversal         | **Example:** Given the tree: `1 -> [2, 3] -> [4, 5, 6, 7]`, the zigzag order is `[1], [3, 2], [4, 5, 6, 7]`. Traverse the levels alternating left to right and right to left. | Medium           | Modified BFS                                         |
| 4    | Average of Levels in Binary Tree     | **Example:** Given nodes with values `[3 -> 9, 20 -> 15, 7]`, calculate the averages: `[3], [14.5], [11]`. For each level, find the average value of the nodes. | Easy             | Level-by-Level BFS, Calculate average at each level  |
| 5    | Find Largest Value in Each Tree Row  | **Example:** Given the tree: `1 -> [3, 2] -> [5, 3, 9]`, the largest values are `[1], [3], [9]`. Find the maximum value at each level of the tree. | Medium           | Level-by-Level BFS, Track max at each level          |
| 6    | Connect All Nodes at the Same Level  | **Example:** Given tree `1 -> [2, 3] -> [4, 5, 7]`, connect nodes at the same level: `2 -> 3`, `4 -> 5 -> 7`. Set the `next` pointers for all nodes at the same level. | Hard             | Level-by-Level BFS with pointers                     |
| 7    | Binary Tree Right Side View          | **Example:** Given the tree: `1 -> [2, 3] -> [5, 4]`, the right side view is `[1, 3, 4]`. Print the rightmost node at each level. | Medium           | Modified BFS, Track last element of each level       |
| 8    | Cousins in Binary Tree               | **Example:** Given the tree: `1 -> [2, 3] -> [4, 5]`, determine if `4` and `5` are cousins. **Output:** `True`. They are at the same level with different parents. | Medium           | BFS, Track level and parent for both nodes           |
| 9    | Binary Tree Level Order Traversal II | **Example:** Given tree `1 -> [2, 3] -> [4, 5, 6]`, the bottom-up level order is `[4, 5, 6], [2, 3], [1]`. Traverse the tree from bottom to top. | Medium           | BFS with stack for reversing levels                  |
| 10   | Binary Tree Vertical Order Traversal | **Example:** Given tree `1 -> [2, 3] -> [4, 5, 6, 7]`, group nodes by vertical levels: `[4], [2], [1, 5, 6], [3], [7]`. Nodes are printed according to their vertical order. | Hard             | BFS with column index tracking                       |
| 11   | Binary Tree Diagonal Traversal       | **Example:** Given tree `1 -> [2, 3] -> [4, 5, 6, 7]`, diagonal traversal yields `[1, 3, 7], [2, 5, 6], [4]`. Traverse the tree diagonally from top right to bottom left. | Medium           | BFS with diagonal grouping                           |
| 12   | Serialize and Deserialize Binary Tree| **Example:** Given tree `1 -> [2, 3] -> [4, 5]`, serialize it to `1,2,3,4,5,null,null`. Deserialize back to form the original tree structure. | Hard             | BFS for level order serialization                    |
| 13   | Maximum Width of Binary Tree         | **Example:** For the tree `1 -> [3, 2] -> [5, 3, 9]`, the maximum width is `4` at the third level. Calculate the number of nodes between the leftmost and rightmost non-null nodes. | Medium           | BFS with position indexing                           |
| 14   | Sum of Nodes at Kth Level            | **Example:** Given tree `1 -> [2, 3] -> [4, 5, 6]`, sum of nodes at level `2` is `4 + 5 + 6 = 15`. Calculate the sum of nodes at the given level `K`. | Easy             | Level-by-Level BFS, Sum nodes at specific level      |
| 15   | Count Complete Tree Nodes            | **Example:** For a complete binary tree with nodes `1 -> [2, 3] -> [4, 5, 6, 7]`, count the nodes. **Output:** `7`. Count all nodes in a complete tree. | Medium           | Modified BFS with count logic                        |
| 16   | Find Leaves of Binary Tree           | **Example:** Given the tree `1 -> [2, 3] -> [4, 5, 6]`, leaves are `[4, 5, 6]`. Collect all nodes that have no children. | Medium           | BFS to identify and collect leaf nodes               |
| 17   | Boundary Traversal of Binary Tree    | **Example:** Given the tree `1 -> [2, 3] -> [4, 5, 6, 7]`, boundary traversal gives `[1, 2, 4, 5, 6, 7, 3]`. Traverse the boundary nodes in a specified order. | Hard             | BFS for boundary nodes                               |
| 18   | Check Completeness of a Binary Tree  | **Example:** Given the tree `1 -> [2, 3] -> [4, 5]`, verify if it’s complete. **Output:** `True`. Check level-wise if the nodes are filled from left to right. | Medium           | Level-by-Level BFS, Validate complete property       |
| 19   | Deepest Leaves Sum                   | **Example:** Given the tree `1 -> [2, 3] -> [4, 5, 6, 7]`, the sum of the deepest leaves (`4, 5, 6, 7`) is `22`. | Medium           | Level-by-Level BFS to track and sum nodes at the deepest level |
| 20   | All Nodes Distance K in Binary Tree  | **Example:** Given the tree `1 -> [2, 3] -> [4, 5]` and target node `2` with `K=1`, nodes at distance `1` are `[1, 4, 5]`. | Hard             | BFS from the target node, using a distance counter to find nodes at distance `K` |


**Detailed Approach for Selected Problems:**

Consider breaking down each approach into smaller steps or adding diagrams to visually represent how BFS is applied to solve each problem for better comprehension.

- **Average of Levels in Binary Tree:** Use level-by-level BFS to traverse the tree. For each level, calculate the sum of the node values and divide by the number of nodes at that level to obtain the average.

- **Find Largest Value in Each Tree Row:** Use a similar level-by-level BFS approach. For each level, track the maximum value and store it.

- **Connect All Nodes at the Same Level:** This problem involves adding pointers between nodes at the same level. During level-wise traversal, keep track of the previous node and connect it to the current node.

- **Binary Tree Right Side View:** Perform a BFS, and for each level, capture the last node in that level to get the right side view of the binary tree.

## 10. Key Takeaways, Tips, and Summary

- **Key Takeaways:** BFS is a powerful technique for level-wise exploration of a tree. It is often implemented using a queue.
- **Practical Tips:** Use BFS when you need to explore nodes level by level or determine the shortest path in an unweighted graph/tree.
- **Summary:** BFS involves visiting nodes level by level using a queue, which is particularly useful for problems requiring complete level exploration.

## 11. Common Pitfalls

- **Handling Edge Cases:** For trees with only one node or highly unbalanced trees, ensure that your implementation can correctly handle these scenarios. For example, if the tree has only one node, the traversal should simply return that single node without any errors.
- **Mistakes to Avoid:** Forgetting to check if the root is `None` before starting traversal can lead to runtime errors (e.g., attempting to access properties of a `None` object, resulting in an `AttributeError`).
- **Troubleshooting Tips:** Ensure that all child nodes are added to the queue correctly, and double-check the termination conditions to avoid infinite loops.

### Explanation of Level Order Traversal of Binary Tree

**Level Order Traversal** is a fundamental tree traversal method where the nodes are visited level by level from top to bottom, starting with the root, and moving left to right at each level. This is often used to understand the structure of a tree, make modifications, or solve problems involving level-wise operations.

#### Example:
Consider the following binary tree:
```
       1
      / \
     2   3
    / \   \
   4   5   6
```
The **level order traversal** of this tree is: `[1], [2, 3], [4, 5, 6]`. This means we first visit the root (`1`), then all its children (`2` and `3`), and finally all the children of nodes at the previous level (`4, 5, 6`).

### Python Code Explanation

Here is a Python implementation for level order traversal using Breadth-First Search (BFS) with detailed comments.

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    # Edge case: if the tree is empty
    if not root:
        return []

    # Result list to store level order traversal
    result = []

    # Initialize a queue and enqueue the root node
    queue = deque([root])

    # Continue until all nodes are processed
    while queue:
        # Number of nodes at the current level
        level_size = len(queue)
        # List to store current level's nodes
        current_level = []

        # Iterate over all nodes at the current level
        for _ in range(level_size):
            # Pop the front element from the queue
            current_node = queue.popleft()
            # Add the current node's value to the current level list
            current_level.append(current_node.val)

            # Add left child to queue if it exists
            if current_node.left:
                queue.append(current_node.left)
            # Add right child to queue if it exists
            if current_node.right:
                queue.append(current_node.right)

        # Add the current level to the result
        result.append(current_level)

    return result

# Example usage
if __name__ == "__main__":
    # Construct the tree: 
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # Print level order traversal
    print(level_order_traversal(root))
```

### Key Points:

- The `deque` data structure is used because it allows efficient appending and popping from both ends, which is useful for BFS.
- The outer while loop ensures we continue processing until all nodes are visited.
- The inner for loop processes all nodes at a given level and prepares for the next level.

The approach uses a queue to ensure each level of nodes is processed in order before moving to the next level, making it efficient for level-order exploration tasks in trees. The **time complexity** is **O(N)**, where **N** is the number of nodes, and the **space complexity** is **O(N)** in the worst case, due to the queue.


### Zigzag Level Order Traversal: Explanation and Python Solution

#### Problem Explanation
In a Zigzag Level Order Traversal, nodes of a binary tree are traversed level by level, but the direction alternates at each level. This means:
- At level 1, nodes are visited left to right.
- At level 2, nodes are visited right to left.
- At level 3, nodes are visited left to right again, and so on.

This traversal pattern gives a zigzag effect, hence the name "Zigzag Level Order Traversal."

#### Numeric Example:
Consider the following binary tree:

```
       1
      / \
     2   3
    / \   \
   4   5   6
```

The **zigzag level order traversal** of this tree would be:
- Level 1: `[1]` (left to right)
- Level 2: `[3, 2]` (right to left)
- Level 3: `[4, 5, 6]` (left to right)

**Final Output:** `[[1], [3, 2], [4, 5, 6]]`

#### Python Solution with Explanation
To solve the problem, we use a Breadth-First Search (BFS) approach with a slight modification to alternate the direction of traversal at each level.

Here is the Python implementation:

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order_traversal(root):
    # Edge case: if the tree is empty
    if not root:
        return []

    # Result list to store zigzag level order traversal
    result = []

    # Initialize a queue and enqueue the root node
    queue = deque([root])

    # Flag to indicate the direction of traversal (left to right or right to left)
    left_to_right = True

    # Continue until all nodes are processed
    while queue:
        # Number of nodes at the current level
        level_size = len(queue)
        # List to store current level's nodes
        current_level = []

        # Iterate over all nodes at the current level
        for _ in range(level_size):
            # Pop the front element from the queue
            current_node = queue.popleft()

            # Add the current node's value to the current level list
            # If traversing left to right, append to the end; if right to left, append to the beginning
            if left_to_right:
                current_level.append(current_node.val)
            else:
                current_level.insert(0, current_node.val)

            # Add left and right children to queue if they exist
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        # Add the current level to the result
        result.append(current_level)
        # Toggle the direction for the next level
        left_to_right = not left_to_right

    return result

# Example usage
if __name__ == "__main__":
    # Construct the tree: 
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # Print zigzag level order traversal
    print(zigzag_level_order_traversal(root))
```


### Key Points:
- The `deque` data structure is used because it allows efficient popping from the front, which is required for level-wise traversal.
- The flag `left_to_right` toggles after each level to ensure the traversal direction is reversed at every alternate level.
- The **time complexity** is **O(N)**, where **N** is the number of nodes, since each node is processed once.
- The **space complexity** is **O(N)**, primarily due to storing nodes in the queue.

This approach ensures that the nodes are visited in the desired zigzag pattern efficiently, making it ideal for problems where a level-wise yet alternating traversal is required.

### Explanation: "Connect All Nodes at the Same Level"

The problem **"Connect All Nodes at the Same Level"** is about connecting nodes horizontally at each level of a binary tree. Specifically, we need to add pointers between all nodes at the same level such that nodes at each level are linked from left to right.

#### Numeric Example:

Consider the following binary tree:

```
       1
      / \
     2   3
    / \   \
   4   5   7
```

The goal is to connect nodes at the same level, resulting in the following connections:

- At level 1: `1` (no connection needed).
- At level 2: Connect `2 -> 3`.
- At level 3: Connect `4 -> 5 -> 7`.

The final connections can be visualized like this:

```
       1
      / \
     2 -> 3
    / \    \
   4 -> 5 -> 7
```

All nodes at the same level are connected from left to right.

### Python Solution:

We can solve this problem using a level-order traversal (BFS) approach. During traversal, we use a queue to keep track of nodes at each level and set up pointers between nodes.

Here is the Python implementation:

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None  # Pointer to the next node at the same level

def connect_nodes_at_same_level(root):
    # Edge case: if the tree is empty
    if not root:
        return None

    # Initialize a queue and enqueue the root node
    queue = deque([root])

    # Continue until all nodes are processed
    while queue:
        # Number of nodes at the current level
        level_size = len(queue)
        # Previous node in the current level (used for connecting nodes)
        previous_node = None

        # Iterate over all nodes at the current level
        for _ in range(level_size):
            # Pop the front element from the queue
            current_node = queue.popleft()

            # Connect the previous node to the current node
            if previous_node:
                previous_node.next = current_node

            # Update the previous node to be the current one
            previous_node = current_node

            # Add left and right children to the queue if they exist
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return root

# Example usage
def print_connections(root):
    # Helper function to print connections at each level
    while root:
        current = root
        while current:
            print(current.val, end=" -> " if current.next else " -> None\n")
            current = current.next
        # Move to the next level (first child of the current level)
        if root.left:
            root = root.left
        else:
            root = root.right

if __name__ == "__main__":
    # Construct the tree: 
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)

    # Connect nodes at the same level and print the connections
    connect_nodes_at_same_level(root)
    print_connections(root)
```

**Output** for the provided example would be:

```
1 -> None
2 -> 3 -> None
4 -> 5 -> 7 -> None
```

### Key Points:

- The queue ensures that we process all nodes at each level before moving to the next.
- The `previous_node` variable helps establish connections between nodes at the same level.
- **Time Complexity** is **O(N)**, where **N** is the number of nodes, since each node is visited exactly once.
- **Space Complexity** is **O(N)** due to the use of the queue for storing nodes at each level.

This approach allows us to efficiently connect nodes at the same level, ensuring that each node has a `next` pointer set to its neighboring node in the level, or `None` if it is the last node in that level.

-
-
-
-
-
-
-
-
-
-
-
-
-
-


### Explanation: Cousins in Binary Tree

The problem **"Cousins in Binary Tree"** involves determining if two nodes in a binary tree are cousins. Two nodes are considered cousins if they meet the following criteria:
1. They are at the same level of the tree.
2. They have different parents.

In other words, cousins are nodes that are at the same depth but are not siblings.

#### Numeric Example:

Consider the following binary tree:

```
       1
      / \
     2   3
    /     \
   4       5
```

In this tree:
- Nodes `4` and `5` are **cousins** because they are both at level 3, and their parents (`2` and `3`) are different.
- Nodes `2` and `3` are **not cousins** because they are at level 2 but have the same parent (`1`).

**Example Question**: Given the tree above, determine if nodes `4` and `5` are cousins.

**Answer**: `True`. Nodes `4` and `5` are cousins.

### Python Solution with Explanation

To solve this problem, we can use a **Breadth-First Search (BFS)** approach to traverse the tree level by level, keeping track of the parent of each node and the level of the target nodes. If both target nodes are found at the same level and have different parents, then they are cousins.

Here's the Python implementation:

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def are_cousins(root, x, y):
    # Edge case: if the tree is empty
    if not root:
        return False

    # Initialize a queue to perform level-order traversal
    queue = deque([(root, None)])  # Each element is a tuple (node, parent)

    while queue:
        level_size = len(queue)
        x_parent = None
        y_parent = None

        # Iterate over all nodes at the current level
        for _ in range(level_size):
            current_node, parent = queue.popleft()

            # Check if the current node is either x or y
            if current_node.val == x:
                x_parent = parent
            if current_node.val == y:
                y_parent = parent

            # Add children to the queue along with their parent
            if current_node.left:
                queue.append((current_node.left, current_node))
            if current_node.right:
                queue.append((current_node.right, current_node))

        # After traversing the current level, check if x and y are cousins
        if x_parent and y_parent:
            # x and y are cousins if they have different parents
            return x_parent != y_parent
        if (x_parent and not y_parent) or (y_parent and not x_parent):
            # If only one of them is found at this level, they are not cousins
            return False

    return False

# Example usage
if __name__ == "__main__":
    # Construct the tree:
    #        1
    #       / \
    #      2   3
    #     /     \
    #    4       5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Check if nodes 4 and 5 are cousins
    print(are_cousins(root, 4, 5))  # Output: True
```

### Key Points:

- The **BFS approach** ensures that we traverse the tree level by level, allowing us to efficiently determine if two nodes are at the same level.
- By keeping track of each node's parent, we can determine if nodes have different parents, which is crucial for determining if they are cousins.
- **Time Complexity**: **O(N)**, where **N** is the number of nodes in the tree, as each node is visited once.
- **Space Complexity**: **O(N)**, due to the use of the queue to store nodes for level-order traversal.

This approach provides a clear way to determine if two nodes are cousins by leveraging level-order traversal and tracking parent nodes.

### Binary Tree Level Order Traversal II: Explanation and Python Solution

The problem **"Binary Tree Level Order Traversal II"** is a variation of level order traversal where the nodes of a binary tree are traversed level by level, but the result should be returned in reverse order, starting from the bottom-most level to the root. 

In other words, you need to do a bottom-up level order traversal.

#### Numeric Example:

Consider the following binary tree:

```
       1
      / \
     2   3
    / \   \
   4   5   6
```

The **level order traversal** from top to bottom would be: `[1], [2, 3], [4, 5, 6]`. 

The **bottom-up level order traversal** would be: `[[4, 5, 6], [2, 3], [1]]`.

### Python Solution with Explanation

Here is a Python implementation for bottom-up level order traversal using Breadth-First Search (BFS) with detailed comments:

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal_ii(root):
    # Edge case: if the tree is empty
    if not root:
        return []

    # Result list to store the level order traversal in reverse order
    result = []

    # Initialize a queue and enqueue the root node
    queue = deque([root])

    # Continue until all nodes are processed
    while queue:
        # Number of nodes at the current level
        level_size = len(queue)
        # List to store current level's nodes
        current_level = []

        # Iterate over all nodes at the current level
        for _ in range(level_size):
            current_node = queue.popleft()  # Pop the front element
            current_level.append(current_node.val)  # Process the current node

            # Add left child to queue if it exists
            if current_node.left:
                queue.append(current_node.left)
            # Add right child to queue if it exists
            if current_node.right:
                queue.append(current_node.right)

        # Insert the current level at the beginning of the result list
        result.insert(0, current_level)

    return result

# Example usage
if __name__ == "__main__":
    # Construct the tree: 
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # Print bottom-up level order traversal
    print(level_order_traversal_ii(root))
```

### Key Points:

- The **BFS approach** is used here to traverse the tree level by level.
- Instead of appending the level at the end of the result list, each level is **inserted at the beginning** of the result list (`result.insert(0, current_level)`) to create the bottom-up order.
- **Time Complexity**: **O(N)**, where **N** is the number of nodes in the tree, as each node is processed exactly once.
- **Space Complexity**: **O(N)**, primarily due to storing nodes in the queue and the final result list.

This approach effectively allows us to get the desired order of levels in reverse, providing a solution for the bottom-up level order traversal problem.


### Problem: Maximum Width of Binary Tree

The problem **"Maximum Width of Binary Tree"** requires finding the maximum width of a binary tree. The width of a level is defined as the number of nodes between the leftmost and rightmost nodes, including any `null` nodes in between.

#### Numeric Example:

Consider the following binary tree:

```
       1
      / \
     3   2
    /     \
   5       9
  / \     / \
 6   7   8  10
```

The **width of each level** in the tree is as follows:
- Level 1: `[1]` has a width of `1`.
- Level 2: `[3, 2]` has a width of `2`.
- Level 3: `[5, null, null, 9]` has a width of `4`.
- Level 4: `[6, 7, 8, 10]` has a width of `4`.

Thus, the **maximum width** of this binary tree is `4`.

### Python Solution with Explanation

To solve this problem, we use a Breadth-First Search (BFS) approach to traverse the tree level by level. While traversing, we track the position (or index) of each node to calculate the width of each level.

Here's the Python implementation:

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_width_of_binary_tree(root):
    # Edge case: if the tree is empty
    if not root:
        return 0

    # Initialize a queue to perform level-order traversal
    # Each element is a tuple (node, index)
    queue = deque([(root, 0)])
    max_width = 0

    # Perform BFS to traverse nodes level by level
    while queue:
        level_length = len(queue)
        # Record the indices of the first and last nodes at the current level
        _, first_index = queue[0]
        _, last_index = queue[-1]
        
        # Calculate the width of the current level
        current_width = last_index - first_index + 1
        # Update the maximum width
        max_width = max(max_width, current_width)

        # Iterate through all nodes at the current level
        for _ in range(level_length):
            current_node, index = queue.popleft()

            # Add left child to the queue if it exists with its index
            if current_node.left:
                queue.append((current_node.left, 2 * index))
            # Add right child to the queue if it exists with its index
            if current_node.right:
                queue.append((current_node.right, 2 * index + 1))

    return max_width

# Example usage
if __name__ == "__main__":
    # Construct the tree:
    #        1
    #       / \
    #      3   2
    #     /     \
    #    5       9
    #   / \     / \
    #  6   7   8  10
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.right.right = TreeNode(9)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.right.right.left = TreeNode(8)
    root.right.right.right = TreeNode(10)

    # Print the maximum width of the binary tree
    print(max_width_of_binary_tree(root))  # Output: 4
```

### Key Points:

- **Indexing Strategy**:
  - We use an indexing strategy where the root starts at index `0`.
  - For each node with index `i`:
    - The left child gets index `2 * i`.
    - The right child gets index `2 * i + 1`.
  - This allows us to calculate the width of each level as the difference between the first and last node indices plus one.
- **BFS Approach**:
  - BFS ensures that nodes are processed level by level, which is essential for calculating the width of each level.
- **Time Complexity**: **O(N)**, where **N** is the number of nodes in the tree, as each node is visited exactly once.
- **Space Complexity**: **O(N)**, due to the use of the queue for storing nodes for level-order traversal.

This approach effectively allows us to determine the maximum width of a binary tree, even in cases where nodes are missing, by leveraging level-wise traversal and keeping track of the position indices.


### Explanation of "Binary Tree Vertical Order Traversal"

**Binary Tree Vertical Order Traversal** is a method used to traverse a binary tree by grouping nodes based on their vertical levels when viewed from top to bottom. Each vertical level is a line that runs vertically from the top of the tree to the bottom, passing through nodes that are aligned in the same direction.

In vertical order traversal, nodes are grouped and printed level-wise from the leftmost vertical line to the rightmost vertical line.

#### How Vertical Order is Determined:
- We assign a **vertical index** to each node in the tree. 
  - The **root** node starts with a vertical index of `0`.
  - For each **left child**, the vertical index is decreased by `1`.
  - For each **right child**, the vertical index is increased by `1`.
- Nodes with the same vertical index are part of the same vertical level.

#### Example:
Consider the following binary tree:
```
       1
      / \
     2   3
    / \   \
   4   5   6
```

The **vertical order traversal** for this tree would be:
- Vertical level -2: `[4]`
- Vertical level -1: `[2]`
- Vertical level 0: `[1, 5]`
- Vertical level 1: `[3]`
- Vertical level 2: `[6]`

**Output:** `[[4], [2], [1, 5], [3], [6]]`

This traversal helps to group nodes that are aligned vertically and is often used in graphical representations or when solving problems that require nodes to be grouped by their relative positions.

Here is the Python code for "Binary Tree Vertical Order Traversal" explained in comments:

```python
# Import the necessary modules
from collections import deque, defaultdict

# Define the TreeNode class to represent a node of the binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # Value of the node
        self.left = left      # Reference to the left child node
        self.right = right    # Reference to the right child node

# Define the function to perform vertical order traversal
def vertical_order_traversal(root):
    # If the tree is empty, return an empty list
    if not root:
        return []

    # Dictionary to store nodes at each vertical level
    # Keys are vertical levels, and values are lists of node values
    vertical_map = defaultdict(list)

    # Initialize a queue for level-order traversal
    # Each element is a tuple (node, vertical_level)
    queue = deque([(root, 0)])

    # Perform BFS to traverse nodes and group them by vertical levels
    while queue:
        # Pop the front element from the queue (node and its vertical level)
        current_node, vertical_level = queue.popleft()

        # Add the current node's value to the list corresponding to its vertical level
        vertical_map[vertical_level].append(current_node.val)

        # If the current node has a left child, add it to the queue with vertical_level - 1
        if current_node.left:
            queue.append((current_node.left, vertical_level - 1))

        # If the current node has a right child, add it to the queue with vertical_level + 1
        if current_node.right:
            queue.append((current_node.right, vertical_level + 1))

    # Sort the vertical levels and prepare the final result list
    # Sort the keys of vertical_map and gather all nodes for each vertical level
    sorted_vertical_levels = sorted(vertical_map.keys())
    result = [vertical_map[level] for level in sorted_vertical_levels]

    # Return the result list
    return result

# Example usage of the vertical order traversal function
if __name__ == "__main__":
    # Construct the binary tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = TreeNode(1)                      # Root node with value 1
    root.left = TreeNode(2)                 # Left child of root with value 2
    root.right = TreeNode(3)                # Right child of root with value 3
    root.left.left = TreeNode(4)            # Left child of node 2 with value 4
    root.left.right = TreeNode(5)           # Right child of node 2 with value 5
    root.right.right = TreeNode(6)          # Right child of node 3 with value 6

    # Perform vertical order traversal and print the result
    print(vertical_order_traversal(root))   # Output: [[4], [2], [1, 5], [3], [6]]
```

### Summary of Code:
- **TreeNode Class**: Represents each node in the binary tree, having a value (`val`), a left child (`left`), and a right child (`right`).
- **vertical_order_traversal Function**:
  - If the tree is empty, returns an empty list.
  - Uses a `defaultdict` to store nodes at each vertical level.
  - Uses a `deque` for BFS traversal, storing nodes along with their vertical levels.
  - Populates the `vertical_map` dictionary with nodes grouped by their vertical levels.
  - Finally, sorts the dictionary keys (i.e., vertical levels) to produce the result list.
- **Example Usage**:
  - Constructs the binary tree as shown.
  - Calls `vertical_order_traversal()` to perform the traversal and prints the vertical order.

This code effectively demonstrates how to perform a vertical order traversal of a binary tree using a BFS approach with a `deque` and a `defaultdict` to group nodes according to their vertical levels.