class Solution:
  def dailyTempratures(self, tempratures: List[int]) -> List[int]:
    stack = [] # pair of values with temp and index temp value
    result = [0] * len(temperatures)

    for index, value in enumerate(temperatures):
      while stack and value > stack[-1][0]:
        stackT, stacki = stack.pop()
        result[stacki] = (index - stacki)
      stack.append([value,index])

    for index, temp in enumerate(temperatures):
      while stack and temp > temperatures[stack[-1]]:
        stack_index = stack.pop()
        result[index] = index - stack_index
      stack.append(index)
    return result
      
