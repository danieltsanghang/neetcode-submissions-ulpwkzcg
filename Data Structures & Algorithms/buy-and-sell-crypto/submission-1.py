class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        res = 0
        for i, n in enumerate(prices):
            cur = prices[i] - start
            if cur > res:
                res = max(res, cur)
            start = min(start, n)
        return res