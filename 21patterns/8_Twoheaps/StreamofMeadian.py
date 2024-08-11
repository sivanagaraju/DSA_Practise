import heapq

def find_medium(stream):
    max_heap = []  # will have the lower numbers 
    min_heap = [] # will have the higher numbers
    
    medians = []
    
    for num in  stream:
        if not max_heap or num < max_heap[0]:
            heapq.heappush(num, max_heap)
        else:
            heapq.heappush(num, min_heap)
            
        
        if len(max_heap) > len(min_heap) + 1 :
            heapq.heappush(min_heap, heapq.heappop(max_heap))
            
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, heapq.heappop(min_heap))
            
        if len(max_heap) == len(min_heap):
            median = (max_heap[0] + min_heap[0]) / 2
        else:
            median = max_heap[0]
            
        medians.append(median)
        
    return medians


nums = [28, 17, 34, 5, 9, 3, 12]
print(find_medium(nums))
            