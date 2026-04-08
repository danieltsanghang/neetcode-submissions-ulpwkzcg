class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        feq = defaultdict(int)
        res = 0
        for r in range(len(s)):
            window_size = (r-l+1)
            c = s[r]
            feq[c] += 1
            if window_size - max(feq.values()) > k:
                removed = s[l]
                print('popped', removed)
                feq[removed] -= 1
                l += 1
            res = max(res, r-l+1)
            print(res, feq, l, r, c)

        return res
