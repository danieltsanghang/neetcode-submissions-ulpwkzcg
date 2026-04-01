class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for pos, i in enumerate(nums):
            mp[target-i] = pos
        for pos, i in enumerate(nums):
            if i in mp and mp[i] != pos:
                return [pos, mp[i]]