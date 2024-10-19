# Tree Depth First Search (DFS) Overview

Tree Depth First Search (DFS) is a technique used to traverse trees or graphs by exploring each branch as deeply as possible before backtracking. In trees, this approach allows you to fully explore a node's descendants before moving to another branch. DFS is particularly effective for problems where you need to visit all nodes, find paths, or reach specific leaf nodes to apply conditions or calculations.

## Different Tree Traversal Techniques

Tree traversal techniques are used to explore or visit all the nodes in a tree. Here are some common traversal techniques:

### Depth First Search (DFS)

DFS explores as far as possible along each branch before backtracking. It has three main types:

1. **Preorder Traversal (Root-Left-Right)**: Visit the root node first, then recursively visit the left subtree, followed by the right subtree. For example, in the tree below:

```
    1
   / \
  2   3
 / \
4   5
```

The Preorder Traversal would be: 1, 2, 4, 5, 3.

2. **In-order Traversal (Left-Root-Right)**: Recursively visit the left subtree, then visit the root node, and finally the right subtree. This traversal is particularly useful for binary search trees to retrieve nodes in sorted order.

For example, in the tree below:

```
    1
   / \
  2   3
 / \
4   5
```

The In-order Traversal would be: 4, 2, 5, 1, 3.

3. **Post-order Traversal (Left-Right-Root)**: Recursively visit the left subtree, then the right subtree, and finally visit the root node. This is useful for deleting nodes in a tree.

For example, in the tree below:

```
    1
   / \
  2   3
 / \
4   5
```

The Post-order Traversal would be: 4, 5, 2, 3, 1.

### Breadth First Search (BFS)

BFS explores nodes **level by level**, from top to bottom. It uses a **queue** to keep track of nodes at each level and is useful for finding the shortest path in unweighted graphs or trees.

## Checklist to Determine if a Problem Belongs to Tree DFS

| Checklist Criteria            | Example                                                                                                                                                                      | Interview Question Example                                                                           |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Traversal or Path Search**  | The problem asks for traversing the entire tree or finding specific paths.                                                                                                   | **Question**: Given a binary tree, write a function that prints the preorder traversal of its nodes. |
| **All Possible Solutions**    | The problem involves finding all possible solutions rather than just one (e.g., all root-to-leaf paths).                                                                     | **Question**: Given a binary tree, find all paths from the root to the leaf nodes.                   |
| **Recursive Structure**       | Trees naturally have recursive structures, so problems that can be broken down into smaller subproblems (e.g., solving the problem for left and right subtrees) may use DFS. | **Question**: Given a binary tree, write a function that computes the maximum depth of the tree.     |
| **Path-Related Computations** | Problems where conditions depend on paths from root to nodes, such as path sums, longest paths, etc., are good candidates for DFS.                                           | **Question**: Find if there is a root-to-leaf path in a binary tree with a given sum.                |

## Tree DFS Templates

Tree DFS can be implemented in three common ways: using recursion, using an iterative approach with a stack, or using Morris Traversal for in-order without extra space. Below, the first two templates are described:

### Recursive DFS Template

The recursive approach to DFS is natural for tree structures, as each node's children can be explored through successive recursive calls. Here's a basic recursive template for Tree DFS:

```python
# Recursive DFS Template
# PRE-ORDER traversal

def dfs_recursive(node):
    if node is None:
        return

    # Process the current node (if required)
    process_node(node)

    # Traverse the left subtree
    dfs_recursive(node.left)

    # Traverse the right subtree
    dfs_recursive(node.right)

# Time Complexity: O(N) - where N is the number of nodes in the tree, as each node is visited once.
# Space Complexity: O(H) - where H is the height of the tree, due to the recursion stack.
```

### Iterative DFS Template (Using Stack)

The iterative approach uses an explicit stack to simulate the recursive calls. This is useful when you want to avoid Python's recursion depth limitations.

#### Space and Time Complexity

- **Time Complexity**: O(N), where N is the number of nodes in the tree, as each node is visited once.
- **Space Complexity**: O(H), where H is the height of the tree. In the worst case, the height can be equal to the number of nodes (O(N)) for skewed trees. 

```python
# Iterative DFS using a Stack
# Preorder traversal

def dfs_iterative(root):
    if root is None:
        return

    stack = [(root, [root.val])]
    while stack:
        node, path = stack.pop()

        # If it's a leaf node, perform any specific operation
        if not node.left and not node.right:
            process_path(path)

        # Traverse the right and left child (right first, so that left is processed first)
        if node.right:
            stack.append((node.right, path + [node.right.val]))
        if node.left:
            stack.append((node.left, path + [node.left.val]))
```

The basic structure usually involves traversing to the left child and right child, then backtracking to undo changes for the current node to reset for the next traversal.

## Examples of Problems Using Tree DFS

### Example 1: Path Sum (Using Recursive Template)

**Problem Statement**: Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

**Recursive Approach**:

