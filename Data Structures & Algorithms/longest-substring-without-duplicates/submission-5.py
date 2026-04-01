class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ct = []
        for c in s:
            if c not in ct:
                ct += [c]
            else:
                ct = ct[ct.index(c)+1:] + [c]
            print(ct)
            l = max(l, len(ct))
        return l