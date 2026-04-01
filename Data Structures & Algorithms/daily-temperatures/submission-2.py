class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        hottest = []
        b = False
        for _, t in enumerate(temperatures):
            i = len(temperatures) - 1 - _
            print(hottest)
            for h in hottest:
                if h[0] > temperatures[i]:
                    b = True
                    res = [h[1] - i] + res
                    print("1", res)
                    break
            if not b:
                res = [0] + res
                print("2", res)
            else:
                b = False
            hottest = [(temperatures[i], i)] + hottest
        return res