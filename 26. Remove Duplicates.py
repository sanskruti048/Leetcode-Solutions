class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:    # check if num is different than the previous num
                nums[k] = nums[i]       # store the unique num at the k-th position
                k += 1                  # increment
        return k 