class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        # [3,4,5,6,1,2] - [6,1,2] - [6,1]
        left = 0
        right = len(nums) - 1
        mid = 0
        res = nums[0]
        while (left <= right):
            if nums[left] <= nums[right]:
                res = min(nums[left], res)
                break
            mid = (left + right) // 2
            res = min(nums[mid], res)
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
            
            
        return res

