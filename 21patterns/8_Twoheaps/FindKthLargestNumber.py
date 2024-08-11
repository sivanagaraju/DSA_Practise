import heapq

def findklargest(nums, k):
    max_heap = []
    min_heap = []
    
    for num in nums:
        if len(max_heap) < k:
            heapq.heappush(max_heap, num)
        elif(num > max_heap[0]):
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, num)
    
    return max_heap[0]

"""
def findKthLargest(nums: List[int], k: int) -> int:
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    return min_heap[0]

"""

nums = [3,2,1,5,6,4]
k = 2
print(findklargest(nums, k))

        