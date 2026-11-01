class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        merged_list = []
        for row in matrix:
            merged_list = merged_list + row
        low = 0
        high = len(merged_list) - 1
        
        while low <= high:
            mid = (low + high)//2
            if merged_list[mid] == target:
                return True
            elif merged_list[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
        