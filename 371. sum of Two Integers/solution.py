class Solution:
  def getSum(self, a: int, b: int) -> int:
    """Calculates the sum of two integers using bitwise XOR and carry operations.

    Args:
        a: The first integer (required).
        b: The second integer (required).

    Returns:
        The sum of a and b.
    """

    while b != 0:
      # Carry is the AND of a and b
      carry = a & b
      # XOR of a and b provides the sum without carry
      a = a ^ b
      # Shift carry one position left for the next iteration
      b = carry << 1

    return a
