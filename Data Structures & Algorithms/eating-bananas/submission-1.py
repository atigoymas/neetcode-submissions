class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            k = (l+r) // 2
            time = 0

            for banana in piles:
                time += math.ceil(float(banana)/k)

            if time <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1
        return ans


        