class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # check if the list is empty
        if len(nums) == 0:
            return [] * len(nums)
        
        # check if the list contains only zeros
        check = False
        for i in nums:
            if i != 0:
                check = True
        # if the list contains only zeros return a list of size len(nums) of all zeros
        if not check:
            return [0] * len(nums)
        

        total_product = 1
        resu = [0] * len(nums)
        
        # get the total product of all elements in the list
        for i in nums:
            if i != 0:
                total_product = total_product * i

        num_zeros = 0
        for i in nums:
            if i  == 0:
                num_zeros += 1
        
        if num_zeros > 1:
            return [0] * len(nums)

        for i in range(0, len(nums)):
            if 0 in nums and nums[i] != 0:
                resu[i] = 0
            elif 0 in nums and nums[i] == 0:
                resu[i] = total_product
            else:
                resu[i] = total_product // nums[i]
        
    # -6
        return resu
        