class Solution:
    def reverse(self, x: int) -> int:
        # Create a result variable
        reverse_int = 0
        
        # Create Two boundaries
        left, right = pow(-2, 31), pow(2, 31) - 1

        # Store original value of x
        initial_x = x

        # Check if x is negative if it is convert it to positive number
        if x < 0:
            x = abs(x)

        # Check if current x value is greater than left boundry and also less than right boundry
        while x >=left and x <= right:
            while x:
                reminder = x % 10 # Grab the last digit of given number
                reverse_int = (reverse_int * 10) + reminder # Add it to currently reveresed int by multiplying to 10 plus the reminder
                x = x // 10 # Update the value of x

            if initial_x < 0:
                return 0 if -abs(reverse_int) <= left else -abs(reverse_int)
            return 0 if abs(reverse_int) >= right else abs(reverse_int)
        else:
            return 0


        