class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums) too easy??
        l, r = 0, len(nums) - 1
        while l < r:
            c = (l+r) // 2
            if nums[c] < nums[r]:
                r = c
            else:
                l += 1
        return nums[l]