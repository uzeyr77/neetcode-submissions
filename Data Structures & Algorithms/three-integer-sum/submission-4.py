class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4 -1 -1 0 1 2
        # - nums[i] = nums[j] + nums[k] 

        # have two pointers start at left and right, first sort the list
        # have an outer for loop, the target is target = 0 - nums[i]
        # then we have a second loop inside the first, the targets are then
        # the two digits that make target = 0, meaning nums[left] + nums[right] is the 
        # sign inverse of target (e.i 4 and -4)
        # since the list is sorted we have 3 cases
        # nums[left] + nums[right] + target > 0, then shift right pointer left (sorted ascend)
        # nums[right] + nums[left] < + target 0, then shift left pointer right
        # otherwise if nums[right] + nums[left] +  target = 0 then found the indices
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res