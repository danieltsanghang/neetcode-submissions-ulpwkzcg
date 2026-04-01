class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
        for c in t:
            if c not in mp or mp[c] == 0:
                return False
            mp[c] -= 1
        return True
