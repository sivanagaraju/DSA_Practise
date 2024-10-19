**Graphs: Comprehensive Overview for Coding Interview Patterns**

### 1. Core Concepts and Coding Patterns
Graphs are data structures used to represent relationships between entities. A graph consists of nodes (vertices) connected by edges, which can either be directed or undirected. They can model real-world problems like social networks, maps, or even dependencies between tasks.

- **Vertices (Nodes)**: Represent entities or points in the graph.
- **Edges**: Represent relationships or connections between nodes.
- **Directed vs. Undirected**: Directed graphs have edges with a direction, meaning the relationship goes one way. Undirected graphs have bidirectional relationships.
- **Weighted Graphs**: Graphs where edges carry values, like distances or costs.

**Typical Use Cases**:
- **Pathfinding**: Finding routes in a city, e.g., GPS applications.
- **Network Flow**: Calculating the optimal data flow between two nodes.
- **Social Networks**: Modeling friendships or following relationships.
- **Dependencies**: Representing task precedence in project management.

### 2. Numeric Example
Consider a graph representing a social network where nodes represent people, and edges represent friendships.

```
A - B
|   |
C - D - E
```
- Here, `A`, `B`, `C`, `D`, and `E` are nodes representing people.
- Edges like `A - B` represent friendships. It is an undirected graph because the relationship is bidirectional.
- **Example Query**: Find all friends of person `A`.
  - **Answer**: `{B, C}`.

### 3. Problem Identification Checklist (in Tabular Format)
| Problem Type                         | Characteristics/Indicators                      | Example                                |
|--------------------------------------|------------------------------------------------|----------------------------------------|
| **Pathfinding Problems**             | Nodes, edges, shortest path                     | Find the shortest route from `A` to `E` |
| **Cycle Detection**                  | Need to detect cycles in dependencies           | Is there a cycle in a project's task dependencies? |
| **Connected Components**            | Find isolated groups in a graph                 | How many disconnected networks exist in a social graph? |

### 4. General Templates with Comments
#### Template 1: Depth-First Search (DFS)
```python
# Depth First Search (DFS) implementation using a stack
# This template is useful for traversal problems, cycle detection, and pathfinding.
def dfs(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # Process the node (e.g., print or collect it)
            for neighbor in graph[node]:
                stack.append(neighbor)
    
    return visited

# Use Case: Finding all nodes reachable from a starting point.
```
- **Use Case**: Applies to finding connected components and checking connectivity between nodes.

#### Template 2: Breadth-First Search (BFS)
```python
# Breadth First Search (BFS) implementation using a queue
# Useful for shortest path problems in unweighted graphs.
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            # Process the node (e.g., print or collect it)
            for neighbor in graph[node]:
                queue.append(neighbor)
    
    return visited

# Use Case: Finding shortest paths in an unweighted graph.
```

### 5. Complexity Analysis
- **DFS**:
  - Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
  - Space Complexity: O(V) due to recursion stack or explicit stack.
  - **Optimization Opportunity**: Reduce the size of visited nodes set by using bitwise operations for large node IDs.

- **BFS**:
  - Time Complexity: O(V + E).
  - Space Complexity: O(V) for the queue.
  - **Optimization Opportunity**: In sparse graphs, use adjacency lists to save memory.

### 6. Discussion on Templates and Patterns
The DFS and BFS templates can solve problems like pathfinding, detecting connected components, and cycle detection. Adjustments might be necessary for weighted graphs or large datasets, such as optimizing storage by using adjacency lists or matrices.

### 7. Multiple Approaches and Implementations
- **Iterative DFS** is usually preferred over **recursive DFS** for very deep graphs to avoid stack overflow issues.
- **Recursive BFS** is not recommended due to complexity in maintaining a queue without a loop.

**Comparative Analysis**:
- **DFS** is ideal for problems where deep exploration is needed (e.g., detecting cycles).
- **BFS** is suitable for shortest path calculations in unweighted graphs.

