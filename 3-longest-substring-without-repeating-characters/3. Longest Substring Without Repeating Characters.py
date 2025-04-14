class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        seen = {}

        for end in range(len(s)):
            char = s[end]
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            seen[char] = end
            max_len = max(max_len, end - start + 1)

        return max_len