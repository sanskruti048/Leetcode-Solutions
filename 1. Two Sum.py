class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
           
            if complement in map:
                return (map[complement], i)
            
            map[nums[i]] = i