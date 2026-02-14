class Solution:
    def isPalindrome(self, s):
        # Uses no extra space for storing s: Optimal Soln:  TC=O(n), SC=O(1)
        left, right = 0, len(s)-1
        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True

        
        # Uses extra space to store the string: TC=O(n), SC=O(n)
        cleaned_str = ''.join([char for char in s.lower() if char.isalnum()])
        cs = cleaned_str
        left = 0
        right = len(cs)-1
        while left < right:
            if (cs[left] != cs[right]):
                return False
            left += 1
            right -= 1
        return True
        