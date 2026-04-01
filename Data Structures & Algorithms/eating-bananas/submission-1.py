class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # biggest pile
        upper_bound = list(sorted(piles))[-1]
        # worst case is one at a time
        lower_bound = 1

        while lower_bound < upper_bound:
            speed = (lower_bound + upper_bound) // 2
            cur = sum([math.ceil(b/speed) for b in piles])
            if cur <= h:
                upper_bound = speed
            else:
                lower_bound = speed + 1
        return lower_bound