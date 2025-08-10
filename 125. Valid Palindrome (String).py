class Solution:
    def isPalindrome(self, s):
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
        