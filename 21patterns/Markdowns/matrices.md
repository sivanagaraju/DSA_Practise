### Comprehensive Guide for Matrices Coding Patterns in Interviews

#### 1. **Core Concepts and Coding Patterns**

Matrices are two-dimensional arrays, often used to represent grids, graphs, or tables of data. They serve as a fundamental data structure for solving problems involving pathfinding, image processing, or geometric manipulations. Core coding patterns for matrices include:

- **Traversal**: Moving through all or selected elements in the matrix.
- **Search and Modification**: Finding a particular value or performing updates.
- **Dynamic Programming on Matrices**: Solving problems such as pathfinding with optimal substructure properties.
- **Backtracking**: For problems like finding all paths or combinations.

Typical use cases involve grid-based games, connectivity problems (like number of islands), or minimal path cost problems.

#### 2. **Examples**

- **Traversal Example**: Given a 3x3 matrix, traverse all elements in row-major order.
  ```
  Matrix:  
  [1, 2, 3]  
  [4, 5, 6]  
  [7, 8, 9]  
  Output: 1, 2, 3, 4, 5, 6, 7, 8, 9
  ```
- **Pathfinding Example**: Minimum path sum from top-left to bottom-right of a matrix where movement is restricted to right and down.
  ```
  Matrix:  
  [1, 3, 1]  
  [1, 5, 1]  
  [4, 2, 1]  
  Output: 7 (Path: 1 → 3 → 1 → 1 → 1)
  ```

#### 3. **Problem Identification Checklist**

To determine if a problem can be solved using matrices, ask:

1. Is the data organized in a grid or 2D form?
2. Are you required to find a path from one cell to another?
3. Is there a need to modify values based on neighboring cells?

| Problem Type        | Example Problem                     | Matrix Representation Indicator                                    |
| ------------------- | ----------------------------------- | ------------------------------------------------------------------ |
| Pathfinding         | Find the shortest path in a 2D grid | Data is represented in a matrix, movement constrained by neighbors |
| Dynamic Programming | Calculate the minimal path sum      | Optimal substructure with grid-based decisions                     |

#### 4. **General Templates with Comments**

##### **Template 1: Matrix Traversal**

```python
# Traverse a matrix row-wise and column-wise
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(matrix)
cols = len(matrix[0])

# Row-wise traversal
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j])
```

**Use Case**: Useful when you need to look at all cells in the matrix, such as calculating the sum of all elements.

##### **Template 2: Backtracking in Matrix**

```python
# Backtracking example: finding all paths from top-left to bottom-right
# Restrictions: Only move right or down

def find_paths(matrix, row, col, path):
    if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
        print(path)
        return
    if row + 1 < len(matrix):
        find_paths(matrix, row + 1, col, path + [(row + 1, col)])
    if col + 1 < len(matrix[0]):
        find_paths(matrix, row, col + 1, path + [(row, col + 1)])

find_paths([[1, 2], [3, 4]], 0, 0, [(0, 0)])
```

**Use Case**: Typically used in problems involving exploration of all possible paths, such as "find all paths from source to destination".

#### 5. **Complexity Analysis**

- **Time Complexity**:
  - For traversal: , where m and n are the dimensions of the matrix.
  - For backtracking:  in the worst case as we explore all possible paths.
- **Space Complexity**:
  - For traversal:  (excluding input matrix).
  - For backtracking:  due to the recursion stack.
- **Optimization Opportunities**: Dynamic programming can be applied to avoid recalculating overlapping subproblems, reducing time complexity.

#### 6. **Discussion on Templates and Patterns**

Different problems require different matrix patterns. For example, pathfinding problems may need dynamic programming, while problems with obstacles may require BFS/DFS. Adjustments like memoization or pruning unneeded paths can be applied depending on the specific problem constraints.

#### 7. **Multiple Approaches and Implementations**

- **Iterative vs Recursive**: Traversing a matrix can be done iteratively with loops or recursively using DFS.
- **Comparative Analysis**: Iterative solutions often use less space than recursive ones due to avoiding stack overhead, while recursive solutions can be more elegant for backtracking.

#### 9. **Practice Problems**

