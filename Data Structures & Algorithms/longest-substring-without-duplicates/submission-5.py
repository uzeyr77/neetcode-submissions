class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) <= 1:
            return 1
        length = 1
        max_length = 0
        map = {}
        left = 0
        right = 1
        map[s[left]] = 1
        while right < len(s):
            if s[right] not in map:
                map[s[right]] = 1
                length += 1
            else:
                left += 1
                right = left
                max_length = max(max_length, length)
                map.clear()
                map[s[right]] = 1
                length = 1
            right += 1
        
        return max(max_length, length)
            


        