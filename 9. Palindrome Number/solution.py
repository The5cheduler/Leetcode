class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Algorithm

        # Create result variable to store the value for reveresed number
        result = 0
        original_x = x
        # Check if number id negative If yes return False
        if x < 0:
            return False

        # Check if number is valid number:
        while x:
    
        # Perform reminder by 10 to fetch the last digit of the number
            reminder = x % 10
        # Update result variable by multiplying with 10 and adding reminder
            result = (result * 10) + reminder
        # Update the value of given number by performing floor division
            x //= 10
        
        # Check if result variable is same as result and return the result
        return original_x == result

