class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        small_side = 0
        right = len(heights) - 1
        if len(heights) == 0:
            return 0
        while (left < right):
            small_side = min(heights[left], heights[right])
            max_area = max(max_area, (small_side * (right- left)))
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] < heights[right]:
                right -= 1
            else:
                right -= 1


        return max_area
            
