class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        resu = [0] * len(temperatures)
        
        for index, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                stk_temp, stk_index = stack.pop()
                resu[stk_index] = index - stk_index
            
            stack.append((temp, index))
        
        return resu

        
                