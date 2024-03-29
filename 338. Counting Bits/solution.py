class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n + 1):
            result.append(self.hammingWeight(i))
        return result
    
    def hammingWeight(self, n):
        result = 0
        while n:
            n &= (n-1)
            result += 1
        return result

# Optimal approach : Time Complexity of O(n) space
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        counter = [0] * (n + 1)
        offset = 1

        for number in range(1, n+1):
            if number == offset * 2:
                offset = number
            counter[number] = 1 + counter[number - offset]
        return counter
