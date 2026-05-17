class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        min_k = 1
        max_k = max(piles)

        ans = max_k

        while min_k <= max_k:
            center_k = int((max_k + min_k) / 2)
            count_h = 0
            for pile in piles:
                count_h += (pile // center_k)  if pile % center_k == 0 else (pile // center_k) + 1
                if count_h > h :
                    min_k = center_k + 1
                    break
            if count_h <= h:
                ans = center_k
                max_k = center_k - 1

        return ans