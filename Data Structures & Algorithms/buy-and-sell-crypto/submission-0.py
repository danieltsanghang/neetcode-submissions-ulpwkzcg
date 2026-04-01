class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_start = prices[0]
        max_end = 0
        res = 0
        for i, n in enumerate(prices):
            max_start = min(max_start, n)
            min_ = max(prices[i:])
            if min_ - max_start < 0:
                continue
            else:
                res = max(res, min_ - max_start)
        return res