import collections
from typing import List

class Solution(object):
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the occurrences of each task
        counter = collections.Counter(tasks)
        
        # Find the maximum count of a task
        max_count = max(counter.values())
        
        # Count the number of tasks with the maximum count
        max_count_tasks = list(counter.values()).count(max_count)
        
        # Calculate the minimum time required to complete all tasks
        min_time = (max_count - 1) * (n + 1) + max_count_tasks
        
        # Return the maximum of the minimum time and the total number of tasks
        return max(min_time, len(tasks))