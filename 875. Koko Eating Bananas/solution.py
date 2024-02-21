class Solution:
  def minEatingSpeed(self, piles: List[int], h:int) -> int:
    # define two pointer to keep track of eating speed.
    left_pointer, right_pointer = 1, max(piles)
    result = right_pointer

    while left_pointer <=  right_pointer:
      # eating speed would be left pointer + right pointer and division by 2
      eating_speed = (left_pointer + right_pointer) // 2
      hours = 0 # number of hours taken to eat given pile at current eating speed

      for bananas in piles:
        # calculate number of hours taken to eat each pile of bananas and add it to total hours
        hours += math.ceil(bananas / eating_speed)

      if hours <= h:
        # check if current calculated hours are less than given hours
        result = min(result, eating_speed) # update the result with minimum of current result or current eating speed
        right_pointer = eating_speed + 1 # update the right pointer to check if slower eating speed it possible
      else:
        left_pointer = eating_speed - 1 # if hours is greater than given hours than we will update left pointer to current eating speed

    # return result once done condition no longer satisfies.
    return result
      
