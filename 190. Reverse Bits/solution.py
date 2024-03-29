class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0 # This represent 00000000000000000000000000000000
        for i in range(32):
            bit = (n >> i) & 1 # To reverse the bit move number to ith bit and perform and logic operation as it will not change other bits 
            result = result | (bit << (31 - i)) # Add bit to result by or logic operaion and shifring the bit by 31 - ith position beacuse if we have zero in current result than replace with new bit and or logic does that 
        return result
# # 11000000000000000000000000000000 +
# # 10000000000000000000000000000000
# # 01000000000000000000000000000000
# now thake that bit 0 to  reult and 
