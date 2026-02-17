class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count = 0
        max_count = 0
        
        # Count vowels in the first window of size k
        for ch in s[0:k]:
            if ch in "aeiou":
                vowel_count += 1

        max_count = vowel_count

         # Slide the window across the string
        for right in range(k, len(s)):
            
            # Add the new entering character
            if s[right] in "aeiou":
                vowel_count += 1
            
            # Remove the old leaving character
            if s[right-k] in "aeiou":
                vowel_count -= 1

            # Update maximum vowel count
            max_count = max(max_count, vowel_count)

        return max_count
