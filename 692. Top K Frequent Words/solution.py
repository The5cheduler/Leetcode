import heapq
from typing import List
from collections import *
class Solution:
    def topKfrequent(self, words: List[str], k:int) -> List[str]:
        # Step 1: Count the frequency of each word
        frequency = Counter(words)
        
        # Step 2: Create a min heap where each element is a tuple containing the negative frequency and the word
        # We use negative frequency to make sure that the min heap always pops the word with the highest frequency first
        min_heap = [(-freq, word) for word, freq in frequency.items()]
        heapq.heapify(min_heap)

        result = []
        # Step 3: Pop k elements from the min heap and append the corresponding words to the result list
        for _ in range(k):
            result.append(heapq.heappop(min_heap)[1])
        
        return result