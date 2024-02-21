from typing import List

class Solution:
    def carFleet(self, target: int, positions: List[int], speed: List[int]) -> int:
        pairs = [[pos, sp] for pos, sp in zip(positions, speed)]

        stack = []
        for position, sp in sorted(pairs)[::-1]:
            stack.append((target - position) / sp)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)