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
                feq[removed] -= 1
                l += 1
            res = r-l+1

        return res
