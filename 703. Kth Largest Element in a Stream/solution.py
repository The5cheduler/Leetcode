import heapq
from typing import List
class KthLargest:
    # Initialize the class with the given value of k and a list of numbers
    def __init__(self, k: int, nums: List[int]):
        self.k, self.min_heap = k, nums
        # Convert the list into a min heap
        heapq.heapify(self.min_heap)
        # Remove elements from the min heap until its size is equal to k
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    # Add a new value to the min heap
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        # If the size of the min heap exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        # Return the smallest element in the min heap
        return self.min_heap[0]