### 9. Practice Problems (in Tabular Format)
| S.No | Question                             | Example                                    | Difficulty Level | Approach       |
|------|--------------------------------------|--------------------------------------------|------------------|----------------|
| 1    | Find all connected components        | Graph with 6 nodes: A-B, C-D, E-F (3 isolated pairs). Output: `{{A, B}, {C, D}, {E, F}}`. Explanation: Nodes A and B are connected, C and D are connected, and E and F are connected, forming 3 isolated components. | Easy             | BFS or DFS (use a `visited` set to track which nodes have been visited to avoid redundant checks) |
| 2    | Shortest path in an unweighted graph | Graph: A-B, B-C, C-D, D-E. Start at A, find shortest path to E. Output: `[A, B, C, D, E]`. Explanation: The shortest path from A to E involves visiting nodes in sequence without skipping any intermediate nodes. | Medium           | BFS (use a queue to keep track of nodes to visit and a dictionary to store the parent of each node to reconstruct the path) |
| 3    | Detect cycle in directed graph       | Graph: A -> B -> C -> A. Output: `Cycle detected`. Explanation: The directed edge from C to A completes a cycle involving nodes A, B, and C. | Medium           | DFS (use an additional `recStack` set to track the nodes in the current recursive stack to detect cycles) |
| 4    | Topological Sort                     | Graph: A -> B, A -> C, B -> D. Output: `[A, B, C, D]`. Explanation: Node A has no dependencies, followed by nodes B and C, and finally D which depends on B. | Medium           | DFS (use a stack to store the order of nodes after visiting all their dependencies) |
| 5    | Check if a graph is bipartite        | Graph: A-B, B-C, C-D, D-A. Output: `True`. Explanation: It is possible to color the nodes in two colors such that no two adjacent nodes have the same color. | Medium           | BFS (use a queue and a color array to ensure nodes are colored alternatively) |
| 6    | Find bridges in a graph              | Graph: A-B, B-C, C-D, D-E, E-B. Output: `[{D, E}]`. Explanation: Removing edge D-E disconnects the graph, making it a bridge. | Hard             | DFS (use discovery and low time arrays to find bridges) |
| 7    | Find articulation points             | Graph: A-B, B-C, C-D, D-E, E-B. Output: `{B, D}`. Explanation: Removing node B or D will increase the number of disconnected components, making them articulation points. | Hard             | DFS (use discovery and low values to determine articulation points) |
| 8    | Clone an undirected graph            | Graph: A-B, B-C, C-A. Output: `Cloned graph with same structure`. Explanation: A new graph is created that replicates the connections between nodes in the original graph. | Medium           | DFS or BFS (use a hashmap to store copies of nodes) |
| 9    | Find all paths between two nodes     | Graph: A-B, B-C, A-C. Find all paths from A to C. Output: `[[A, B, C], [A, C]]`. Explanation: There are two paths from A to C: directly or via node B. | Medium           | DFS (use recursion to find all possible paths) |
| 10   | Detect cycle in an undirected graph  | Graph: A-B, B-C, C-A. Output: `Cycle detected`. Explanation: The edges A-B, B-C, and C-A form a loop, which is a cycle. | Medium           | DFS (use a parent array to keep track of visited nodes and their parents) |
| 11   | Minimum spanning tree (Prim's)       | Graph: Weighted graph with nodes A, B, C. Output: `Minimum spanning tree edges`. Explanation: The edges are selected such that the total weight is minimized, connecting all nodes. | Hard             | Prim's algorithm (use a priority queue to select the minimum weight edge) |
| 12   | Minimum spanning tree (Kruskal's)    | Graph: Weighted graph with nodes A, B, C. Output: `Minimum spanning tree edges`. Explanation: Edges are added in increasing order of weight, ensuring no cycles are formed. | Hard             | Kruskal's algorithm (use union-find to detect cycles) |
| 13   | Word ladder transformation           | Words: `hit` to `cog`. Output: `4 (hit -> hot -> dot -> dog -> cog)`. Explanation: Each word changes by one letter at a time, and each transformed word must be a valid word. | Medium           | BFS (use a queue to transform one letter at a time) |
| 14   | Course schedule                      | Courses: `A -> B, B -> C, C -> A`. Output: `Cycle detected`. Explanation: The course dependencies form a cycle, making it impossible to complete all courses. | Medium           | DFS (use a visited and recursion stack to detect cycle in dependencies) |
| 15   | Connected components in grid         | Grid with 1s and 0s. Output: `Number of islands`. Explanation: Each group of connected 1s represents an island. The output is the count of such islands. | Medium           | DFS (use nested loops to iterate through grid and DFS to explore islands) |
| 16   | Shortest path in a binary matrix     | Grid with 0s and 1s. Start at top-left, end at bottom-right. Output: `Shortest path length`. Explanation: The shortest sequence of moves from the start to the end, avoiding obstacles (1s). | Medium           | BFS (use a queue to explore all possible paths) |
| 17   | Network delay time                   | Graph with weighted edges. Output: `Time taken for signal to reach all nodes`. Explanation: Calculate the minimum time required for a signal to reach every node from a given start node. | Hard             | Dijkstra's algorithm (use a priority queue to find shortest paths) |
| 18   | Rotten oranges                       | Grid with fresh and rotten oranges. Output: `Time taken for all oranges to rot`. Explanation: Each rotten orange spreads rot to adjacent fresh oranges in each time unit. The output is the time required for all to rot, or -1 if impossible. | Medium           | BFS (use a queue to track rotten oranges and spread to adjacent fresh ones) |
| 19   | Find if path exists in graph         | Graph: A-B, B-C, C-D. Check if path exists from A to D. Output: `True`. Explanation: There is a sequence of edges from A to D, making a path possible. | Easy             | DFS or BFS (use a `visited` set to avoid redundant checks) |
| 20   | Reconstruct itinerary                | Flights: JFK -> SFO, JFK -> ATL, SFO -> ATL. Output: `[JFK, ATL, SFO, ATL]`. Explanation: All tickets must be used exactly once, forming a valid itinerary. | Hard             | DFS (use backtracking to find the valid itinerary using all tickets) |
| 21   | Number of Provinces                  | Graph represented as an adjacency matrix. Output: `Number of provinces`. Explanation: A province is a group of directly or indirectly connected cities. | Medium           | DFS (use a `visited` array to mark all cities in the same province) |
| 22   | Course schedule II                   | Courses with dependencies. Output: `Order to finish all courses`. Explanation: The order in which all courses can be completed, respecting prerequisites. | Medium           | Topological sort (use DFS to determine the order of courses) |
| 23   | Critical Connections in Network      | Network graph. Output: `List of critical connections`. Explanation: Critical connections are edges that, if removed, increase the number of disconnected components. | Hard             | Tarjan's algorithm (use discovery and low time to find critical edges) |
| 24   | Alien Dictionary                     | Sorted alien words. Output: `Order of characters`. Explanation: Determine the character order based on the given sorted words in an alien language. | Hard             | Topological sort (use BFS/DFS to determine character precedence) |
| 25   | Evaluate Division                    | Equations like A/B = 2, B/C = 3. Query A/C. Output: `6`. Explanation: Using the given equations, calculate the value of A/C by multiplying A/B and B/C. | Medium           | DFS (use a graph representation of equations to evaluate queries) |
| 26   | Cheapest Flights Within K Stops      | Flights with costs. Find cheapest from A to B with at most K stops. Output: `Cost`. Explanation: Calculate the minimum flight cost from A to B with no more than K stops in between. | Hard             | BFS (use a priority queue to track cost and stops) |
| 27   | Find Eventual Safe States            | Graph where nodes are either safe or lead to cycles. Output: `List of safe nodes`. Explanation: Nodes are safe if they do not lead to a cycle. The output is a list of such nodes. | Medium           | DFS (use colors to track visiting state of nodes) |
| 28   | Redundant Connection                 | Graph edges, find the edge causing a cycle. Output: `The redundant edge`. Explanation: Adding the edge results in a cycle, making it redundant. | Medium           | Union-Find (use union and find operations to detect cycle) |
| 29   | Longest Increasing Path in Matrix    | Matrix with integers. Output: `Length of the longest increasing path`. Explanation: Find the longest path in the matrix where each step moves to a strictly greater value. | Hard             | DFS with memoization (use recursion and memoization to avoid redundant calculations) |
| 30   | Graph Valid Tree                     | Graph with N nodes and N-1 edges. Output: `True/False if graph is a valid tree`. Explanation: A valid tree must have no cycles and all nodes must be connected. | Medium           | DFS or BFS (check for cycle and connectivity using visited set) |

Sure! I'll choose 7 random practice problems from the list and provide detailed explanations along with Python code.

### 1. **Detect Cycle in Directed Graph**
- **Problem**: Detect if there is a cycle in a directed graph.
- **Example**: 
  - Graph: A -> B -> C -> A.
  - **Explanation**: The directed edges create a cycle (A → B → C → A).
  - **Output**: `Cycle detected`.
  
**Python Code**:
```python
from collections import defaultdict

def is_cyclic(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        # Mark the node as visited and add to recursion stack
        if node not in visited:
            visited.add(node)
            rec_stack.add(node)

            # Recur for all neighbors
            for neighbor in graph[node]:
                if neighbor not in visited and dfs(neighbor):
                    return True
                elif neighbor in rec_stack:
                    return True
        
        rec_stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True

    return False

# Example graph represented as an adjacency list
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

print("Cycle detected" if is_cyclic(graph) else "No cycle detected")
```
- **Explanation**: 
  - We use DFS to visit each node.
  - The `rec_stack` set keeps track of nodes in the current recursive stack to detect cycles.
  - If we revisit a node that is in the `rec_stack`, it means we have a cycle.

### 2. **Find All Connected Components**
- **Problem**: Find all connected components in an undirected graph.
- **Example**: 
  - Graph with 6 nodes: A-B, C-D, E-F.
  - **Explanation**: The graph has three isolated components: {A, B}, {C, D}, and {E, F}.
  - **Output**: `{{A, B}, {C, D}, {E, F}}`.
  
**Python Code**:
```python
def find_connected_components(graph):
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components

# Example graph
graph = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['E']
}

connected_components = find_connected_components(graph)
print("Connected Components:", connected_components)
```
- **Explanation**:
  - We use DFS to explore each connected component.
  - Each time we start DFS on an unvisited node, we discover a new connected component.

### 3. **Shortest Path in an Unweighted Graph**
- **Problem**: Find the shortest path in an unweighted graph.
- **Example**: 
  - Graph: A-B, B-C, C-D, D-E.
  - **Explanation**: Start at `A` and find the shortest path to `E`. The shortest path is A → B → C → D → E.
  - **Output**: `[A, B, C, D, E]`.

**Python Code**:
```python
from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        elif node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            visited.add(node)

    return None

# Example graph
graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D']
}

shortest_path = bfs_shortest_path(graph, 'A', 'E')
print("Shortest Path from A to E:", shortest_path)
```
- **Explanation**: 
  - Use BFS to ensure that we find the shortest path in an unweighted graph.
  - We maintain a queue of paths and extend the path by one node at each step.

### 4. **Check if a Graph is Bipartite**
- **Problem**: Check if a given graph is bipartite.
- **Example**:
  - Graph: A-B, B-C, C-D, D-A.
  - **Explanation**: The graph can be colored using two colors such that no two adjacent nodes have the same color.
  - **Output**: `True`.

**Python Code**:
```python
def is_bipartite(graph):
    color = {}
    for node in graph:
        if node not in color:
            queue = deque([node])
            color[node] = 0
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        return False
    return True

# Example graph
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

print("Is the graph bipartite?", is_bipartite(graph))
```
- **Explanation**:
  - We use BFS to try and color the graph with two colors.
  - If we find a conflict, the graph is not bipartite.

### 5. **Find All Paths Between Two Nodes**
- **Problem**: Find all paths between two nodes in a graph.
- **Example**:
  - Graph: A-B, B-C, A-C.
  - **Explanation**: Find all paths from A to C. The possible paths are A → B → C and A → C.
  - **Output**: `[[A, B, C], [A, C]]`.

**Python Code**:
```python
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': []
}

all_paths = find_all_paths(graph, 'A', 'C')
print("All paths from A to C:", all_paths)
```
- **Explanation**:
  - Use DFS to find all paths from the start node to the end node.
  - Recursively extend each path until the end node is reached.

### 6. **Network Delay Time**
- **Problem**: Find the time it will take for all nodes to receive a signal.
- **Example**:
  - Graph with weighted edges: A -> B (1), B -> C (2), A -> C (4).
  - **Explanation**: Starting from A, the time taken for the signal to reach all nodes is `3` (A → B → C).
  - **Output**: `3`.

**Python Code**:
```python
import heapq

def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    pq = [(0, k)]
    dist = {}

    while pq:
        time, node = heapq.heappop(pq)
        if node not in dist:
            dist[node] = time
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (time + weight, neighbor))

    return max(dist.values()) if len(dist) == n else -1

# Example graph with weights
times = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('A', 'C', 4)
]

print("Network delay time:", network_delay_time(times, 3, 'A'))
```
- **Explanation**:
  - Use Dijkstra’s algorithm to calculate the shortest time taken for the signal to reach all nodes.

### 7. **Course Schedule**
- **Problem**: Determine if you can finish all courses given prerequisites.
- **Example**:
  - Courses: A -> B, B -> C, C -> A.
  - **Explanation**: The course dependencies form a cycle, making it impossible to complete all courses.
  - **Output**: `Cycle detected`.

**Python Code**:
```python
def can_finish_courses(num_courses, prerequisites):
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    visited = set()
    rec_stack = set()

    def dfs(node):
        if node in rec_stack:
            return False
        if node in visited:
            return True

        rec_stack.add(node)
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        rec_stack.remove(node)
        visited.add(node)
        return True

    for course in range(num_courses):
        if not dfs(course):
            return False

    return True

# Example courses with prerequisites
prerequisites = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'A')
]

print("Can finish courses?", can_finish_courses(3, prerequisites))
```
- **Explanation**:
  - Use DFS to detect cycles in the course dependency graph.
  - If a cycle is detected, it means it is impossible to complete all courses.

