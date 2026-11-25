class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # compare nums[mid] to the left most item 
        # in the left half if mid is greater than nums[0], in the right half if not 

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[0]: # in the left side
                if nums[mid] > target:
                    if nums[l] < target: # search left side
                        return guess_number(0, mid-1, target, nums)
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
            else: # in the right side
                if nums[mid] > target:
                    if nums[r] > target:
                       r = mid -1
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    if nums[r] > target:
                         resu = guess_number(mid+1, r, target, nums)
                         return resu
                    else:
                        r = mid - 1
        return -1

def guess_number(low: int, high: int, secret: int, nums: list[int]) -> int:
    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[mid] == secret:
            return mid
        elif mid < secret:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1





