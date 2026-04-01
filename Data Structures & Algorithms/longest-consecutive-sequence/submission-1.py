class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        mp = {}
        for n in sorted(nums):
            for k in mp.keys():
                if k+mp[k] + 1 == n:
                    mp[k] += 1
            mp[n] = 0
            print(mp)
        max = 0
        for k,v in mp.items():
            if v > max:
                max = v
        return max + 1