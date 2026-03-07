class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n-1))

        # for x in range(0,100):
        #     if n > 0 and n == 2 ** x:
        #         return True
        
        # return False
