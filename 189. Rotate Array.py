class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        
        # Reverse Function
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n      # incase, k > n

        reverse(nums, 0, n-1)        # reverse the whole array
        reverse(nums, 0, k-1)        # reverse the first k elements
        reverse(nums, k, n-1)        # reverse the remaining n-k elements

        return nums

        