class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      freq_t = {}
      freq_s = {}
      for i in s:
        if i in freq_s:
            c = freq_s[i] 
            c += 1
            freq_s[i] = c
        else:
            freq_s[i] = 1    
      for i in t:
        if i in freq_t:
            c = freq_t[i] 
            c += 1
            freq_t[i] = c
        else:
            freq_t[i] = 1
      return freq_t == freq_s;