| S.No | Question                                     | Example Explanation                                                                                                                                                                                                                                                                  | Difficulty Level | Approach                                                                                     |
| ---- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------- |
| 1    | Find the minimum path sum in a matrix        | Given Matrix: [ [1, 3, 1], [1, 5, 1], [4, 2, 1] ]Example Path: Start at (0,0) with value 1 → move right to (0,1) with value 3 → move right to (0,2) with value 1 → move down to (1,2) with value 1 → move down to (2,2) with value 1.Total Path Sum = 1 + 3 + 1 + 1 + 1 = 7Output: 7 | Medium           | Dynamic Programming (using a 2D DP array to store minimal path sums for each cell)           |
| 2    | Find all paths from top-left to bottom-right | Given Matrix: [ [1, 2], [3, 4] ]Example Paths: Path 1: Start at (0,0) → move down to (1,0) → move right to (1,1). Path 2: Start at (0,0) → move right to (0,1) → move down to (1,1).Output: [(0,0)→(1,0)→(1,1)], [(0,0)→(0,1)→(1,1)]                                                 | Medium           | Backtracking (using recursion to explore all paths with an extra list to store current path) |
| 3    | Count number of islands                      | Given Binary Matrix: [ [1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 1], [1, 0, 1, 1] ]Explanation: Island 1: Cells (0,0), (0,1), (1,0). Island 2: Cell (1,3). Island 3: Cells (2,2), (2,3), (3,2), (3,3). Island 4: Cell (3,0).Total Number of Islands: 4Output: 4                          | Hard             | DFS/BFS traversal (using a visited set to keep track of visited cells)                       |
| 4    | Find the longest increasing path in a matrix | Given Matrix: [ [9, 9, 4], [6, 6, 8], [2, 1, 1] ]Explanation: One of the longest increasing paths is 1 → 2 → 6 → 9.Output: Length = 4                                                                                                                                                | Hard             | DFS with memoization (using a cache to store results of previously computed paths)           |
| 5    | Rotting Oranges                              | Given Matrix: [ [2, 1, 1], [1, 1, 0], [0, 1, 1] ]Explanation: Use BFS to find the time taken for all fresh oranges to rot.Output: 4                                                                                                                                              | Medium           | BFS (using a queue to track rotting process level by level)                                  |
| 6    | Word Search in Matrix                        | Given Matrix: [ ["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"] ], Word: "ABCCED"Explanation: Use backtracking to find the word in the matrix.Output: True                                                                                                                                      | Medium           | Backtracking (recursively exploring all paths to match the word)                             |
| 7    | Unique Paths in a Grid                       | Grid Size: 3x7Explanation: Calculate the number of unique paths from top-left to bottom-right.Output: 28                                                                                                                                                                      | Easy             | Dynamic Programming (using a 2D array to count paths)                                       |
| 8    | Search a 2D Matrix                           | Given Matrix: [ [1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60] ], Target: 3Explanation: Search for the target in the matrix.Output: True                                                                                                                                    | Medium           | Binary Search (treat the matrix as a sorted 1D array)                                       |
| 9    | Flood Fill Algorithm                         | Given Image: [ [1, 1, 1], [1, 1, 0], [1, 0, 1] ], Starting Pixel: (1,1), New Color: 2Explanation: Replace all connected 1s starting from (1,1) with 2.Output: [ [2, 2, 2], [2, 2, 0], [2, 0, 1] ]                                                                               | Easy             | DFS/BFS (to explore all connected pixels)                                                   |
| 10   | Maximum Size Square Sub-matrix of 1s        | Given Binary Matrix: [ [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1] ]Explanation: Find the largest square containing only 1s.Output: 3 (size of the square)                                                                                                        | Medium           | Dynamic Programming (using a 2D DP array to track the size of the largest square ending at each cell) |
| 11   | Spiral Order of Matrix                       | Given Matrix: [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]Explanation: Traverse the matrix in a spiral order.Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]                                                                                                                                      | Easy             | Iterative Traversal (using boundaries to keep track of the spiral)                          |
| 12   | Kth Smallest Element in a Sorted Matrix      | Given Matrix: [ [1, 5, 9], [10, 11, 13], [12, 13, 15] ], k = 8Explanation: Find the kth smallest element in the sorted matrix.Output: 13                                                                                                                                    | Medium           | Min-Heap (pushing elements row-wise into the heap)                                          |
| 13   | Set Matrix Zeroes                            | Given Matrix: [ [1, 1, 1], [1, 0, 1], [1, 1, 1] ]Explanation: Set entire row and column to 0 if an element is 0.Output: [ [1, 0, 1], [0, 0, 0], [1, 0, 1] ]                                                                                                                   | Medium           | Constant Space Approach (using first row and column as markers)                             |
| 14   | Matrix Rotation (90 Degrees)                 | Given Matrix: [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]Explanation: Rotate the matrix by 90 degrees clockwise.Output: [ [7, 4, 1], [8, 5, 2], [9, 6, 3] ]                                                                                                                           | Medium           | Transpose and Reverse Approach                                                              |
| 15   | Search in a Row-wise and Column-wise Sorted Matrix | Given Matrix: [ [1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17] ], Target: 5Explanation: Search for the target in the sorted matrix.Output: True                                                                                                    | Medium           | Start from Top-Right (eliminating rows or columns based on comparison)                      |
| 16   | Find Peak Element in a 2D Matrix             | Given Matrix: [ [10, 20, 15], [21, 30, 14], [7, 16, 32] ]Explanation: Find a peak element (greater than its neighbors).Output: 30                                                                                                                                            | Hard             | Divide and Conquer (similar to binary search approach)                                      |
| 17   | Minimum Cost Path in a Grid                  | Given Grid: [ [1, 2, 3], [4, 8, 2], [1, 5, 3] ]Explanation: Find the minimum cost to reach the bottom-right from top-left.Output: 8                                                                                                                                         | Medium           | Dynamic Programming (using a 2D DP array to store minimal costs)                           |
| 18   | Sudoku Solver                                | Given Partially Filled 9x9 GridExplanation: Fill the grid such that every row, column, and 3x3 box contains the numbers 1 to 9.Output: Completed Sudoku Grid                                                                                                                | Hard             | Backtracking (trying all possibilities and reverting if a conflict occurs)                  |
| 19   | Maximum Gold Path                            | Given Grid: [ [1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20] ]Explanation: Find the maximum amount of gold that can be collected starting from any cell.Output: 28                                                                                                 | Medium           | DFS (exploring all paths and keeping track of collected gold)                               |
| 20   | Shortest Bridge                              | Given Binary Matrix: [ [0, 1], [1, 0] ]Explanation: Connect two islands by flipping the minimum number of 0s to 1s.Output: 1                                                                                                                                                | Hard             | BFS (to expand one island and find the shortest path to the other)                          |


