import heapq

def solve_top_k_problem(nums, k):
    # Determine if we're finding top K largest or smallest
    # For K largest elements, use a min heap
    # For K smallest elements, use a max heap (we'll use negative values to simulate this)
    is_finding_largest = True  # Change this based on the problem

    # Initialize the heap
    heap = []
    
    for num in nums:
        # Modify the value based on whether we're finding largest or smallest
        value = num if is_finding_largest else -num
        
        if len(heap) < k:
            # If the heap is not full, add the element
            heapq.heappush(heap, value)
        elif value > heap[0]:
            # If the heap is full and the current element is greater than the smallest in the heap,
            # remove the smallest and add the current element
            heapq.heapreplace(heap, value)
    
    # Prepare the result
    # Remember to revert the negation if we were finding smallest elements
    result = [-x for x in heap] if not is_finding_largest else heap
    
    return result

# Example usage
nums = [3, 1, 5, 12, 2, 11]
k = 3
top_k = solve_top_k_problem(nums, k)
print(f"The top {k} elements are: {top_k}")

# Variations and modifications:
# 1. For finding most frequent elements:
#    - Use a dictionary to count frequencies
#    - Use (frequency, element) pairs in the heap
#    - Modify comparison logic accordingly

# 2. For problems like "K closest points to origin":
#    - Modify the `value` calculation to use distance formula
#    - Use (distance, point) pairs in the heap

# 3. For stream processing:
#    - Modify the main loop to process elements one by one as they come in
#    - Maintain the heap size at K all the time

# 4. For problems requiring custom comparison:
#    - Define a custom class with `__lt__` method
#    - Use instances of this class in the heap

# Note: This template uses a min-heap by default.
# For max-heap behavior, negate the values and comparison logic.