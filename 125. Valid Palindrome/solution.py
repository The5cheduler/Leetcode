class Solution:
  def isValidPalindrome(self, string: str) -> bool:
    left = 0
    right = len(string) - 1

    while left < right:
      if not string[left].isalnum():
        left += 1
      elif not string[right].isalnum():
        right -= 1
      elif string[left].lower() == string.[right].lower():
        left += 1
        right -= 1
      else:
        return False
    return True
