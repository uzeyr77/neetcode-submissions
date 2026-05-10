class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        e = len(nums) - 1
        while l <= e:
            mid = (l + e)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid  - 1
            elif nums[mid] < target:
                l = mid + 1
        return -1 