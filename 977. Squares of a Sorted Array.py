class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Optimal SolutionV: TC = O(n), SC = O(n) 
        left, right = 0, len(nums)-1
        sq = []
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                sq.append(nums[right] ** 2) 
                right -= 1
            else:
                sq.append(nums[left] ** 2) 
                left += 1
        return sq[::-1]
    

        # Brute Force Approach: TC = O(n log n), SC = O(n) 
        # sq = []
        # for i in range(len(nums)):
        #     sq.append(nums[i] ** 2)
        # return sorted(sq)

        