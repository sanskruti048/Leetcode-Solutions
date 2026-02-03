class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i = j = 0
        
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                ans += word1[i]
            if j < len(word2):
                ans += word2[j]
            i += 1
            j += 1
                
        return ans