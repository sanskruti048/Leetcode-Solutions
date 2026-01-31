class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        xor_val = 0
        
        for i in range(n):
            xor_val ^= i ^ nums[i]
        
        return xor_val ^ n
        