class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * (len(temperatures))
        s = []
        for _ in range(len(temperatures)):
            cur = temperatures[_]
            while s and temperatures[s[-1]] < cur:
                # using a list like s = s[1:] will time out
                i = s.pop()
                res[i] = _ - i
            s.append(_)
        return res