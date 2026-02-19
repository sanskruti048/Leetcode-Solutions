class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            # add right character
            count[s[right]] = count.get(s[right], 0) + 1
            
            # update max frequency in current window
            max_freq = max(max_freq, count[s[right]])
            
            # if window invalid → shrink
            while (right-left+1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # update answer
            max_len = max(max_len, right-left+1)

        return max_len
