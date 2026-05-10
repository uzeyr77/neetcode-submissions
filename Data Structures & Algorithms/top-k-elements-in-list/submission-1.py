class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resu = [] 
        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        arr = []
        for val, count in map.items():
            arr.append([count, val])

        # sort in ascending order based on the count e.i least freq to most freq
        arr.sort()
        while len(resu) < k: 
            # arr.pop() returns the value popped from the back, so pops most freq to less freq and [1] 
            # gets the value and not the count
            resu.append(arr.pop()[1])
                

     
        return resu
        