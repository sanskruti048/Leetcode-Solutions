class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        target_count = {}
        for ch in t:
            target_count[ch] = target_count.get(ch, 0) + 1
        required = len(target_count)
        
        window_count = {}
        formed = 0

        left = 0
        min_len = float("inf")
        min_window = ""

        for right in range(len(s)):
            ch = s[right]
            window_count[ch] = window_count.get(ch, 0) + 1

            # Increase formed only when required frequency is met
            if ch in target_count and window_count[ch] == target_count[ch]:
                formed += 1

            # Try to shrink while window is valid
            while formed == required:
                window_size = right - left + 1

                if window_size < min_len:
                    min_len = window_size
                    min_window = s[left : right+1]

                left_ch = s[left]
                window_count[left_ch] -= 1

                # If a required char drops below needed frequency → window invalid
                if left_ch in target_count and window_count[left_ch] < target_count[left_ch]:
                    formed -= 1

                left += 1

        return min_window