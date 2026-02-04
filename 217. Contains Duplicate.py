class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ans = set()
        for i in range(len(nums)):
            if nums[i] in ans:
                return True
            ans.add(nums[i])
        return False