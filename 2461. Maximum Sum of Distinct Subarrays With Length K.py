class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        window_sum = 0
        max_sum = 0
        count = {}
        
        # Build first window
        for i in range(k):
            count[nums[i]] = count.get(nums[i], 0) + 1
            window_sum += nums[i]
        
        # Check first window
        if len(count) == k:
            max_sum = window_sum

        # Slide the window
        for right in range(k, len(nums)):
            # Add new element
            window_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1
            
            # Remove left element
            left = nums[right - k]
            window_sum -= left
            count[left] -= 1

            # Remove from map if frequency becomes 0
            if count[left] == 0:
                del count[left]
        
            # Update answer ONLY if all elements are distinct
            if len(count) == k:
                max_sum = max(max_sum, window_sum)
        
        return max_sum

