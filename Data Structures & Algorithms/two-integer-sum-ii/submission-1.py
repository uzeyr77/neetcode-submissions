class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        difference = 0

        for i in range(len(numbers)):
            difference = target - numbers[i]
            j = i
            for j in range(len(numbers)):
                if numbers[j] != numbers[i] and numbers[j] == difference:
                    return [i+1,j+1] 