```python
# Recursive DFS for Path Sum

def has_path_sum_recursive(node, target_sum):
    if node is None:
        return False

    # If it's a leaf node, check if the path sum equals the target sum
    if not node.left and not node.right and target_sum == node.val:
        return True

    # Recurse down to left and right children with updated sum
    return (has_path_sum_recursive(node.left, target_sum - node.val) or
            has_path_sum_recursive(node.right, target_sum - node.val))
```

### Example 2: All Paths From Root to Leaf (Using Recursive and Iterative Templates)

**Problem Statement**: Given a binary tree, return all root-to-leaf paths.

**Recursive Approach**:

```python
# Recursive DFS for All Paths From Root to Leaf

def all_paths_recursive(node):
    def dfs(node, path, result):
        if node is None:
            return

        path.append(str(node.val))

        # If it's a leaf node, add the path to the result
        if not node.left and not node.right:
            result.append("->".join(path))
        else:
            dfs(node.left, path, result)
            dfs(node.right, path, result)

        # Backtrack
        path.pop()

    result = []
    dfs(node, [], result)
    return result
```

**Iterative Approach**:

```python
# Iterative DFS for All Paths From Root to Leaf

def all_paths_iterative(root):
    if root is None:
        return []

    stack = [(root, [str(root.val)])]
    result = []

    while stack:
        node, path = stack.pop()

        if not node.left and not node.right:
            result.append("->".join(path))

        if node.right:
            stack.append((node.right, path + [str(node.right.val)]))
        if node.left:
            stack.append((node.left, path + [str(node.left.val)]))

    return result
```

**Numeric Example**:
Consider the following binary tree:

```
    1
   / \
  2   3
 / \
4   5
```

- **Recursive Approach**: The paths from root to leaf are: `1->2->4`, `1->2->5`, and `1->3`.
- **Iterative Approach**: Using the stack, we get the same paths: `1->2->4`, `1->2->5`, and `1->3`.

### Example 3: Maximum Path Sum (Using Recursive Template)

**Problem Statement**: Find the maximum path sum in a binary tree. The path can start and end at any node.

**Recursive Approach**:

```python
# Recursive DFS for Maximum Path Sum

def max_path_sum_recursive(root):
    def dfs(node):
        nonlocal max_sum
        if node is None:
            return 0

        # Calculate the maximum path sum for the left and right children
        left_max = max(dfs(node.left), 0)
        right_max = max(dfs(node.right), 0)

        # Update the global maximum path sum
        current_sum = node.val + left_max + right_max
        max_sum = max(max_sum, current_sum)

        # Return the maximum gain from continuing the path
        return node.val + max(left_max, right_max)

    max_sum = float('-inf')
    dfs(root)
    return max_sum
```

## Key Takeaways for Tree DFS

- **Template Usage**: The basic template for DFS remains similar across problems; however, specifics like how to process nodes, the conditions for leaf nodes, and what to do during backtracking will change.
- **Recursive vs Iterative**: Recursive solutions are more natural for trees, but iterative solutions can avoid recursion limits in Python.
- **Path Storage**: Often, DFS requires storing the current path, especially if the problem requires outputting or processing the path from the root to a leaf node.
- **Global Variables**: For problems like finding the maximum path sum, a global variable (`nonlocal` or a class-level variable) is often used to track the maximum value across all recursive calls.

## Practice Problems

| S.No | Question                                                                                         | Numeric Example                                 | Difficulty Level | Approach            |
| ---- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------- | ---------------- | ------------------- |
| 1    | Path Sum II: Find all paths from root to leaf that sum to a given value.                         | Given tree: `1 -> 2 -> 4, 5; 1 -> 3` with sum 7 | Medium           | Recursive/Iterative |
| 2    | Diameter of Binary Tree: Use DFS to calculate the diameter (longest path between any two nodes). | Binary tree with nodes `1, 2, 3, 4, 5`          | Medium           | Recursive           |
| 3    | Lowest Common Ancestor: Find the lowest common ancestor of two nodes in a binary tree using DFS. | Nodes `4 and 5` in a tree `1, 2, 3, 4, 5`       | Medium           | Recursive           |
| 4    | Binary Tree Maximum Path Sum                                                                     | Find max path in tree `1 -> 2 -> 3, 4 -> 5`     | Hard             | Recursive           |
| 5    | Binary Tree All Paths                                                                            | Find all paths in tree `1 -> 2 -> 4, 5; 1 -> 3` | Easy             | Recursive/Iterative |
| 6    | Count Good Nodes in Binary Tree                                                                  | Count good nodes in tree `3 -> 1 -> 4, 5`                                  | Medium           | Recursive/Iterative |
| 7    | Binary Tree Right Side View                                                                      | Find right side view of tree `1 -> 2, 3 -> 4, 5`                           | Medium           | Iterative           |
| 8    | Flatten Binary Tree to Linked List                                                               | Flatten tree `1 -> 2, 3 -> 4, 5, 6` to linked list                         | Medium           | Recursive           |
| 9    | Sum Root to Leaf Numbers                                                                         | Calculate sum of all numbers from root to leaf in tree `1 -> 2, 3 -> 4, 5` | Medium           | Recursive/Iterative |
| 10   | Validate Binary Search Tree                                                                      | Validate if tree `2 -> 1, 3` is a BST                                      | Medium           | Recursive/Iterative |