#### 10. **Key Takeaways, Tips, and Summary**

- **Key Takeaways**: Matrices are versatile and can represent a variety of problems involving grids.
- **Practical Tips**: Always start by identifying if a problem involves a 2D grid, then choose the right pattern such as traversal, backtracking, or dynamic programming.
- **Summary**: Matrices are a powerful tool for grid-based problems, and applying the correct template requires identifying the problem's structure and constraints.

#### 11. **Common Pitfalls**

- **Mistakes to Avoid**: Not considering boundary conditions (e.g., going out of the matrix bounds).
- **Troubleshooting Tips**: Use print statements to check traversal paths or track recursive calls to identify incorrect movement or conditions.

Here are detailed explanations of 7 randomly selected questions from the practice problems:

### 1. **Find the Minimum Path Sum in a Matrix**
**Problem**: Given a matrix, find the minimum path sum from the top-left to the bottom-right, where you can only move right or down.

**Example**:
- Given Matrix:
  ```
  [1, 3, 1]
  [1, 5, 1]
  [4, 2, 1]
  ```
- Start at (0,0) with value `1`, move right to (0,1) with value `3`, move right to (0,2) with value `1`, move down to (1,2) with value `1`, and finally move down to (2,2) with value `1`.
- **Total Path Sum**: 1 + 3 + 1 + 1 + 1 = **7**

