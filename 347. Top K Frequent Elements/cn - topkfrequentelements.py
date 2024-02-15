from typing import List

def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    # write your code here
    # Dictionary to store the count of each element
    count = {}
    # Array to organize elements based on their frequency
    frequency = [[] for _ in range(n + 1)]

    # Count the occurrences of each element in the array
    for num in arr:
        count[num] = 1 + count.get(num, 0)
    
    # Organize elements by frequency
    for num, freq_count in count.items():
        frequency[freq_count].append(num)
    
    # Result array to store the top K frequent elements
    result = []

    # Iterate through the frequency array in reverse order
    for i in range(len(frequency) - 1, 0, -1):
        # Append elements to the result array
        for num in frequency[i]:
            result.append(num)
            # Check if we have found the top K frequent elements
            if len(result) == k:
                return result
