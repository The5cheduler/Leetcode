from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create an empty min heap
        min_heap = []

        # Iterate through each point in the input list
        for x, y in points:
            # Calculate the distance from the origin using Euclidean distance formula
            distance = pow(x,2) + pow(y,2)
            
            # Append the distance and the point to the min heap as a tuple
            min_heap.append((distance, [x, y]))
        
        # Convert the list into a min heap
        heapq.heapify(min_heap)

        # Pop the k smallest elements from the min heap and return them as a list
        return [heapq.heappop(min_heap)[1] for _ in range(k)]