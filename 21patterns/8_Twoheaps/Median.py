import heapq

def two_heap_structure(nums):
    min_heap = []
    max_heap = []
    
    for num in nums:
        if not max_heap or num < max_heap[0]:
            heapq.heappush(max_heap, num)
        else:
            heapq.heappush(min_heap, num)
            
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, heapq.heappop(min_heap))
            
    
    result = []
    while max_heap or min_heap:
        if max_heap:
            result.append(heapq.heappop(max_heap))  # using heapq gettting the minimum element.
        if min_heap:
            result.append(heapq.heappop(min_heap))
    return result

nums = [28, 17, 34, 5, 9, 3, 12]
print(two_heap_structure(nums))