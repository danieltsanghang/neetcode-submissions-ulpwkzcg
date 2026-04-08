class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        feq = defaultdict(int)
        res = 0
        for r in range(len(s)):
            window_size = (r-l+1)
            c = s[r]
            feq[c] += 1
            # if the current window is not valid, shrink left bound by
            # 1 so that the window width is still the current best length
            if window_size - max(feq.values()) > k:
                removed = s[l]
                feq[removed] -= 1
                l += 1 # this stops the res from increasing when the window is invalid
            res = r-l+1

        return res