**Python Code**:
```python
def min_path_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = matrix[0][0]

    # Initialize the first row and first column
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]

    # Fill the rest of dp array
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]

matrix = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(min_path_sum(matrix))  # Output: 7
```

### 2. **Count Number of Islands**
**Problem**: Given a binary matrix representing a grid of water (`0`) and land (`1`), find the number of distinct islands.

**Example**:
- Given Matrix:
  ```
  [1, 1, 0, 0]
  [1, 0, 0, 1]
  [0, 0, 1, 1]
  [1, 0, 1, 1]
  ```
- **Number of Islands**: 4
  - Island 1: (0,0), (0,1), (1,0)
  - Island 2: (1,3)
  - Island 3: (2,2), (2,3), (3,2), (3,3)
  - Island 4: (3,0)

**Python Code**:
```python
def num_islands(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return
        grid[i][j] = 0
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1

    return count

grid = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 1], [1, 0, 1, 1]]
print(num_islands(grid))  # Output: 4
```

### 3. **Rotting Oranges**
**Problem**: Given a 2D grid where `2` represents a rotten orange, `1` represents a fresh orange, and `0` is an empty cell. Each minute, rotten oranges rot their adjacent fresh oranges. Determine how many minutes until no fresh oranges are left.

**Example**:
- Given Matrix:
  ```
  [2, 1, 1]
  [1, 1, 0]
  [0, 1, 1]
  ```
- **Output**: 4 (all fresh oranges will be rotten after 4 minutes)

**Python Code**:
```python
from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh_oranges += 1

    minutes_passed = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        r, c, minutes = queue.popleft()
        minutes_passed = max(minutes_passed, minutes)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_oranges -= 1
                queue.append((nr, nc, minutes + 1))

    return minutes_passed if fresh_oranges == 0 else -1

grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(oranges_rotting(grid))  # Output: 4
```

### 4. **Flood Fill Algorithm**
**Problem**: Given a 2D grid, replace all connected cells of a given color starting from a given pixel with a new color.

**Example**:
- Given Image:
  ```
  [1, 1, 1]
  [1, 1, 0]
  [1, 0, 1]
  ```
- Starting Pixel: `(1,1)`, New Color: `2`
- **Output**:
  ```
  [2, 2, 2]
  [2, 2, 0]
  [2, 0, 1]
  ```

**Python Code**:
```python
def flood_fill(image, sr, sc, new_color):
    original_color = image[sr][sc]
    if original_color == new_color:
        return image

    def dfs(r, c):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original_color:
            return
        image[r][c] = new_color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image

image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(flood_fill(image, 1, 1, 2))  # Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
```

### 5. **Unique Paths in a Grid**
**Problem**: Given a grid of size `m x n`, find the number of unique paths from the top-left to the bottom-right corner, only moving down or right.

**Example**:
- Grid Size: `3x7`
- **Output**: `28`

**Python Code**:
```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]

print(unique_paths(3, 7))  # Output: 28
```

### 6. **Set Matrix Zeroes**
**Problem**: Given an `m x n` matrix, if an element is `0`, set its entire row and column to `0`.

**Example**:
- Given Matrix:
  ```
  [1, 1, 1]
  [1, 0, 1]
  [1, 1, 1]
  ```
- **Output**:
  ```
  [1, 0, 1]
  [0, 0, 0]
  [1, 0, 1]
  ```

**Python Code**:
```python
def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    first_row = any(matrix[0][j] == 0 for j in range(cols))
    first_col = any(matrix[i][0] == 0 for i in range(rows))

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row:
        for j in range(cols):
            matrix[0][j] = 0
    if first_col:
        for i in range(rows):
            matrix[i][0] = 0

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
set_zeroes(matrix)
print(matrix)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
```

### 7. **Matrix Rotation (90 Degrees)**
**Problem**: Rotate the given `n x n` matrix by `90 degrees` clockwise.

**Example**:
- Given Matrix:
  ```
  [1, 2, 3]
  [4, 5, 6]
  [7, 8, 9]
  ```
- **Output**:
  ```
  [7, 4, 1]
  [8, 5, 2]
  [9, 6, 3]
  ```

**Python Code**:
```python
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

