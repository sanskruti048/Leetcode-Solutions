class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()     # Sort the array
        ans = []
        
        # Fix one number at a time (index i)
        for i in range(len(nums) - 2):

            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Early stopping: Sum > 0 
            if nums[i] > 0:
                break

            left, right = i+1, len(nums)-1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                # Found a valid triplet
                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values for left pointer
                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    # Skip duplicate values for right pointer
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                # Sum is too small → move left to increase sum
                elif total < 0:
                    left += 1

                # Sum is too large → move right to decrease sum
                else:
                    right -= 1

        return ans           
        