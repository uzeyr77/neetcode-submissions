class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        if len(s) < 2:
            return True
        while l <= r:
            if (s[l].isalnum() and s[r].isalnum()):
                if s[l].lower() != s[r].lower():
                    return False
            else:
                if not s[l].isalnum():
                    l += 1
                else:
                    r -= 1
                continue
            l+=1
            r-=1
        return True