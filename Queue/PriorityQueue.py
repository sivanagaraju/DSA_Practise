class PriorityQueue:
    def __init__(self):
        # Initiliase an empty list to store the heap elements
        self.heap = []
        
    def push(self, value, priority):
        # append the new element to the end of the loop
        self.heap.append((value, priority))
        
        # call _heapify_up  to maintain the heap property
        # len(self.heap) - 1  gives the newly added index
        self._heapify_up(len(self.heap) - 1)
        
    def pop(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # store the root element( highest priority)
        root = self.heap[0]
        # replace the root with last element in the heap.
        self.heap[0] = self.heap.pop()
        
        # call _heapify_down to maintain the heap property        
        self._heapify_down(0)
        
        return root              
    
    # bubble up
    def _heapify_up(self, index):
        """
        when we add a new element we have to maintain the heap property. 
        This esnures that the highest priority element is always at the root.        
        """
        # calculate the parent index
        parent_index = (index -1) // 2
        # if the index is 0 or negative, stop(already at the root)
        if index <= 0:
            return 
        # if the parent priority is less than the current elements priority, swap them 
        elif self.heap[parent_index][1] < self.heap[index][1]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.hep[parent_index]
            # do recusively call the _heapify up to maintain the heap property  
            self._heapify_up(parent_index)
    
    #bubble down
    def _heapify_down(self, index):
        """
        swap the current node with one of its children to ensure the heap property is maintained the affetes subtree.
        By recusively calling heapify own on the swapped child we ensure the heap property is maintained. 
        """
        # calculate the left and right child indices
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        """
        Root: index 0 (in this case, (8, 5))
        Left child: 2 * index + 1 (in this case, 2 * 0 + 1 = 1, which corresponds to (7, 4))
        Right child: 2 * index + 2 (in this case, 2 * 0 + 2 = 2, which corresponds to (6, 3))
        """
        largest = index
        
        # if the left child exists and has a higher priority, update largest
        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index][1] > self.heap[largest][1]
        ):
            largest = left_child_index
        
        # if the right child exists and has a higher priority, update largest
        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index][1] > self.heap[largest][1]
        ):
            largest = right_child_index
        
        # if the largest index is not the current index, swap and recuersively call heapify down
        if largest !=  index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest) 
            

pq = PriorityQueue()
pq.push("apple", 3)
pq.push("banana", 1)
pq.push("orange", 2)

print(pq.pop())  # Output: ("banana", 1)
print(pq.pop())  # Output: ("orange", 2)
print(pq.pop())  # Output: ("apple", 3)
    