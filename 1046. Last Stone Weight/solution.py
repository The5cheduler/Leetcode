from heapq import *
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Convert the stones to negative values
        for idx, stone in enumerate(stones):
            stones[idx] = -stone

        # Convert the list into a min-heap
        heapify(stones)
        
        # Continue the process until there is only one stone left
        while stones:
            # Take out the largest stone
            stone1 = -heappop(stones)
            
            # If there are no more stones, return the last stone's weight
            if not stones:
                return stone1
            
            # Take out the second largest stone
            stone2 = -heappop(stones)
            
            # If the two stones are not of equal weight, calculate the difference and add it back to the heap
            if stone1 > stone2:
                heappush(stones, stone2 - stone1)
        
        # If there are no stones left, return 0
        return 0