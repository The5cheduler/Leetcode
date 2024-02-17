from typing import List

class solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices or len(prices) < 2: return 0

        leftPointer, rightPointer = 0,1
        maxProfit = 0

        while rightPointer < len(prices):
            if prices[leftPointer] < prices[rightPointer]:
                profit = prices[rightPointer] - prices[leftPointer]
                maxProfit = max(profit, maxProfit)
            else:
                leftPointer = rightPointer
            rightPointer += 1

        return maxProfit

if __name__ == "__main__":
    # Create an instance of the solution class
    s = solution()

    # Test the maxProfit function
    prices = [7, 1, 5, 3, 6, 4]
    result = s.maxProfit(prices)
    print("Max Profit:", result)
