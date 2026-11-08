class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)

        left = 1
        right = max(piles)
        best_k = right
        time = 0
        while left <= right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time = time + math.ceil(float(pile)/mid)
            if time > h:
                left = mid + 1
            else:
                best_k = min(mid, best_k)
                right = mid - 1
        return best_k
