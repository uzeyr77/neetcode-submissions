class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if it is the start of a sequence, its the start if it has no left neighbors
            if (n-1) not in numSet:
                length = 0
                # loop as long as conseq numbers in the set
                # n + length is initially n + 0, then n + 1, then n + 2 and so on, so while those # are in the set increment length
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest