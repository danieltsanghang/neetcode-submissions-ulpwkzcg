class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        feq1 = defaultdict(int)
        for c in s1:
            feq1[c] += 1
        l = 0
        feq2 = defaultdict(int)

        for i, c in enumerate(s2):
            if i - l < len(s1):
                feq2[c] += 1
            else:
                if feq2[s2[l]] > 1:
                    feq2[s2[l]] -= 1
                else:
                    feq2.pop(s2[l])
                l += 1
                feq2[c] += 1
            if feq2 == feq1:
                return True
        return False