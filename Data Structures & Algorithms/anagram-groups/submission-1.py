class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for str in strs:
            mp[hash(tuple(sorted(str)))] += [str]
        return list(mp.values())