class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        
        div = 1
        while x >= 10 * div:
            div *= 10
        
        while x:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10
            div /= 100
        
        return True


        # Brute Force Approach (converting to string)
        # num = str(x)
        # rev = num[::-1]
        # if num == rev:
        #     return True
        # return False
