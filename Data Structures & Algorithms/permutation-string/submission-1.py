class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        feq1 = defaultdict(int)
        for c in s1:
            feq1[c] += 1
        print(feq1)
        l, r = 0, len(s1)
        while r < len(s2) + 1:
            feq2 = defaultdict(int)
            for c in s2[l:r]:
                feq2[c] += 1
            print(feq2, s2[l:r])
            if feq2 == feq1:
                print(feq2)
                return True
            l += 1
            r += 1
        return False