------------------------------------------------------

**Path Sum II: Find all paths from root to leaf that sum to a given value**

To solve the **Path Sum II** problem, the goal is to find **all paths** in a binary tree where the sum of the nodes along each path is equal to a given target value. Unlike the basic path sum problem, this requires capturing **all possible root-to-leaf paths** that match the sum condition.

### **Numeric Example**
Consider the following binary tree:
```
    5
   / \
  4   8
 /   / \
11  13  4
/ \      \
7  2      1
```
- **Target Sum**: 22

- **Paths that meet the sum**:
  - `5 -> 4 -> 11 -> 2`
  - `5 -> 8 -> 4 -> 5`

### **Recursive Approach**
This approach uses Depth First Search (DFS) recursively, starting from the root node. It keeps track of the current path and checks at each leaf node if the path sum equals the target sum.

```python
# Recursive DFS for Path Sum II

def path_sum_recursive(node, target_sum):
    def dfs(node, current_path, remaining_sum):
        if node is None:
            return

        # Add the current node to the path
        current_path.append(node.val)

        # If it's a leaf node and the remaining sum equals the node's value
        if not node.left and not node.right and remaining_sum == node.val:
            result.append(list(current_path))
        else:
            # Recurse to left and right children with updated remaining sum
            dfs(node.left, current_path, remaining_sum - node.val)
            dfs(node.right, current_path, remaining_sum - node.val)

        # Backtrack: remove the current node from the path
        current_path.pop()

    result = []
    dfs(node, [], target_sum)
    return result
```

### **Iterative Approach**
This approach uses an **explicit stack** to simulate the recursive calls and to store paths. Each entry in the stack stores the current node, the path leading to it, and the remaining target sum.

```python
# Iterative DFS for Path Sum II

def path_sum_iterative(root, target_sum):
    if root is None:
        return []

    stack = [(root, [root.val], target_sum - root.val)]
    result = []

    while stack:
        node, current_path, remaining_sum = stack.pop()

        # If it's a leaf node and the remaining sum equals zero, add the path to the result
        if not node.left and not node.right and remaining_sum == 0:
            result.append(list(current_path))

        # Traverse right and left child (right first, so left is processed first)
        if node.right:
            stack.append((node.right, current_path + [node.right.val], remaining_sum - node.right.val))
        if node.left:
            stack.append((node.left, current_path + [node.left.val], remaining_sum - node.left.val))

    return result
```
------------

**Diameter of Binary Tree: Use DFS to calculate the diameter (longest path between any two nodes)**

In the context of a binary tree, the **diameter** is defined as the **longest path between any two nodes**. This path may or may not pass through the root of the tree. The diameter is not simply the height of the tree but can be calculated by measuring the length of the longest possible path.

### **How DFS Helps Calculate Diameter**

1. **DFS Traversal**: To find the diameter, you can use **Depth First Search (DFS)** to recursively compute the height of each subtree.
2. **Tracking the Longest Path**: At each node, the diameter could be the longest path through that node, which is calculated by adding the heights of its left and right subtrees.
3. **Global Maximum**: To determine the overall diameter, a **global variable** is maintained and updated whenever a new maximum path length is found.

### **Approach**
1. Traverse the entire tree using DFS.
2. For each node, calculate:
   - **Height of the left subtree**.
   - **Height of the right subtree**.
3. **Diameter through the current node**: This is the sum of the left and right subtree heights.
4. Update the global maximum diameter with the current value if it is larger.

### **Recursive Implementation Example**
```python
# Recursive DFS to calculate the diameter of a binary tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root):
    def dfs(node):
        nonlocal diameter
        if node is None:
            return 0

        # Recursively calculate the height of left and right subtrees
        left_height = dfs(node.left)
        right_height = dfs(node.right)

        # Update the global diameter (the longest path through the current node)
        diameter = max(diameter, left_height + right_height)

        # Return the height of the subtree rooted at this node
        return 1 + max(left_height, right_height)

    diameter = 0
    dfs(root)
    return diameter


# Example
# Consider the following binary tree:
#     1
#    / \
#   2   3
#  / \
# 4   5
# The diameter of this tree is 3 (path: 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameter_of_binary_tree(root))  # Output: 3
```

In this example:
- The **diameter** of a binary tree is measured in **edges**, not nodes.
- The **diameter** is the longest path, which is `3` (either from `4 -> 2 -> 1 -> 3` or from `5 -> 2 -> 1 -> 3`).
- The **DFS** helps efficiently calculate both the height of each subtree and track the maximum diameter throughout the traversal. 

The recursive approach makes it easy to explore each subtree, calculate the required heights, and update the global maximum for the diameter in one traversal.