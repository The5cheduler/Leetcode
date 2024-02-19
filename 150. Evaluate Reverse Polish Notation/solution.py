from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # approach 1

        operation = {
            "+" : add,
            "-" : sub,
            "*" : mul,
            "/" : truediv,
        }
        stack = []

        for token in tokens:
            if token in operation:
                stack[-1] = int(operation[token](stack[-2], stack.pop()))
            else:
                stack.append(int(token))

        return stack.pop()

        # Approach 2
        for token in tokens:
            if token == "+":
                stack[-1] = int(add(stack[-2], stack.pop()))
            elif token == "-":
                stack[-1] = int(sub(stack[-2], stack.pop()))
            elif token == "*":
                stack[-1] = int(mul(stack[-2], stack.pop()))
            elif token == "/":
                stack[-1] = int(truediv(stack[-2], stack.pop()))
            else:
                stack.append(int(token))

        return stack.pop()



if __name__ == "__main__":
    # Create an instance of the solution class
    s = Solution()
    result = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print("Max Profit:", result)