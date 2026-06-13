class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 1
        count = 0
        l = 0
        map = {}

        for r in range(len(s)):
            if s[r] in map:
                map[s[r]] = map[s[r]] + 1
            else:
                map[s[r]] = 1
            
            while ((r - l + 1) - max(map.values())) > k:
                c = map[s[l]]
                map[s[l]] = c - 1
                l += 1
            count = max(count, (r - l + 1))
        return count
            
                
            