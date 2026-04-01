class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)
        l = 0
        t = -1
        while l < r:
            cur = int((r-l)/2) + l
            if cur == t:
                return -1
            t = cur
            if nums[t] == target:
                return t
            elif nums[t] > target:
                r = t
            else:
                l = t
        return 0 if nums[0] == target else -1