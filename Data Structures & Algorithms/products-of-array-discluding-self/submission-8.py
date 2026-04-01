class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for n in nums]
        right = [1 for n in nums]
        for pos, n in enumerate(nums):
            if pos == 0:
                left[pos] = 1
            else:
                left[pos] = left[pos-1] * nums[pos-1]

            r = len(nums) - pos - 1
            if r == len(nums)-1:
                right[r] = 1
            else:
                right[r] = right[r+1] * nums[r+1]

        return [left[i] * right[i] for i in range(len(nums))]