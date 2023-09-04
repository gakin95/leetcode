#Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        last_seen = {}
        longest = [0,1]
        start_ids = 0
        for i, char in enumerate(s):
            if char in last_seen:
                start_ids = max(start_ids, last_seen[char] + 1)
            if longest[1] - longest[0] < i + 1 - start_ids:
                longest = [start_ids, i+1]
            last_seen[char] = i
        return longest[1] - longest[0]