import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []

        for num in self.nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, num)
            else:
                heapq.heappushpop(self.heap, num)        

    def add(self, val: int) -> int:
        k = self.k
        heap = self.heap

        if len(heap) < k:
            heapq.heappush(heap, val)
        else:
            heapq.heappushpop(heap, val)
        
        return heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)