class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_length = 0
        sub = set()
        left = 0
        for right in range(len(s)):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1
            sub.add(s[right])
            max_length = max(max_length, len(sub))
        
        return max_length
        