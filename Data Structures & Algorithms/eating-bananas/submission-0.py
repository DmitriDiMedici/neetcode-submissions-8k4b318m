import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        k = 0

        while left <= right:
            mid = (left + right) // 2
            hours = self.calc_hours(mid, piles)
            if hours > h:
                left = mid + 1
            else:
                k = mid
                right = mid - 1

        return k

    def calc_hours(self, speed, piles):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / speed)
        return total_hours