class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for str in strs:
            mp[hash(tuple(sorted(str)))] += [str]
            print(mp)
        return list(mp.values())