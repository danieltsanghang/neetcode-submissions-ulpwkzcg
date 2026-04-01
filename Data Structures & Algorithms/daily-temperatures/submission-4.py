class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        hottest = []
        b = False
        for _ in range(len(temperatures)):
            i = len(temperatures) - 1 - _
            for h in hottest:
                if h[0] > temperatures[i]:
                    b = True
                    res = [h[1] - i] + res
                    break
            if not b:
                res = [0] + res
            else:
                b = False
            hottest = [(temperatures[i], i)] + hottest
        return res